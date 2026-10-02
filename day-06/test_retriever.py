
from retriever import load_documents as load_knowledgebase, retrive

# documents = load_knowledgebase()

# for fileName, document in documents.items():
#     print(f"file name: {fileName}")
#     print(f"file Content: {document}")
#     print(f"="*40)

"""  Test retiever base don keyword """
print(retrive("artificial"))
print(retrive("AI"))
print(retrive("SQL"))
print(retrive("Python"))



