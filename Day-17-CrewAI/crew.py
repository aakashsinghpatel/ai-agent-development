from crewai import Crew, Process
from agents import reviewer_agent,coder_agent,research_agent
from tasks import research_task, coding_task, review_task

crew = Crew(
    agents=[
        reviewer_agent,
        coder_agent,
        reviewer_agent
    ],
    tasks=[
        research_task,
        coding_task,
        review_task
    ],
    process=Process.sequential,
    verbose=True
)