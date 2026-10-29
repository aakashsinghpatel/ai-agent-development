from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatOllama(model=os.getenv("ASSISTANT_MODEL"))