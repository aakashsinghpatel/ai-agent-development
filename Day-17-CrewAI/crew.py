from crewai import Crew, Process
from agents import reviewer_agent,coder_agent,research_agent
from tasks import research_task, coding_task, review_task, memory_task
from llm import llm_manager

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
    memory=True,
    embedder={
            "provider": "ollama",
            "config": {
                "model_name": "nomic-embed-text",
                "url": "http://localhost:11434/api/embeddings"
            }},
    process=Process.hierarchical,
    manager_llm=llm_manager,
    verbose=True
)

""" Creating other crew so that can validate that the data stored by crew 
above access by below or new crew or not """

memmory_crew = Crew(tasks=[memory_task], 
                    agents=[research_agent],
                    memory=True,
                    embedder={
                                "provider": "ollama",
                                "config": {
                                    "model_name": "nomic-embed-text",
                                    "url": "http://localhost:11434/api/embeddings"
                            }
                    }
            )
