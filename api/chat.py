"""
RAG Chat API endpoint for Scott Adams Wiki.
Uses Qdrant Cloud for retrieval and Gemini for generation.
"""

import json
import os
from http.server import BaseHTTPRequestHandler

from google import genai
from qdrant_client import QdrantClient

# Config from environment
QDRANT_CLOUD_URL = os.environ.get("QDRANT_CLOUD_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
COLLECTION = "scott_adams_chunks"

# Initialize clients lazily
_gemini = None
_qdrant = None

def get_gemini():
    global _gemini
    if _gemini is None:
        _gemini = genai.Client(api_key=GEMINI_API_KEY)
    return _gemini

def get_qdrant():
    global _qdrant
    if _qdrant is None:
        _qdrant = QdrantClient(url=QDRANT_CLOUD_URL, api_key=QDRANT_API_KEY)
    return _qdrant


def embed_query(text):
    result = get_gemini().models.embed_content(
        model="gemini-embedding-001",
        contents=text,
    )
    return result.embeddings[0].values


def search_chunks(query, limit=5):
    query_vector = embed_query(query)
    results = get_qdrant().search(
        collection_name=COLLECTION,
        query_vector=query_vector,
        limit=limit,
    )
    return [
        {
            "text": r.payload.get("text", ""),
            "episode_title": r.payload.get("episode_title", ""),
            "episode_date": r.payload.get("episode_date", ""),
            "url": r.payload.get("url", ""),
            "timestamp": r.payload.get("start_timestamp", ""),
            "score": r.score,
        }
        for r in results
    ]


def generate_answer(query, contexts):
    context_text = "\n\n---\n\n".join([
        f"Episode: {c['episode_title']} ({c['episode_date']})\n"
        f"Timestamp: {c['timestamp']}\n"
        f"Content: {c['text']}"
        for c in contexts
    ])
    
    prompt = f"""You are an AI assistant for the Scott Adams Wiki.

Based on these excerpts from "Coffee with Scott Adams", answer the question.
- Quote Scott directly when relevant
- Mention which episode the info comes from
- Be accurate to his actual views

CONTEXT:
{context_text}

QUESTION: {query}

ANSWER:"""

    response = get_gemini().models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )
    return response.text


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            data = json.loads(body)
            query = data.get("query", "")
            
            if not query:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Missing query"}).encode())
                return
            
            contexts = search_chunks(query, limit=5)
            answer = generate_answer(query, contexts)
            
            response = {
                "answer": answer,
                "sources": [
                    {
                        "episode": c["episode_title"],
                        "date": c["episode_date"],
                        "url": c["url"],
                        "timestamp": c["timestamp"],
                    }
                    for c in contexts
                ]
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
