import streamlit as st

from app.chatbot import SmartLibrarian

chatbot = SmartLibrarian()

st.set_page_config(
    page_title="Smart Librarian",
    page_icon="📚",
)

st.title("📚 Smart Librarian")

query = st.text_input(
    "What kind of book are you looking for?"
)

if st.button("Recommend"):

    if query.strip():

        with st.spinner("Searching for the perfect book..."):

            response = chatbot.chat(query)

        st.success("Recommendation")

        st.write(response)