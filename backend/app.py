from fastapi import FastAPI, Query
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter
from sentence_transformers import SentenceTransformer
import os

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
COLLECTION_NAME = "movies"

app = FastAPI(title="IMDB Recommender API")

qclient = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # küçük ve hızlı

@app.get("/search")
def search(q: str = Query(..., min_length=1), limit: int = 5):
    vec = embedder.encode(q).tolist()
    result = qclient.search(
        collection_name=COLLECTION_NAME,
        query_vector=vec,
        limit=limit,
        with_payload=True,
        with_vectors=False
    )
    # result: list of ScoredPoint
    movies = []
    for r in result:
        payload = r.payload or {}
        movies.append({
            "id": r.id,
            "score": r.score,
            "title": payload.get("title"),
            "year": payload.get("year"),
            "genres": payload.get("genres"),
            "plot": payload.get("plot"),
        })
    return {"query": q, "results": movies}
