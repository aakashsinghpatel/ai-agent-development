
from mcp_manager import run_tool

async def execute_action(mcp_registory, next_action, argumenent):
    result = await run_tool(next_action, mcp_registory, argumenent)
    if hasattr(result, "content"):
        if result.content:
            return result.content[0].text
    return str(result)