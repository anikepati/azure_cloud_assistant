from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        try:
            self.model = OpenAIEmbeddings()
        except:
            self.model = HuggingFaceEmbeddings(model_name=model_name)

    def embed(self, text):
        return self.model.embed_query(text)