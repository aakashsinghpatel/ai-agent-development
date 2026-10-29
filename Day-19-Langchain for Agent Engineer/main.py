from model import model
from prompt import prompt
from agent import call_autonomous_agent
def main():
    user_query = input("What is your query::")

    # msg = prompt.invoke({"question":user_query})
    # print("Prompt msg is:")
    # print(msg)
    # print("="*50)
    # response = model.invoke(msg)
    # print("="*50)
    # print("Response is:", response)
    # print("="*50)
    # print("Response content is:", response.content)

    """ No nee to handle tool executiona and loop """
    response = call_autonomous_agent({
            "messages": [
                {
                    "role": "user",
                    "content": user_query
                }
            ]
        })

    print("="*50)
    print("Agent whole response")
    print(response)
    print("="*50)
    print("Agent expected response")

    # print(response)

if __name__ == "__main__":
    main()