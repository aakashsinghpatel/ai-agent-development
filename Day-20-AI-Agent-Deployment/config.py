from dotenv import load_dotenv
import os
load_dotenv()

MODEL = os.getenv("LLM_Model")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
