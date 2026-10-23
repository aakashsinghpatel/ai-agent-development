from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio

from mcp_client import connent_mcp, disconnect_mcp,discover_tools, execute_tool

# Load configuratio
load_dotenv()

# Create AI model client
client = OpenAI(base_url=os.getenv("BASE_URL"),api_key=os.getenv("API_KEY"))

def planner(user_input, tool_list):
    """ Method that return the tool name to be used for user query to full fill """
    tool_description = build_tool_description(tool_list)
    prompt=f""" 
        You are an intelligent AI planner.
        Available tools:
        {tool_description}
        User Query: {user_input}

        You have to select the best match tool for user query.
        Just return the tool name ONLY.
        If not tool matched found for user Query then just return 'None'
        Do not return description.  
     """
    response = client.chat.completions.create(model=os.getenv("ASSITANT_MODEL"), 
                                              messages=[{
                                                  "role":"user",
                                                  "content":prompt
                                              }])
    return response.choices[0].message.content.strip() 
    # return None

def build_tool_description(tool_list):
    """ Create tool description for all tool of MCP server """
    tool_description = '' 
    for tool in tool_list:
        tool_description+=f""" 
        Tool Name:{tool.name}
        Tool Description:{tool.description}
        """
    return tool_description

def generate_response(user_input, tool_result):
    """ Method to generate natural response for the user query based on response of tool """
    prompt= f""" 
        User Query: {user_input}
        Tool Response: {tool_result}
        Create the natural respose based on available tools response only.
     """
    response = client.chat.completions.create(model=os.getenv("ASSITANT_MODEL"),
                                              messages=[
                                                  {"role":"user", "content":prompt}
                                              ])
    return response.choices[0].message.content

# MCP 
async def mcp_main():
    # Step 1: connect to MCP
    mcp_client = await connent_mcp()

    #step 2 : Disciver all available tools
    tool_list  = await discover_tools(mcp_client)
    print("---------- Available tools----------")
    for tool in tool_list:
        print(f"{tool.name}:{tool.description}")
    print("---------- Available tools----------")

    
    # step 3: Create tool Planner: Ollam select tool base on query
        # create a planner that take tool and user request and retuen toolname that best match
        # -----
        # tool_description=''
        # for tool in tool_list:
        #     tool_description+=f""" 
        #     Tool name: {tool.name} 
        #     Tool Description: {tool.description}
        #     """
        # print("Created tool description is : ", tool_description)
        # -----

        # Take user input
    user_input = input(" You: ")
    tool_name = planner(user_input, tool_list)
    # print("Selected tool for user Query is:", tool_name)

    # step 4: Request MCP to execute tool: request MCP to execute selected tool
    tool_result = await execute_tool(mcp_client,tool_name)
    
    # step 5: Generate natural lanugae response
    ai_response = generate_response(user_input, tool_result)     

    #step 6: Show natural response
    print(" AI:", ai_response)

    # close the connection with mcp
    await disconnect_mcp(mcp_client)

if __name__ == "__main__":
    asyncio.run(mcp_main())