# app.py
import streamlit as st
from chatbot import get_bot_response

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Ask me anything...", key="user_input")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    # Append user input
    st.session_state.chat_history.append(("You", user_input))

    # Get bot response
    bot_reply = get_bot_response(user_input)
    st.session_state.chat_history.append(("Bot", bot_reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
