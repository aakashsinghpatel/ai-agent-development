from openai import OpenAI
from dotenv import load_dotenv
import os 


load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))


def format_answer(state):
    prompt = f"""
        The user asked:
        {state["user_request"]}

        Actions performed:
        {state["actions"]}

        Observations:
        {state["observations"]}

        Answer the user naturally.

        Do not mention internal planning.
        Do not mention state.
        Do not mention tools.
        """
    response = client.chat.completions.create(
        model=os.getenv("ASSISTANT_MODEL"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()
