from dotenv import load_dotenv
import os

"""  Security: Centralization
Keeping secrets safe as load from env and env do not pussed to git
 """
load_dotenv()

BASE_URL = os.getenv("ASSISTANT_MODEL") 
MODEL  = os.getenv("ASSISTANT_MODEL", "qwen3b:1.7b") 
API_KEY = os.getenv("API_KEY","ollama") 
MAX_RETRY= os.getenv("MAX_RETRY", 3)
TIMEOUT = os.getenv("TIMEOUT",60) 
MAX_REVISIONS = os.getenv("MAX_REVISIONS",8)