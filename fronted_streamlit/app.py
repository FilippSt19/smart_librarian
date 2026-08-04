import streamlit as st

from app.engine.agents.smart_librarian import (
    SmartLibrarianAgent,
)


st.set_page_config(
    page_title="Smart Librarian",
    page_icon="📚",
    layout="centered",
)

@st.cache_resource
def get_chatbot():

    return SmartLibrarianAgent()

chatbot = get_chatbot()

st.title("📚 Smart Librarian")

st.caption(
    "Discover your next favorite book using AI, RAG and OpenAI."
)

with st.sidebar:

    st.header("📖 Example Questions")

    st.markdown(
        """
- I want a fantasy book about friendship.
- Recommend a romance novel.
- Suggest a dystopian book.
- I love war stories.
- Recommend a science fiction novel.
"""
    )

    if st.button("🗑 Clear Conversation"):

        st.session_state.messages = []

if "messages" not in st.session_state:

    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

prompt = st.chat_input(
    "What kind of book are you looking for?"
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching for the perfect book..."
        ):

            try:

                response = chatbot.chat(prompt)

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                    }
                )

            except Exception as exc:

                st.error(
                    f"Unexpected error:\n\n{exc}"
                )