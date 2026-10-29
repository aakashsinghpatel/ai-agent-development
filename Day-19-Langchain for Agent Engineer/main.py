from model import model

def main():
    user_query = input("What is your query::")
    response = model.invoke(user_query)
    
    print("==="*50)
    print("Response is:", response)
    print("==="*50)
    print("Response content is:", response.content)


if __name__ == "__main__":
    main()