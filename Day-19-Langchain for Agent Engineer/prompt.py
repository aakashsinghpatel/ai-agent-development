from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate(messages=[
                ("system", "You are an AI agent teacher"),
                ("human","{question}")
                ])