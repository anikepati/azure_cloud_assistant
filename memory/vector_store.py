from chromadb import Client
from chromadb.config import Settings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

class VectorStore:
    def __init__(self, collection_name="anomaly_data"):
        self.client = Client(Settings(anonymized_telemetry=False))
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=OpenAIEmbeddingFunction()
        )

    def add_document(self, doc_id: str, text: str):
        self.collection.add(documents=[text], ids=[doc_id])

    def query(self, query: str, top_k: int = 3):
        return self.collection.query(query_texts=[query], n_results=top_k)