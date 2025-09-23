import csv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance

QDRANT_HOST = "qdrant"
QDRANT_PORT = 6333
COLLECTION_NAME = "movies"

model = SentenceTransformer("all-MiniLM-L6-v2")
qclient = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)


VECTOR_SIZE = model.get_sentence_embedding_dimension()
try:
    qclient.get_collection(COLLECTION_NAME)
except Exception:
    qclient.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
    )

points = []
batch_size = 64
with open("movies.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader):
        text = (row.get("plot") or "") + " " + (row.get("title") or "")
        vector = model.encode(text).tolist()
        payload = {
            "title": row.get("title"),
            "year": row.get("year"),
            "genres": row.get("genres"),
            "plot": row.get("plot"),
            "imdb_id": row.get("imdb_id")
        }
        points.append(PointStruct(id=idx, vector=vector, payload=payload))

        if len(points) >= batch_size:
            qclient.upsert(collection_name=COLLECTION_NAME, points=points)
            print(f"Upserted {len(points)} points")
            points = []

if points:
    qclient.upsert(collection_name=COLLECTION_NAME, points=points)
    print(f"Upserted final {len(points)} points")
