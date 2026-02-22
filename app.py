import streamlit as st
from backend.llm_client import LLMClient


# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Career Advisor Chatbot")
st.write("Get personalized career advice powered by Groq AI.")


# ---------------------------
# Initialize Gemini Client
# ---------------------------
if "client" not in st.session_state:
    st.session_state.client = LLMClient()


# ---------------------------
# Initialize Chat Memory
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------
# Display Chat History
# ---------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------------------
# Chat Input
# ---------------------------
if user_input := st.chat_input("Ask me about your career..."):

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Build structured conversation history
    formatted_history = []

    for msg in st.session_state.messages:
        formatted_history.append({
            "role": msg["role"],
            "parts": [msg["content"]]
        })

    # Generate AI response
    try:
        with st.spinner("Thinking..."):
            response = st.session_state.client.generate_response(formatted_history)

        # Store assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.markdown(response)

    except Exception as e:
        st.error(f"Error: {str(e)}")