import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

# Page config
st.set_page_config(page_title="💬 Vertex AI Tec Chatbot", layout="wide")

# Custom CSS for floating sidebar chat widget
st.markdown(
    """
    <style>
    /* Hide default Streamlit header and footer */
    header, footer {visibility: hidden;}

    /* Chat widget container */
    .chat-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 350px;
        max-height: 500px;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.25);
        background: white;
        display: flex;
        flex-direction: column;
        z-index: 9999;
    }

    /* Chat header */
    .chat-header {
        background: #4A90E2;
        color: white;
        padding: 10px;
        font-weight: bold;
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
        text-align: center;
    }

    /* Chat body */
    .chat-body {
        padding: 10px;
        flex-grow: 1;
        overflow-y: auto;
    }

    /* Chat input */
    .stChatInputContainer {
        margin: 0 !important;
        padding: 8px;
        border-top: 1px solid #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create chatbot UI
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.markdown('<div class="chat-header">💬 Vertex AI Tec Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="chat-body">', unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! I’m your Vertex AI Tec assistant. How can I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

st.markdown("</div>", unsafe_allow_html=True)  # Close chat body

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        response_box = st.empty()
        collected = ""

        with requests.post(API_URL, json={"role": "user", "content": prompt}, stream=True) as r:
            for chunk in r.iter_content(chunk_size=None):
                if chunk:
                    text = chunk.decode("utf-8")
                    collected += text
                    response_box.markdown(collected)

        st.session_state.messages.append({"role": "assistant", "content": collected})

st.markdown("</div>", unsafe_allow_html=True)  # Close chat container
