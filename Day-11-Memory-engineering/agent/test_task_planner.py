from task_planner import decompose_task

def main():
    user_input = input(" You: ")
    """ Break Big task (user request) into smaller task """
    task_list = decompose_task(user_input)
    print("List of task: From Task decomposer")
    for task in task_list:
        print("",task)

if __name__ == "__main__":
    main()