import asyncio
from openai import OpenAI
from dotenv import load_dotenv
import os 

from agent.mcp_client import connect, disconnect, discover_tool
from graph import build_graph

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))


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

    graph = build_graph(tool_list, mcp_client)

    user_request = input(" You:")

    initial_state = {
        "user_request": user_request,
        "current_step": 0,
        "max_step": 5,
        "actions": [],
        "observations": [],
        "finished": False,
        "action":'',
        "final_answer": ""
    }

    # final_state = graph.invoke(initial_state)

    # Run graph asynchronously
    final_state = await graph.ainvoke(initial_state)

    
    print()
    print("Final Answer:")
    print(final_state['final_answer'])
    await disconnect(mcp_client)
    

if __name__ == "__main__":
    asyncio.run(main())

