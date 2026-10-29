from model import model
from prompt import prompt

from langchain_core.output_parsers import StrOutputParser

def main():
    user_query = input("What is your query::")

    """ with this we do not need to invoke prompt and model specifically
    pipe operator pass input of first to second and so again """
    # chain  = prompt | model 
    """  we can also diectly parse the output of model in stronly rather res.content """
    parser = StrOutputParser()

    """  Chaining with pipe operator to remove manuall calling """
    chain = prompt | model |parser

    res = chain.invoke({"question": user_query})

    print(res)

if __name__ == "__main__":
    main()