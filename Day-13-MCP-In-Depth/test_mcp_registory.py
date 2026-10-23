import asyncio
from mcp_manager import create_tool_registory, run_tool, close_server, get_all_resources_prompt, get_resource, get_prompt
async def main():
    servers = ["time_mcp_server/server.py", "weather_mcp_server/server.py"]
    try:
        clients, tool_registory = await create_tool_registory(servers)

        # print("tool registory: \n", tool_registory)
        print("Available tools:\n")
        for tool_name, value   in dict(tool_registory).items():
            print(f"Tool name: {tool_name} \nclient name:{value['client']} \n-----------------------------")

        print("execute tool weather")
        #  Pass argument to toolas dictionaly this will arotio conert as name arumen tto tool at
        # server
        weather_result = await run_tool("get_weather", tool_registory, {'city':"Indore"})
        print("Weather result for indore is:", weather_result.content[0].text)
        print("-"*40)
        weather_client = clients[1]
        mcp_prompt, mcp_resources = await get_all_resources_prompt(weather_client)
        print("Prompt available at MCP server:\n", mcp_prompt)
        print("-"*40)
        print("Resources available at MCP server:\n", mcp_resources)
        print("-"*40)
        weather_resource_urI = "weather:/cities"
        weather_resource_data = await get_resource(weather_client, weather_resource_urI)
        print("weather_resource_data at MCP server:\n", weather_resource_data)
        print("-"*40)
        weather_city_prompt =await get_prompt(weather_client,'get_wether_report',{"city": "Indore"})
        print("weather_city_prompt at MCP server:\n", weather_city_prompt)

        # weather_result = await run_tool("get_weather", tool_registory, {'city':"halua"})
        # print("Weather result for indore is:", weather_result.content[0].text)
        # print("-"*40)
        # print("execute tool roll dice")
        # roll_dice_result = await run_tool("roll_dice", tool_registory)
        # print("Roll dice result:", roll_dice_result.content[0].text)

    except :
        print("error")
    finally:
        await close_server(clients)
        print("All connection to clients closed")

if __name__ == "__main__":
    asyncio.run(main())