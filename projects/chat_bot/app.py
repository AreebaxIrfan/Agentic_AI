import streamlit as st
import google.generativeai as genai
import os

# Set up Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Fetch API key from environment variable
if not GEMINI_API_KEY:
    st.error("Please set the GEMINI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

# Initialize session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title of the app
st.title("Chat with the Assistant")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input for user prompt
chat_input = st.chat_input("Enter your prompt")

if chat_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": chat_input})

    # Display user message
    with st.chat_message("user"):
        st.write(chat_input)

    # Generate assistant response using Gemini API
    try:
        response = model.generate_content(chat_input)
        assistant_response = response.text
    except Exception as e:
        assistant_response = f"Sorry, I encountered an error: {str(e)}"

    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(assistant_response)