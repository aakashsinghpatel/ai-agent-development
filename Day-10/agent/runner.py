import asyncio

from mcp_client import connect, disconnect, discover_tool
from loop import run_agent_loop
from planner import planner
from executor import execute_action
from answer import format_answer

async def main():
    mcp_client = await connect()

    """ Get all tool list from mcp server """
    tool_list = await discover_tool(mcp_client)

    print("="*40)
    print("===== Advanced AI Agent (Agent planning: Brek goal on subtask)")
    print("="*40)

    print("\nAvailable Tools")
    print("----------------")

    for tool in tool_list:
        print(tool.name)
    print("----------------")

    user_input = input(" You: ")

    """ Run agen loop """
    state = await run_agent_loop(user_input, planner, execute_action, format_answer, tool_list, mcp_client)

    print(" AI:", state['final_answer'])

    await disconnect(mcp_client)


if __name__ == '__main__':
    asyncio.run(main())