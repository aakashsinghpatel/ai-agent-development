from fastmcp import FastMCP
from datetime import datetime
import random
import string
import secrets

mcp_server = FastMCP("First Time Server")


""" Now create tool that available on MCP server 
@decorator: that tell that this are tool availble with serve and expose to client
asynt method:
 doc sting: This are not for programmer bit for server/ client that descibe the use case of tool.
 This will be expose to outside AI agent so thta they use it for getting know when it get call
"""

@mcp_server.tool()
async def get_current_time():
    """ Return the current date and time """
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")

@mcp_server.tool()
async def roll_dice():
    """ Return the current date and time """
    return random.randint(1,6)

@mcp_server.tool()
async def generate_password(length=12):
    """ Generate random password."""
    permissable_characters=string.ascii_letters+string.punctuation+string.digits
    password = [secrets.choice(string.ascii_letters),secrets.choice(string.punctuation),
                 secrets.choice(string.ascii_uppercase), secrets.choice(string.digits)]
    password += [secrets.choice(permissable_characters) for _ in range(length-4)]
    return "".join(password)


if __name__ == "__main__":
    print("Starting MCP server")
    mcp_server.run()

