from config import MODEL, OLLAMA_BASE_URL
from langchain_ollama import ChatOllama


model = ChatOllama(model=MODEL, base_url=OLLAMA_BASE_URL)