import streamlit as st
from datetime import datetime
import csv
import pandas as pd

st.set_page_config(page_title="Write diary", page_icon="📝")
def main():
    # Markdown을 사용하여 텍스트 가운데로 배치
    st.markdown("<h1 style='text-align: center;'> 📱 Write diary 📱</h1>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()
st.sidebar.header("Write diary")



def feelingslider():
    with st.form("write"):
        st.subheader("Feeling Slider")

        # 기분 슬라이더
        st.write("- **너의 기분(상태)를 퍼센트로 표현해봐!**")
        feeling = st.slider(
            '',
            0, 100)
        if feeling:
            st.write("**오늘의 내 기분 퍼센트는** ", feeling, '**% !**')

            if feeling <=25:
                st.write("""오늘 힘들었군요 고생 많았어요! """)

            elif feeling > 25 and feeling <=75:
                st.write("**그럭저럭이었던 하루! 오늘 푹 자고 내일 더 힘내봅시다!**")

            else:
                st.write("**오늘 알차게 보냈군요! 수고했어요 내일도 힘내봅시다!**")
     
        submitted = st.form_submit_button("Submit", use_container_width=True)
        if submitted:
            st.caption("**Feeling slider 저장 완료!**")
        

def Writedatediary():
    
    with st.form('form'):
        st.subheader("Change date")
        now_time = datetime.now()
        formatted = now_time.strftime("%Y-%m-%d")
        st.write(" **Today Date :** ",formatted)
        selected_date = st.date_input("기록하려는 날짜 변경")
        submitted = st.form_submit_button("Change", use_container_width=True)
        if submitted:
            st.write(selected_date,"일 기준으로 작성")
        #     return selected_date
        # return formatted
    
    types = st.multiselect(
    label="**오늘 기분 어때?**",
    options=['😄','😍','😌','😕','😖','😭','😪','😶'],
    max_selections=3,
    )
            
    diary = st.text_input(label="**오늘의 일기를 작성해봐! :** ")
    
    if diary:
        st.write(diary)
        st.sidebar.header("Today's Diary saved")
        st.write('**오늘의 일기 저장 완료!👍**')
    # 내용 저장 
    # 만약 오늘 날짜로 저장한다면 -> 날짜 변경을 안 한다면 오늘 날짜로 딕셔너리에 내용과 함께 저장
    # 사용자가 선택한 날짜 가져오기
        diary_dict = {}
        if selected_date == datetime.now().strftime("%Y-%m-%d"):
            # 오늘 날짜를 선택한 경우
            diary_dict = load_diary()
            diary_dict[selected_date] = diary
            save_diary(diary_dict)
        else:
            # 오늘 날짜를 선택하지 않은 경우
            diary_dict = load_diary()
            diary_dict[selected_date] = diary
            save_diary(diary_dict)

            
def load_diary():
    try:
        with open("diary.csv", "r", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            diary_dict = {row[0]: row[1] for row in reader}
    except FileNotFoundError:
        diary_dict = {}
    return diary_dict

def save_diary(diary_dict):
    with open("diary.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for key, value in diary_dict.items():
            writer.writerow([key, value])



# # 일기 불러오기
# def search_diary(diary_dict):
#     with st.form("p"):
#         st.subheader("Load diary")
#         search_diary =st.date_input("기록하려는 날짜 변경")
#         if search_diary:
#             with open("diary.csv","r",newline='', encoding='utf-8') as f:
#                 reader = csv.DictReader(f)
#                 if diary_dict[]
                



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # 기분 그래프


feelingslider()
Writedatediary()