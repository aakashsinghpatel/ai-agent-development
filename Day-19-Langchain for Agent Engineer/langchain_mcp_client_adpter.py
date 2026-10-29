

# Created adapter fro connection MCP tool with langchain

# from langchain_mcp_adapters.client import MultiServerMCPClient
# With this there is issue to connect with fast mcp server of fasmc as fastmcpo >mcp 2.00 
# and langchain-mcp-adapters  require mcp of <2.
""" client_old = MultiServerMCPClient({
        "time_server": {
            "transport": "stdio",
            "command": "python",
            "args": [
                "mcp_server.py"
            ]
        }
    }
) """

# new impor tot connect wqith fast mcp
from langchain.mcp import MCPAdapter

config = {
    "mcpServers": {
        "time_server": {
            "command": "python",
            "args": ["mcp_server.py"]
        }
    }
}

async def get_mcp_tools():

    async with MCPAdapter(config) as adapter:
        tools = await adapter.list_tools()
        print(tools)
        return tools