import asyncio
from openai import OpenAI
from dotenv import load_dotenv
import os 

from mcp_client import connect, disconnect, discover_tool
from planner import planner
from loop import run_agent_loop
from executor import execute_action

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

async def main():

    mcp_client = await connect()
    tool_list = await discover_tool(mcp_client)
    
    print("Available Tools")
    print("----------------")

    for tool in tool_list:
        print(tool.name)

    print("="*40)
    print("**** My autonomous AI Agent *********")
    print("="*40)

    user_request = input(" You:")

    state = await run_agent_loop(user_request, planner, execute_action,format_answer,tool_list,mcp_client)
    print()
    print("Final Answer:")
    print(state["final_answer"])
    

if __name__ == "__main__":
    asyncio.run(main())

