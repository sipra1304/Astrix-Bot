import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import JSONLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate

# LangChain setup
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load scraped data
loader = JSONLoader(file_path="scraped_data.json", jq_schema=".[].page_content", text_content=False)
advaita_data = loader.load()

pprint(advaita_data)

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(advaita_data)

# Create a vector store
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# Retrieve and generate using the relevant snippets of the blogs.
retriever = vectorstore.as_retriever()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

template = """Forget that you are an AI. You are Astrix, a lost astronaut in the stellar galaxy; Advaita is the grandest fest of the stellar galaxy; your job is to effectively solve the queries and provide support and welcome them. You can use the data stored in the advaita context.

Always say "See you at the Fest!" at the end of the answer.

{context}

Question: {question}

Helpful Answer:"""

custom_rag_prompt = PromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | custom_rag_prompt
    | llm
    | StrOutputParser()
)

# Invoke the chain with a question
response = rag_chain.invoke("What is Advaita?")
print(response)