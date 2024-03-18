import streamlit as st
from datetime import date
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Write To-do", page_icon="📌")
def main():
    # Markdown을 사용하여 텍스트 가운데로 배치
    st.markdown("<h1 style='text-align: center;'> 📆 To-Do 📆 </h1>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()
st.sidebar.header("Write To-do")

now_time = datetime.now()
formatted = now_time.strftime("%Y-%m-%d")
st.write(" **Today date :** ",formatted)

task = st.text_input("오늘 해야 할 것들을 적어보세요!", " ")

if st.button("Add To-do list"):
    if task:
        st.session_state["task_list"].append(task)

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

# for i,t in enumerate(st.session_state["task_list"]):
    # st.write(f"{i+1}. {t}")

for i, t in enumerate(st.session_state["task_list"]):
    if st.checkbox(f"{i+1}. {t}"):
        st.session_state["task_list"].remove(t)
