"""
MW-Wiki Knowledge Graph Engine
Builds a networkx graph from topic files and exports to _graph.json for D3 visualization.
"""

from __future__ import annotations
import json
import logging
import re
from pathlib import Path
from collections import defaultdict

import networkx as nx
import yaml

log = logging.getLogger(__name__)

WIKI_DIR  = Path(__file__).parent.parent / "wiki"
GRAPH_OUT = WIKI_DIR / "_graph.json"

DOMAIN_COLORS = {
    "identity":  "#3b82f6",   # blue
    "intune":    "#22c55e",   # green
    "sentinel":  "#ef4444",   # red
    "defender":  "#f97316",   # orange
    "exchange":  "#a855f7",   # purple
    "teams":     "#06b6d4",   # cyan
    "azure":     "#eab308",   # yellow
    "unknown":   "#64748b",   # grey
}

EDGE_COLORS = {
    "EXPLAINS":    "#3b82f6",
    "REQUIRES":    "#22c55e",
    "CONTRADICTS": "#ef4444",
    "SUPERSEDES":  "#f97316",
    "CITED_BY":    "#a855f7",
    "CO_AUTHOR":   "#64748b",
}


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


def get_domain(topic_path: str) -> str:
    """Extract top-level domain from topic path like identity/conditional-access/..."""
    parts = topic_path.split("/")
    return parts[0] if parts else "unknown"


