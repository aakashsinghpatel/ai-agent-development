from langchain.agents import create_agent
from model import model
from tools import (current_date_time, roll_dice, random_password)


available_tools = [current_date_time, roll_dice, random_password] 

agent = create_agent(model=model, tools= available_tools)

def call_autonomous_agent(user_request):

    """ With .invoke(): whole agent loop will be handle no need to write manual
     code for function call and loop handling all will be hnadle by langchain agent """
    response = agent.invoke(user_request)

    return response

