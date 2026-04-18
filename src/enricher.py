"""
MW-Wiki Context Enricher
Reads the knowledge graph and writes related_topics, prerequisite_topics,
and context_note back into each topic file's frontmatter.
Run after librarian completes or on demand.
"""

from __future__ import annotations
import json
import logging
from pathlib import Path
import yaml

log = logging.getLogger(__name__)

WIKI_DIR  = Path(__file__).parent.parent / "wiki"
GRAPH_OUT = WIKI_DIR / "_graph.json"


def parse_frontmatter(content: str) -> tuple[dict, str]:
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
                return meta, parts[2].strip()
            except yaml.YAMLError:
                pass
    return {}, content


def render_frontmatter(meta: dict) -> str:
    return "---\n" + yaml.dump(meta, default_flow_style=False, allow_unicode=True) + "---\n\n"


def enrich_topics():
    if not GRAPH_OUT.exists():
        log.error("Graph not built. Run: python3 src/graph.py first.")
        return

    graph = json.loads(GRAPH_OUT.read_text())
    nodes = {n["id"]: n for n in graph["nodes"]}
    links = graph["links"]

    # Build adjacency — node index to node id
    index_to_id = {n["index"]: n["id"] for n in graph["nodes"]}

    # Build edge map per topic
    edges_by_topic: dict[str, list[dict]] = {}
    for link in links:
        src_id = index_to_id.get(link["source"] if isinstance(link["source"], int) else link["source"])
        tgt_id = index_to_id.get(link["target"] if isinstance(link["target"], int) else link["target"])
        if not src_id or not tgt_id:
            continue
        for topic_id in [src_id, tgt_id]:
            if topic_id not in edges_by_topic:
                edges_by_topic[topic_id] = []
            edges_by_topic[topic_id].append({
                "src": src_id,
                "tgt": tgt_id,
                "type": link["type"],
                "weight": link.get("weight", 1)
            })

    topic_files = [f for f in WIKI_DIR.rglob("*.md") if not f.name.startswith("_")]
    enriched = 0

    for tf in topic_files:
        rel      = tf.relative_to(WIKI_DIR)
        topic_id = str(rel).replace(".md", "").replace("\\", "/")

        content  = tf.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(content)

        edges = edges_by_topic.get(topic_id, [])

        # ── RELATED TOPICS ──
        # REQUIRES edges where this topic is source or target — high overlap topics
        related = []
        for e in edges:
            if e["type"] == "REQUIRES" and e["weight"] >= 0.35:
                other = e["tgt"] if e["src"] == topic_id else e["src"]
                if other != topic_id and not other.startswith("author::") and other not in related:
                    related.append(other)

        # Sort by weight, take top 4
        related = related[:4]

        # ── PREREQUISITE TOPICS ──
        # Topics in the same domain that are "simpler" — fewer sources, higher centrality
        prereqs = []
        current_src_count = nodes.get(topic_id, {}).get("src_count", 0)
        for e in edges:
            if e["type"] == "REQUIRES":
                other = e["tgt"] if e["src"] == topic_id else e["src"]
                if other == topic_id or other.startswith("author::"):
                    continue
                other_node = nodes.get(other, {})
                # Prerequisite = same domain, more sources (more foundational)
                if (other_node.get("domain") == nodes.get(topic_id, {}).get("domain") and
                        other_node.get("src_count", 0) > current_src_count and
                        other not in prereqs):
                    prereqs.append(other)

        prereqs = prereqs[:2]

        # ── CONFLICT TOPICS ──
        conflicts = []
        for e in edges:
            if e["type"] == "CONTRADICTS":
                other = e["tgt"] if e["src"] == topic_id else e["src"]
                if other != topic_id and not other.startswith("author::"):
                    conflicts.append(other)

        # ── CONTEXT NOTE ──
        domain   = nodes.get(topic_id, {}).get("domain", "")
        label    = nodes.get(topic_id, {}).get("label", topic_id)
        src_count = nodes.get(topic_id, {}).get("src_count", 0)
        latest   = nodes.get(topic_id, {}).get("latest", "")

        if related:
            related_labels = [nodes.get(r, {}).get("label", r.split("/")[-1]) for r in related[:2]]
            context_note = (
                f"{label} is part of the {domain} domain. "
                f"It connects closely to {' and '.join(related_labels)}. "
                f"Synthesised from {src_count} community source{'s' if src_count != 1 else ''}."
            )
        else:
            context_note = (
                f"{label} is part of the {domain} domain. "
                f"Synthesised from {src_count} community source{'s' if src_count != 1 else ''}."
            )

        # ── WRITE BACK ──
        changed = False

        if related and meta.get("related_topics") != related:
            meta["related_topics"] = related
            changed = True

        if prereqs and meta.get("prerequisite_topics") != prereqs:
            meta["prerequisite_topics"] = prereqs
            changed = True

        if conflicts and meta.get("conflict_topics") != conflicts:
            meta["conflict_topics"] = conflicts
            changed = True

        if meta.get("context_note") != context_note:
            meta["context_note"] = context_note
            changed = True

        if changed:
            tf.write_text(render_frontmatter(meta) + body, encoding="utf-8")
            enriched += 1
            log.info(f"  Enriched: {topic_id} — {len(related)} related, {len(prereqs)} prereqs")

    log.info(f"Enrichment complete — {enriched}/{len(topic_files)} topic files updated")
    return enriched


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    enrich_topics()
