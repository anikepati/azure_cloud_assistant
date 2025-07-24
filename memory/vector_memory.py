import chromadb

class VectorMemory:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("azure-agent-memory")

    def add_context(self, text, metadata):
        self.collection.add(documents=[text], metadatas=[metadata], ids=[metadata['id']])

    def query_context(self, query):
        return self.collection.query(query_texts=[query], n_results=3)