import os
import subprocess
from loader import load_document
from splitter import split_documents
from vectorstore import create_vectorstore

PDF_FILE = "agriculture-11-00707.pdf"
DB_DIR = "chroma_db"

def ingest_documents():
    """Ingest documents into ChromaDB"""
    print("📥 Loading PDF...")
    docs = load_document(PDF_FILE)

    print("✂️ Splitting documents...")
    chunks = split_documents(docs)

    print("🧠 Creating vectorstore...")
    create_vectorstore(chunks)
    print("✅ Ingestion complete! Data stored in ChromaDB.\n")

def run_smart_query():
    """Smart search mode using query_constructor.py"""
    
    print("🚀 Launching interactive query system...\n")
    subprocess.run(["python3", "query_constructor.py"])

if __name__ == "__main__":
    print("=== 📚 ChromaDB Project ===")

    # Check if ChromaDB already exists
    if not os.path.exists(DB_DIR) or not os.listdir(DB_DIR):
        print("🛠️ Vector DB not found. Starting ingestion first...")
        ingest_documents()
    else:
        print("🟢 Existing ChromaDB found. Skipping ingestion.\n")

    # After ingestion (or if DB already existed), directly launch query mode
    run_smart_query()
