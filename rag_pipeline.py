# Import Python Libraries
import os
import pymongo
from dotenv import load_dotenv

# Load .env so that OPENAI_API_KEY is available
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# COnneect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["askthenews_db"]
collection = db["bbc_news"]

# Fetch and format all news entries
docs = []
for doc in collection.find():
    title = doc.get("title", "")
    pubDate = doc.get("pubDate", "")
    text = f"{title} ({pubDate})"
    docs.append(text)

print(f"✅ Loaded {len(docs)} documents from MongoDB")

# Import LangChain + FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

# Initialize the embedding model
embedding_model = OpenAIEmbeddings(openai_api_key=openai_key)

# Wrap docs in Langchain Document objects
documents = [Document(page_content=doc) for doc in docs]

# Split long documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=20)
split_docs = text_splitter.split_documents(documents)

# Create the FAISS vector store
vectorstore = FAISS.from_documents(split_docs, embedding_model)
vectorstore.save_local("faiss_news_index")
print("✅ FAISS vector store created and saved!")
