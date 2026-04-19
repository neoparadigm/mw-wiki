"""
MW-Wiki Server
"""
import logging
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from query import query as run_query, load_index

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="MW-Wiki")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class QuestionRequest(BaseModel):
    question: str

@app.post("/api/query")
async def query_endpoint(req: QuestionRequest):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    result = run_query(req.question)
    return {"answer": result.answer, "topics_used": result.topics_used, "sources": result.sources, "warnings": result.warnings, "citations_ok": result.citations_ok}

@app.get("/api/index")
async def get_index():
    index = load_index()
    return {"topics": index}

@app.get("/api/health")
async def health():
    import yaml
    index = load_index()
    raw_dir = BASE_DIR / "raw"
    processed = BASE_DIR / "raw" / ".processed.txt"
    articles_crawled = len(list(raw_dir.glob("*.md"))) if raw_dir.exists() else 0
    articles_processed = len(processed.read_text().splitlines()) if processed.exists() else 0
    gaps_file = BASE_DIR / "wiki" / "_gaps.md"
    gaps = gaps_file.read_text().count("| `") if gaps_file.exists() else 0
    return {
        "status": "ok",
        "topics": len(index),
        "articles_crawled": articles_crawled,
        "articles_processed": articles_processed,
        "gaps": gaps,
    }


@app.get("/api/graph")
async def get_graph():
    graph_file = BASE_DIR / "wiki" / "_graph.json"
    if graph_file.exists():
        import json
        return JSONResponse(json.loads(graph_file.read_text()))
    return JSONResponse({"error": "Graph not built yet. Run: python3 src/graph.py"}, status_code=404)

@app.get("/graph")
async def graph_ui():
    ui_file = BASE_DIR / "ui" / "graph.html"
    if ui_file.exists():
        return FileResponse(ui_file)
    return JSONResponse({"error": "graph.html not found"}, status_code=404)

@app.get("/")
async def root():
    ui_file = BASE_DIR / "ui" / "index.html"
    if ui_file.exists():
        return FileResponse(ui_file)
    return JSONResponse({"name": "MW-Wiki API", "version": "0.1.0", "docs": "/docs"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
