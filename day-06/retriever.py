
from pathlib import Path


def load_documents():
    """ Method to load all document of knowledge base """
    documents = {}
    # To get respective path folder
    folder = Path('knowledge')
    # glob() : iterator of all matching file
    for file in folder.glob('*.txt'):
        documents[file.name] = file.read_text(encoding='utf-8')
    return documents


def retrive(keyword):
    """ Retrieve the file name and content based on keyword matching.
     The first match """
    documents = load_documents()
    for filename, content in documents.items():
        if keyword in content:
            return filename, content
    return None, None