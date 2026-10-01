
from tools import get_current_time,generate_password,roll_dice, read_text_file


def execute_tool(input):
    user_input= input.lower()
    '''Manager to decide which toll need to be called base don user input'''
    if "time" in user_input or "clock" in user_input:
        return get_current_time()
    elif "password" in user_input or "passcode" in user_input:
        return generate_password()
        
    elif "roll" in user_input or "dice" in user_input:
        return roll_dice()

    elif "summarize" in user_input or "explain" in user_input or "ask" in user_input:
        filename = ''
        if "summarize" in user_input:
            filename = user_input[10:]
        elif "explain" in user_input:
            filename = user_input[8:]
        elif "ask" in user_input:
            parts = str(user_input).split(maxsplit=2)
            filename = parts[1]
        content =  read_text_file(f"data/{filename}")
        return content
    else:
        return None
            