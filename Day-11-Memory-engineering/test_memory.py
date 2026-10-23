from memory import create_database, save_memory, search_semantic_memories

def main():

    create_database()

    # save_memory("My name is Akash", "welcome akash, Please enjoy tyour day!")
    # save_memory("I live in indore", "wonderfull! Indore is great place witt visit having multiple tourist place.")
    # save_memory("What is python", "Python is an prograaming languge nowdays used for muiplt AI works.")
    # save_memory("What is Java", "Java is an prograaming languge nowdays used for muiplt AI works.")

    result = search_semantic_memories("what is my coding?")
    
    print("Result (Relevant memories):")
    for row in result:
        print("Row: ", row)

if __name__ == "__main__":
    main()