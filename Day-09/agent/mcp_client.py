from fastmcp import Client
from pathlib import Path

async def connect():
    """ Method to connect with MCP server """
    client = Client(Path('mcp_server.py'))
    await client.__aenter__()
    print("Connected to MCP server")
    return client

async def discover_tool(client):
    """  Method to return  list of tool available on MCP server """
    return await client.list_tools()

async def execute_tool(client, tool_name, argument= None):
    """ Method to execute tool on MCP server """
    return await client.call_tool(tool_name , argument)

async def disconnect(client):
    """ Methos to terminate/stop mcp server """
    await client.__aexit__()
