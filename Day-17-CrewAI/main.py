from crew import crew, memmory_crew


def main():

    # similar to graph.invoke()
    result = crew.kickoff()
    memory_crew_result = memmory_crew.kickoff()

    print("\n")
    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    print(result)
    print("=" * 60)
    print("FINAL RESULT: Memory Crew")
    print("=" * 60)
    print(memory_crew_result)


if __name__ == "__main__":
    main()