def build_graph() -> nx.DiGraph:
    G = nx.DiGraph()

    topic_files = list(WIKI_DIR.rglob("*.md"))
    topic_files = [f for f in topic_files if not f.name.startswith("_")]

    log.info(f"Building graph from {len(topic_files)} topic files...")

    author_topics: dict[str, list[str]] = defaultdict(list)
    all_topics: dict[str, dict] = {}

    # ── Pass 1: add topic nodes ──────────────────────────────────────────────
    for tf in topic_files:
        rel = tf.relative_to(WIKI_DIR)
        topic_id = str(rel).replace(".md", "").replace("\\", "/")
        content = tf.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(content)

        domain = get_domain(topic_id)
        color  = DOMAIN_COLORS.get(domain, DOMAIN_COLORS["unknown"])

        sources   = meta.get("sources", []) or []
        authors   = list({s.get("author", "Unknown") for s in sources if s.get("author")})
        dates     = [s.get("date", "") for s in sources if s.get("date")]
        latest    = max(dates) if dates else ""
        src_count = len(sources)

        # Word count as proxy for depth
        word_count = len(body.split())

        G.add_node(
            topic_id,
            type       = "topic",
            label      = topic_id.split("/")[-1].replace("-", " ").title(),
            domain     = domain,
            color      = color,
            authors    = authors,
            src_count  = src_count,
            latest     = latest,
            word_count = word_count,
            size       = max(8, min(30, src_count * 4 + 8)),
        )

        all_topics[topic_id] = {"meta": meta, "body": body, "authors": authors}

        for author in authors:
            author_topics[author].append(topic_id)

    # ── Pass 2: add author nodes ─────────────────────────────────────────────
    for author, topics in author_topics.items():
        author_id = f"author::{author.lower().replace(' ', '_')}"
        G.add_node(
            author_id,
            type   = "author",
            label  = author,
            color  = "#f1f5f9",
            size   = max(10, min(35, len(topics) * 3 + 10)),
            topics = topics,
        )
        for topic_id in topics:
            G.add_edge(author_id, topic_id,
                       type=  "CITED_BY",
                       color= EDGE_COLORS["CITED_BY"],
                       weight= 1)

    # ── Pass 3: infer REQUIRES edges from keyword co-occurrence ─────────────
    # Topics that share many keywords likely have a prerequisite relationship
    topic_keywords: dict[str, set[str]] = {}
    for topic_id, data in all_topics.items():
        body = data["body"].lower()
        words = set(re.findall(r'\b[a-z]{4,}\b', body))
        topic_keywords[topic_id] = words

    topic_ids = list(all_topics.keys())
    for i, t1 in enumerate(topic_ids):
        for t2 in topic_ids[i+1:]:
            shared = topic_keywords[t1] & topic_keywords[t2]
            score  = len(shared) / max(len(topic_keywords[t1]), len(topic_keywords[t2]), 1)
            if score > 0.35:
                # High overlap — likely related
                G.add_edge(t1, t2,
                           type=   "REQUIRES",
                           color=  EDGE_COLORS["REQUIRES"],
                           weight= round(score, 2))

    # ── Pass 4: CONTRADICTS edges from _conflicts.md ────────────────────────
    conflicts_file = WIKI_DIR / "_conflicts.md"
    if conflicts_file.exists():
        conflicts_text = conflicts_file.read_text(encoding="utf-8")
        # Extract topic references from conflicts
        mentioned = re.findall(r'`([a-z/\-]+)`', conflicts_text)
        mentioned = [m for m in mentioned if m in all_topics]
        for i in range(len(mentioned) - 1):
            t1, t2 = mentioned[i], mentioned[i+1]
            if t1 != t2 and t1 in G and t2 in G:
                G.add_edge(t1, t2,
                           type=   "CONTRADICTS",
                           color=  EDGE_COLORS["CONTRADICTS"],
                           weight= 1)

    # ── Pass 5: gap nodes ────────────────────────────────────────────────────
    gaps_file = WIKI_DIR / "_gaps.md"
    if gaps_file.exists():
        gaps_text = gaps_file.read_text(encoding="utf-8")
        gap_topics = re.findall(r'`([a-z/\-]+)`', gaps_text)
        for gap in set(gap_topics):
            if gap not in G:
                domain = get_domain(gap)
                G.add_node(
                    gap,
                    type   = "gap",
                    label  = gap.split("/")[-1].replace("-", " ").title(),
                    domain = domain,
                    color  = "#ef4444",
                    size   = 8,
                    pulsing= True,
                )

    log.info(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G


def export_graph(G: nx.DiGraph) -> dict:
    """Export graph to D3-compatible JSON."""

    node_index = {n: i for i, n in enumerate(G.nodes())}

    nodes = []
    for node_id, data in G.nodes(data=True):
        nodes.append({
            "id":        node_id,
            "index":     node_index[node_id],
            "type":      data.get("type", "topic"),
            "label":     data.get("label", node_id),
            "color":     data.get("color", "#64748b"),
            "size":      data.get("size", 8),
            "domain":    data.get("domain", ""),
            "authors":   data.get("authors", []),
            "src_count": data.get("src_count", 0),
            "latest":    data.get("latest", ""),
            "pulsing":   data.get("pulsing", False),
        })

    links = []
    for src, tgt, data in G.edges(data=True):
        links.append({
            "source": node_index[src],
            "target": node_index[tgt],
            "type":   data.get("type", "RELATED"),
            "color":  data.get("color", "#334155"),
            "weight": data.get("weight", 1),
        })

    graph_data = {
        "nodes": nodes,
        "links": links,
        "meta": {
            "topic_count":  sum(1 for n in nodes if n["type"] == "topic"),
            "author_count": sum(1 for n in nodes if n["type"] == "author"),
            "gap_count":    sum(1 for n in nodes if n["type"] == "gap"),
            "edge_count":   len(links),
            "domains":      list(DOMAIN_COLORS.keys()),
            "edge_types":   list(EDGE_COLORS.keys()),
            "colors":       {**DOMAIN_COLORS, **EDGE_COLORS},
        }
    }

    GRAPH_OUT.write_text(json.dumps(graph_data, indent=2), encoding="utf-8")
    log.info(f"Graph exported → {GRAPH_OUT}")
    return graph_data


def build_and_export() -> dict:
    G = build_graph()
    return export_graph(G)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    build_and_export()
