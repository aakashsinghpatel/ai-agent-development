
from tools import get_current_time,generate_password,roll_dice


def execute_tool(input):
    user_input= input.lower()
    '''Manager to decide which toll need to be called base don user input'''
    if "time" in user_input or "clock" in user_input:
        return get_current_time()
    elif "password" in user_input or "passcode" in user_input:
        return generate_password()
        
    elif "roll" in user_input or "dice" in user_input:
        return roll_dice()
    else:
        return None
            