import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

embedding_model = OpenAIEmbeddings(api_key=openai_key)
vectorstore = FAISS.load_local("faiss_news_index", embedding_model, allow_dangerous_deserialization=True)

retriever = vectorstore.as_retriever()
llm = OpenAI(openai_api_key=openai_key, temperature=0)

qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

while True:
    query = input("\n Ask a question (or type 'exit'): ")
    if query.lower() == "exit":
        break
    answer = qa_chain.invoke(query)['result']
    print(f"Answer: {answer}")
