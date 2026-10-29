from config import MODEL
from langchain_ollama import ChatOllama


model = ChatOllama(model=MODEL)