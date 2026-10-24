

""" This is part of security: Input validation """
def validate_input(input):
    if len(str(input)) <=0 :
        raise ValueError("Input is empty")
    elif len(str(input)) > 500:
        raise ValueError("Input is too lengthy")


def validate_task(task):
    if not task:
        raise ValueError("Task cannot be empty.")
    task = task.strip()
    if len(task) > 5000:
        raise ValueError("Task is too long.")
    return task
