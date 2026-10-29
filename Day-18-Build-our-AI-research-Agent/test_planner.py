from agent import research_planner


request = (
    "Research about the jobs requirement in AI 	agent domain."
)


plan = research_planner(
    request
)


print("\nRESEARCH PLAN\n")
print(plan)

