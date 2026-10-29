
from retriever import retriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import sys
sys.path.append("..")  
from model import model

def get_context(question):
    documents = retriever.invoke(question)

    return "\n\n".join(
        document.page_content
        for document in documents
    )


def main():
    print("==== RAG With langchain====")
    user_query = input("Please write your query:: ")
    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using only the provided context.

        Context:
        {context}

        Question:
        {question}
        """
        )
    # Langcahin (LCEL): chianing the pipeline
    # {"context": get_context,"question": lambda x: x} :: paraller call: pass the input to bot
    # getconetc and lambda as
    # as LCEL need function mae as input rest passing param it handles
    chain = ({"context": get_context,"question": lambda x: x}| prompt | model | StrOutputParser())
    answer = chain.invoke(user_query)

    print(answer)
if __name__ == "__main__":
    main()