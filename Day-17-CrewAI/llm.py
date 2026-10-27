from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(model='ollama/qwen3:1.7b')