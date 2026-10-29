""" connet to mcp server and call tool """


# from langchain_mcp_client_adpter import client
from langchain.agents import create_agent
from model import model
from langchain_mcp_client_adpter import get_mcp_tools
import asyncio

async def main():
    try:
        tools = await get_mcp_tools()
        print("All availbe tool of server:\n", tools)

        user_query = input("What is your query::")

        """ create agent with MCP tools"""
        agent  = create_agent(model=model, tools=tools)
        response = await agent.ainvoke({
                "messages": [
                    {
                        "role": "user",
                        "content": user_query
                    }
                ]
            })
        print("="*50)
        print("Agent whole response")
        print(response)
        print("="*50)
        print("Agent expected response")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())