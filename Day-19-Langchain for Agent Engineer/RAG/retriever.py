from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

from pathlib import Path

# 1. Load document
loader = TextLoader(Path("knowledge/notes.txt"),encoding="UTF-8")
documents = loader.load()

print("Document loaded")

# 2. chumk documents
# Recurssively chunk the documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50)
chunks = splitter.split_documents(documents)
print("Docuemnt chunked")
# 3. Embedd documents
# Crete function/model to embedd
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# 4. Store in Vector DB
""" FAISS use the model and cover into the chunk """
# it store the embedding only into VS not whole chunk it take 
# embedding mpdel as parsam and embedd itS
vector_store = FAISS.from_documents(
    chunks,
    embeddings
)
print("Vectore store created")
# 5. retriver function/method
retriever = vector_store.as_retriever()