from mcp_client import execute_tool

async def execute_action(client, action_name):
    result = await execute_tool(client,action_name)

    if hasattr(result, "content"):
        if result.content:
            return result.content[0].text
    return str(result)