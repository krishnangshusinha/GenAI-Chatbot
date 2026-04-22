from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

#loading the env variables
load_dotenv()

#streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 Generative AI Chatbot")

#inititate chat history (intitializing it in session storage so that our chat histroy is not lost if application is rendered, so the chat_history is intitialised for the first time when application is started)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


#show history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#llm initiate
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.0,
)

#input box
user_prompt = st.chat_input("Ask Chatbot...")       # add that input box

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user", "content": user_prompt})

    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assitant"}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content":  assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)