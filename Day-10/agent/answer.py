from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))



def format_answer(state):
    """ Method to format the and create final ansewer from state dict """
    prompt = f"""
            The user asked:
            {state["user_request"]}
    
            Actions performed:
            {state["actions"]}
    
            Observations:
            {state["observations"]}

            tasks: {state['tasks']}

            Intermediate Results:
            {state["results"]}

            Give the user a natural and concise answer.

            Do not mention:
            - planner
            - agent loop
            - MCP
            - internal state
            - tools
            - internal reasoning
            """
    response = client.chat.completions.create(model=os.getenv("ASSISTANT_MODEL"),
            messages=[{"role": "user","content": prompt}])
    
    return response.choices[0].message.content.strip()