from model import model
from prompt import prompt

def main():
    user_query = input("What is your query::")

    msg = prompt.invoke({"question":user_query})
    print("Prompt msg is:")
    print(msg)
    print("="*50)
    response = model.invoke(msg)
    print("="*50)
    print("Response is:", response)
    print("="*50)
    print("Response content is:", response.content)


if __name__ == "__main__":
    main()