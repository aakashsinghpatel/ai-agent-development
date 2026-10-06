from fastmcp import FastMCP

server = FastMCP("Weather Server")

@server.tool()
def get_weather(city:str):
    """ Method to return city of temprature """
    # This method take argument also in tool call
    print("tool called with arg:", city)
    city_temprature = {"Indore":"25 Degree", 
                      "Patna":" 32 Degree",
                      "Delhi":"40 Degree"}

    return  city_temprature.get(city.capitalize(),"Weather data not availa0ble.")


# Mcp resource use to share resource to clinet
@server.resource("weather:/cities")
def get_wether_cities():
    return ["indore", "Delhi"]

@server.prompt()
def get_wether_report(city):
    prompt= f""" 
        you ar an intelligent reprt creater
        User input:{city}
        please create a good report on this city wether. 
     """
    return prompt

if __name__ == "__main__":
    """ When server on local """
    # server.run()
    """ When server on remote then this file we have to run manually to start server """
    server.run(transport="http", host="127.0.0.1", 
        port=8000) 