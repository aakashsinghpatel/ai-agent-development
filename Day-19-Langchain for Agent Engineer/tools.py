from datetime import datetime
import string
import secrets


from langchain_core.tools import tool

""" Make this python function as langchain tools """

@tool()
def current_date_time():
    """ Return current date and time """
    return datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

@tool()
def random_password(length=10):
    "Return generated random password"
    password =[]
    pass_character = string.ascii_letters + string.digits+ string.punctuation
    for i in range(length):
        password+=[secrets.choice(pass_character)]

    return "".join(password)

@tool()
def roll_dice() -> int:
    """Roll a six-sided dice."""
    import random
    return random.randint(1, 6)
