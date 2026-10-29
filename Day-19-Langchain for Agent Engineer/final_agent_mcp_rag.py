

from model import model
from RAG.retriever import retriever
from langchain.agents import create_agent
from langchain_mcp_client_adpter import get_mcp_tools
import asyncio
from langchain.tools import tool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

""" creating mcp rag retriver tool """

@tool
def search_knowledeg(user_query):
    """ Search the local knowledge base return the relevent information"""
    documents = retriever.invoke(user_query)
    return "\n\n".join(
            document.page_content
            for document in documents
        )


async def main():

    mcp_tools = await get_mcp_tools()
    agent = create_agent(model=model, tools=mcp_tools+[search_knowledeg])

    query = input("Please enter your query:: ")
    prompt = ChatPromptTemplate(messages=[("human", "{query}")]).invoke({"query": query})
    chain = agent

    res = await chain.ainvoke(prompt)
    print("Result of agent::")
    print(res)
    print("final result:")
    print(res["messages"][-1].content)

    print("="*50)
    print("Debug Agent flow")
    for msg in res["messages"]:
        print(msg)
        print("\n")

if __name__ =="__main__":
    asyncio.run(main())
