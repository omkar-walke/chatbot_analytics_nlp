from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Set up API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyBm4shP3cpJD67BSQhTlIzViZ4Q2CCI3eQ"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Create a chat session with the model
def get_gemini_response(question):
    # Create the chat session object (initialize ChatSession correctly)
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    chat = model.start_chat(history=[])
    
    # Send the question to the chat model and return the response
    response = chat.send_message(question)
    
    # Adjusted to access response text properly
    return response.text  # Assuming the response object has a 'text' attribute

# Streamlit setup
st.set_page_config(page_title="CHATBOT-DEMO")
st.header("GEMINI LLM APPLICATION")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

input_text = st.text_input("Input:", key="input")
submit = st.button("ASK THE QUESTION")

if submit and input_text:
    response_text = get_gemini_response(input_text)
    st.session_state["chat_history"].append(("YOU", input_text))
    st.session_state["chat_history"].append(("BOT", response_text))

st.subheader("The response is")
if st.session_state["chat_history"]:
    for role, text in st.session_state["chat_history"]:
        st.write(f"{role}: {text}")
