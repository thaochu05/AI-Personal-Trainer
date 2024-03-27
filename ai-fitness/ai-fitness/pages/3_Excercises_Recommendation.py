import av
import os
import sys
import streamlit as st
import cv2
import tempfile
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.tools.retriever import create_retriever_tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import datetime
from Homepage import set_sidebar_visibility  
BASE_DIR = os.path.abspath(os.path.join(__file__, '../../'))
sys.path.append(BASE_DIR)


st.title("Weekly Excercises Recommendation")
# Create a placeholder for the chat messages
chat_container = st.empty()


# Define your chatbot model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0,openai_api_key='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')
output_parser = StrOutputParser()
# Text input for entering messages

user_height = st.text_input("Enter your height:", "", key = "height")
user_weight = st.text_input("Enter your weight:", "", key = "weight")
push_up = st.text_input("How many push ups can you do in a row:", "", key = "push_up")
user_days = st.text_input("How many days a week do you want to go to the gym: (from 1 to 7)", "", key = "days")
goal = st.radio("Select your fitness goal:", ["Lose weight", "Bulk up", "Cut"], key = "goal")
experience = st.radio("Select your fitness experience:", ["Beginner", "Intermediate", "Advanced"], key = "experience")
current_date = datetime.datetime.now().date()

def change_format(response):
    prompt = ChatPromptTemplate.from_template("""Currently, I am having this weekly plan for my workout: {plan}. I want you to transform it into 
                                            this format: a list of dictionaries where each dictionaries includes: 
                                                "title": "Excercise name - Set x Reps x Weight",
                                                    "color": "Color hexa code" # Different pastel color for different focus of the excercise, same color for same focus
                                                    "start": "" #which is which day excercise start,
                                                    "end": "" # same day as start,
                                                    "resourceId": "a" # a to f, randomize it for each excercise
                                                    """)
    chain = prompt | llm | output_parser
    return chain.invoke({"plan":response})
    # Function to interact with the chatbot
def chat_with_bot(user_height,user_weight,user_days,goal):
    prompt = ChatPromptTemplate.from_template("""My weight is {kg} kg, my height is {cm} cm, I want to go to the gym {days} days a week,
                                                and I want my gym days to spread through out the week, and my goal is to {goal}. My experience with the gym is {experience}, 
                                                and currently I can only do {pushup} in a row. Can you plan me a weekly workout routine, with detailed excercises (How many rep and set)
                                                and recommended weight, and I want it to be in calendar view?. Starting from today, which is {date}, and I want to have format like this:
                                              Monday - (main focus of excercises) - year/month/date: 
                                              -list of excercises in the day """)
    chain = prompt | llm | output_parser
    return chain.invoke({ "kg": user_weight, "cm": user_height, "days": user_days, "goal": goal, "experience": experience, "pushup": push_up, "date": current_date})
input_placeholder = st.empty()
# Button to send the message
if st.button("Submit"):
    bot_respond = chat_with_bot(user_height,user_weight,user_days,goal)
    saved_response = change_format(bot_respond)

    st.write(bot_respond)
    st.session_state['transferred_variable'] = saved_response
    
    

        



