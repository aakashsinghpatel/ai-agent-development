from fastmcp import FastMCP
from datetime import datetime
import random
import string
import secrets


server = FastMCP("Time Serve")


@server.tool()
def generate_password(length:str = 12):
    """ Method to generate random password """
    password = [secrets.choice(string.ascii_letters),
                secrets.choice(string.punctuation),
                secrets.choice(string.digits)]
    password_characters = string.ascii_letters+string.digits+string.punctuation
    password+=[secrets.choice(password_characters) for _ in range(length-4)]
    return "".join(password)

@server.tool()
def get_current_time():
    """ Method to return current date and time """
    return datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

@server.tool()
def roll_dice():
    return random.randint(0,6)

if __name__ == "__main__":
    server.run()
