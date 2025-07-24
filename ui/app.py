import os
import streamlit as st
from dotenv import load_dotenv
from router.gent_router import AgentRouter

# Load environment variables from .env
load_dotenv()

st.set_page_config(page_title="Azure Cloud Assistant 🤖", layout="wide")
st.title("Azure Cloud Assistant — Identity, Access & Insights")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Render chat history
for entry in st.session_state.chat_history:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])

# Input box for user query
user_input = st.chat_input("Ask me about permissions, app insights, anomalies...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    agentRouter = AgentRouter()
    response = agentRouter.route(user_input)

    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.experimental_rerun()
