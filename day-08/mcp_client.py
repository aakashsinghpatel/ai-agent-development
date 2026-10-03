from fastmcp import Client
from pathlib import Path

async def connent_mcp():
    """ Connect with MCP Server """
    # client  = Client("mcp_server.py")
    client = Client(Path("mcp_server.py"))
    await client.__aenter__()
    print("Connected to MCP server")
    return client

async def disconnect_mcp(client):
    """ Close the MCP connecttion """
    await client.__aexit__(None, None, None)



async def discover_tools(client):
    """ Return list of All available tool of MCP server """
    tool_list = await client.list_tools()

    return tool_list

async def execute_tool(client, tool_name, argument=None):
    """ Execute the tool that available on server """
    response = await client.call_tool(tool_name, argument)
    return response


