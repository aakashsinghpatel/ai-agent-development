import asyncio
from openai import OpenAI
from dotenv import load_dotenv
import os 

# from mcp_client import connect, disconnect, discover_tool
from planner import planner
from loop import run_agent_loop
from executor import execute_action


from mcp_manager import create_tool_registory, run_tool, close_server

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

mcp_servers_path = ['../time_mcp_server/server.py', "../weather_mcp_server/server.py"]

async def main():

    clients, tool_registory = await create_tool_registory(mcp_servers_path)
    
    print("Available Tools")
    print("----------------")
    tool_list =[]
    print(tool_registory)
    for entry in tool_registory.values():
        tool_list.append(entry['tool'])

    for tool in tool_list:
        print(tool.name)

    print("="*80)
    print("**** My autonomous AI Agent with multi MCP server call*********")
    print("="*80)

    user_request = input(" You:")

    state = await run_agent_loop(user_request, planner, execute_action,format_answer,tool_list, tool_registory)
    print()
    print("Final Answer:")
    print(state["final_answer"])
    

if __name__ == "__main__":
    asyncio.run(main())

