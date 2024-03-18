import streamlit as st
import streamlit_option_menu

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.write("# Welcome to Diary App! 👋")

st.sidebar.success("Select a demo above.")


st.markdown(
    """
  This diary app has three functions.
   - Write a diary: \n
   Let's record what happened in the day and end the day in a good mood!

   - Chatbot: \n
   Tell me about your frustrating concerns that you can't tell anyone easily. I have a chatbot on your side!

   - To-do : \n
   Let's organize what we have to do today and write it down! Plan your day!
"""
)