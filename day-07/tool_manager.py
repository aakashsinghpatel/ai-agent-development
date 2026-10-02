
from tools import get_current_time,generate_password,roll_dice


def execute_tool(tool_name):
    '''Manager to decide which tool need to be called base tool name passed'''
    if tool_name == 'get_current_time':
        return get_current_time()
    elif tool_name == 'generate_password':
        return generate_password()
    elif tool_name == 'roll_dice':
        return roll_dice()
            