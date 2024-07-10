import os
import json
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleVectorStore
from scrapping.scr_advaita import scrape_advaita
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

advaita_data = scrape_advaita()

def get_conversational_chain():
    prompt_template = """
    You are Astrix, a lost astronaut in the stellar galaxy; Advaita is the grandest fest of the stellar galaxy; your job is to effectively solve the queries and provide support and welcome them. You can use the data stored in the advaita context.
    Context:\n {context}?\n
    User: {query} \n
    Astronaut Guide Astrix: {answer} :
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "query"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

st.title("Advaita Chatbot - Astrix")
st.subheader("Greetings, traveler! Astrix at your service. Lost in Advaita I may be, but I haven't lost my way around the grandest fest in the stellar galaxy!.")

user_input = st.text_input("Wonders can I help you discover? ✨🚀:")

if user_input:
    chain = get_conversational_chain()

    # Check if advaita_data is not None before using it
    if advaita_data is not None:
        # Convert advaita_data to a single context string
        context = "\n".join([f"{page['key'].capitalize()}:\n{page['page_content']}" for page in advaita_data])
        response = chain.invoke({"context": context, "query": user_input, "answer": ""})
        st.write("Reply:", response.get('answer', "No response available yet."))
    else:
        st.write("An error occurred while scraping data. Please try again later.")

# Add buttons for opening URLs
if st.button("Register for Hackfest"):
    st.write("Opening Hackfest Registration...")
    st.markdown("[Register for Hackfest](https://unstop.com/hackathons/inter-college-hackathon-advaita-tecno-cultural-fest-international-institute-of-information-technology-iiit-bh-857179)", unsafe_allow_html=True)

if st.button("Register for Swig N Code"):
    st.write("Opening Swig N Code Registration...")
    st.markdown("[Register for Swig N Code](https://www.naukri.com/code360/events/swig-n-code?utm_source=campus-ambassador&utm_medium=ET&utm_campaign=CNIIIT)", unsafe_allow_html=True)

if st.button("View Swig N Code Rulebook"):
    st.write("Opening Swig N Code Rulebook...")
    st.markdown("[View Swig N Code Rulebook](https://drive.google.com/file/d/17MkHtHFtHwH929csu8vja2MYxgdWU1fV/view)", unsafe_allow_html=True)

if st.button("Register for Dirt Rush"):
    st.write("Opening Dirt Rush Registration...")
    st.markdown("[Register for Dirt Rush](https://unstop.com/competitions/dirt-rush-advaita-tecno-cultural-fest-of-iiit-bhubaneswar-international-institute-of-information-technology-857200)", unsafe_allow_html=True)

if st.button("Register for Line Follower"):
    st.write("Opening Line Follower Registration...")
    st.markdown("[Register for Line Follower](https://unstop.com/competitions/line-follower-advaita-tecno-cultural-fest-international-institute-of-information-technology-iiit-bhubaneswa-857177)", unsafe_allow_html=True)

if st.button("Register for Robo Soccer"):
    st.write("Opening Robo Soccer Registration...")
    st.markdown("[Register for Robo Soccer](https://unstop.com/events/robo-soccer-advaita-tecno-cultural-fest-international-institute-of-information-technology-iiit-bhubaneswar-857211)", unsafe_allow_html=True)

if st.button("Register for Cybersec Battle"):
    st.write("Opening Cybersec Battle Registration...")
    st.markdown("[Register for Cybersec Battle](https://unstop.com/hackathons/cybersec-battle-international-institute-of-information-technology-iiit-bhubaneswar-890695?lb=02mBqKH)", unsafe_allow_html=True)

if st.button("Register for Switch Coding"):
    st.write("Opening Switch Coding Registration...")
    st.markdown("[Register for Switch Coding](https://www.naukri.com/code360/events/switch-coding?utm_source=campus-ambassador&utm_medium=ET&utm_campaign=CNIIIT)", unsafe_allow_html=True)

if st.button("View Merchandise"):
    st.write("Opening Merchandise Page...")
    st.markdown("[View Merchandise](https://www.advaita-iiitbh.in/merch)", unsafe_allow_html=True)

if st.button("View Pronights"):
    st.write("Opening Pronights Page...")
    st.markdown("[View Pronights](https://www.advaita-iiitbh.in/#pronights)", unsafe_allow_html=True)
