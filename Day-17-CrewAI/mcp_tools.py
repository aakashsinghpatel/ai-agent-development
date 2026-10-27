from mcp_client import connent_mcp, execute_tool, disconnect_mcp

import asyncio
from crewai.tools import tool
# Adpter to connect with MCP tool via CrewAI tool
async def call_mcp_current_date_time():
    try:    
        client = await connent_mcp()
        result = await execute_tool(client=client, tool_name="get_current_time")
        return result.content[0].text
    finally:
        await disconnect_mcp(client)

# Creating CrewAI tool this will link into agent
# mcp_current_time() got an unexpected keyword argument 'operation': to get reid fro erro pass operaion
@tool("MCP Current Time")
def mcp_current_time(operation: str = "current_time") -> str:
    """ Get the current date and time from MCP """
    return asyncio.run(call_mcp_current_date_time())
    