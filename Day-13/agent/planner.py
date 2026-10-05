from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"),base_url=os.getenv("BASE_URL"))

def get_tool_description(tool_list):
    """ Methos to return all list of tools """
    tool_description = ''
    for tool in tool_list:
        tool_description+= f""" 
            Tool Name:{tool.name}
            Tool Description: {tool.description}
            Tool argument: {tool.input_schema}
         """
    return tool_description

def planner(state, tool_list):
    """ Planner : Planner with retutn a dictionry of next_action/tool_name with 
    respective argument based on current state
      """
    available_tools = get_tool_description(tool_list)
    prompt = f"""  
    You are an intelligent Planner.
    Your job is to only decide next action.
    user Request: {state['user_request']}

    Available Tools:
    {available_tools}

    completed action:
    {state['actions']}

    Previous observation:
    {state['observations']}

    Instruction:
        1. Choose only ONE next action.
        2. Never repeat an action that has already been completed.
        3. Use the observations to decide what is still required.
        4. If the user's request has been completely satisfied, return FINISH.
        5. Always Return ONLY valid JSON.
        6. Do not explain your answer.

        Use exactly this format to return the next action:
        {{"tool": "tool_name, "arguments":{{'argument_name': 'argument_value'}}}}
        For FINISH return:
        {{"tool": "FINISH", "arguments":{{}}}}

    """

    response = client.chat.completions.create(model=os.getenv("ASSISTANT_MODEL"),
                                   messages=[{'role':'user', 'content':prompt}])
    
    result = response.choices[0].message.content
    print("Planner result:\n", result)
    return json.loads(result)