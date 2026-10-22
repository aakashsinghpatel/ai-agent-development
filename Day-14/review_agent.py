from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

def review_code(task,code):
   
    prompt = f"""
        You are a Reviewer Agent.

        Review the following solution.

        Task:
        {task}

        Solution:
        {code}

        Check:

        1. Correctness
        2. Python syntax
        3. Logic
        4. Missing issues
        5. Possible improvements

        Return ONLY valid JSON.

        Use exactly this format:

        {{
            "status": "approved",
            "feedback": "The solution is correct."
        }}

        OR:

        {{
            "status": "needs_revision",
            "feedback": "Explain what needs to be changed."
        }}

        Use "approved" only when the solution is acceptable.

        Use "needs_revision" when the solution requires a correction.
        """

    response = client.chat.completions.create(model=os.getenv("ASSISTANT_MODEL"), messages=[
            {"role":"user", "content":prompt}
    ])

    return  response.choices[0].message.content
