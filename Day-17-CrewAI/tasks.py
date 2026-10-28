from crewai import Task

from agents import (
    research_agent,
    coder_agent,
    reviewer_agent
)


research_task = Task(
    description=(
        " My name is Akash patel and keep remeber my name for"
        " future tasks"
        "Research the concept of "
        "autonomous AI agents. "
        "Explain the agent loop, "
        "tools, state and observations."
         "Before completing the task, use "
          "the MCP Current Time tool and "
        "include the returned time."
    ),
    expected_output=(
        "A concise technical explanation "
        "of autonomous AI agents."
    ),
    agent=research_agent
)


coding_task = Task(
    description=(
        "Using the research provided by "
        "the researcher, create a simple "
        "Python example of an AI agent loop."
    ),
    expected_output=(
        "A complete Python code example "
        "with a short explanation."
    ),
    agent=coder_agent,
    context=[
        research_task
    ]
)


review_task = Task(
    description=(
        "Review the Python code produced "
        "by the developer. Identify "
        "errors and suggest improvements."
    ),
    expected_output=(
        "A code review containing "
        "identified problems and "
        "recommended improvements."
    ),
    agent=reviewer_agent,
    context=[
        coding_task
    ]
)

memory_task = Task(
                description="What is my name that i have told u in my previos task",
                   expected_output="The name of the person.", agent=research_agent)

