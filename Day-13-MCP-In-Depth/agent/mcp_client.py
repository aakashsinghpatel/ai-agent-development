from fastmcp import Client

""" Method to connect with passed argument named seve """
async def connect(server_path):
    client = Client(server_path)
    await client.__aenter__()
    print("Connected to MCP server:", server_path)
    return client


""" Method to disconnect with named client of server """
async def disconnet(client):
    await client.__aexit__(None, None, None)


""" Method to get all available tool of server """
async def discover_tool(client):
    tools = await client.list_tools()
    return tools

""" Method to execute the tool of on passd client linked server """
async def execute_tool(client, tool_name, argument=None):
    return await client.call_tool(tool_name, argument)
