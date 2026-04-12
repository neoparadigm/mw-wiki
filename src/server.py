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
from fastapi.responses import JSONResponse
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

@app.get("/api/health")
async def health():
    index = load_index()
    return {"status": "ok", "topics": len(index)}

@app.get("/")
async def root():
    return JSONResponse({"name": "MW-Wiki API", "version": "0.1.0", "docs": "/docs"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
