# loader.py
from langchain_community.document_loaders import PyPDFLoader
def load_document(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs