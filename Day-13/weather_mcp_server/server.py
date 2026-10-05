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

if __name__ == "__main__":
    server.run()