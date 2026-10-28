from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(model='ollama/qwen3:1.7b')

# Can use specific model for manager of multi agent
llm_manager = LLM(model='ollama/qwen3:1.7b')