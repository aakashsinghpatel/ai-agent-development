
from mcp_client import execute_tool

async def execute_action(mcp_client, next_action):
    result = await execute_tool(mcp_client,next_action)
    if hasattr(result, "content"):
        if result.content:
            return result.content[0].text
    return str(result)