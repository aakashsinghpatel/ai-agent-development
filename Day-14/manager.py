from research_agent import research
from coding_agent import write_code
from review_agent import review_code


def run_manager(task):

    print("\nManager → Research Agent")

    research_result = research(
        task
    )

    print("\nManager → Coding Agent")

    code_result = write_code(
        task,
        research_result
    )

    print("\nManager → Reviewer Agent")

    review_result = review_code(
        task,
        code_result
    )

    return {
        "research": research_result,
        "code": code_result,
        "review": review_result
    }
