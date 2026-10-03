
import asyncio
from mcp_client import *

async def main():

    # Connect to mcp client
    client = await connent_mcp()

    # get list of available tools
    tool_list = await discover_tools(client)
    print("Too List", tool_list)
    print("Available Tools")
    for tool in tool_list:
        print(f"{tool.name}: {tool.description}")
    print("----------------")

    # Execute tool
    response = await execute_tool(client, 'roll_dice')
    print("Tool response", response.content[0].text)

    # close the connection with mcp
    await disconnect_mcp(client)

asyncio.run(main())