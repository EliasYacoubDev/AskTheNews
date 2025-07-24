# AskTheNews – RAG-powered News Q&A Chatbot

**AskTheNews** is an intelligent Retrieval-Augmented Generation (RAG) system that:
- Scrapes latest BBC news using Scrapy
- Stores headlines in MongoDB
- Embeds them with OpenAI embeddings
- Indexes with FAISS vector store
- Answers user questions with a RetrievalQA chain

---

## Features

- 🔍 Web scraping with Scrapy (BBC)
- 🧠 Semantic search with FAISS + OpenAI
- 💬 Natural question answering with GPT-4o
- 🧾 MongoDB for document storage
- 🧪 Local streaming for fast response

---

## Project Structure

AskTheNews/
│
├── news_scraper/ # Scrapy project
│ ├── spiders/
│ └── pipelines.py
│
├── faiss_news_index/ # FAISS vector store (gitignored)
│
├── rag_pipeline.py # Embeds docs from MongoDB
├── rag_chat.py # Streamed QA interaction
├── .env # API keys (gitignored)
└── requirements.txt

---

## ⚙️ Setup Instructions

### 1. Clone the repo
git clone https://github.com/EliasYacoubDev/AskTheNews.git
cd AskTheNews

### 2. Create and activate virtual env
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add .env file
OPENAI_API_KEY=your_openai_key
MONGO_URI=mongodb://localhost:27017

## Run Pipeline
### Scrape BBC News
scrapy crawl bbc
## Embed to FAISS
python rag_pipeline.py
## Ask Questions
python rag_chat.py
