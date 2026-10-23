
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))


def build_tool_description(tool_list):
    """ Created tool description of the tool got from MCP server """
    tool_description =""
    for tool in tool_list:
        tool_description += f""" 
            Tool Name: {tool.name}
            Tool description: {tool.description}
         """
    return tool_description


def planner(state, tool_list):
    """ Planner with decide next task and action"""
    tool_description = build_tool_description(tool_list)

    prompt = f""" 
        You are an intelligent planner.
        Your job is to select next unfinished task and best tool to complete it.

        user request:
        {state['user_request']}

        pending task:
        {[ item["task"] for item in state['tasks'] if item['status']== 'PENDING']}

        Observation:
        {state["observations"]}

        Intermediate Results:
        {state["results"]}

        Available Tools:
        {tool_description}

        Rules:
        1. Select only one pending task.
        2. The TASK must be copied EXACTLY from the
            pending task list.
        3. Do not change the task wording.
        4. Do not select a completed task.
        5. Select the best available tool for that task.
        6. Use previous observations and results.
        7. If an action failed, reconsider the task.
        8. If tasks are still PENDING task, return exactly in this format: cls{{"task": <exact pending task>, "tool": <tool_name>}}
        9. If there are no PENDING task, return ONLY in same format : {{"task": "FINISH"}}
        10. Do not explain anything.
        11. Return ONLY a valid JSON object.
        Next Decision:
     """
    response = client.chat.completions.create(
        model=os.getenv("ASSISTANT_MODEL"),
        messages=[
            {
                "role": "system",
                "content": "You are an AI planner."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content.strip()


