from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from memory.vector_store import VectorStore

class GenAIAnalyzer:
    def __init__(self):
        self.vstore = VectorStore()
        self.llm = ChatOpenAI(temperature=0)
        self.chain = RetrievalQA.from_chain_type(llm=self.llm, retriever=self.vstore.collection.as_retriever())

    def analyze(self, query: str):
        return self.chain.run(query)