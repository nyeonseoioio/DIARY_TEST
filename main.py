import openai
from dotenv import load_dotenv
from openai import OpenAI
import os


# # .env 파일에서 환경 변수를 로드합니다.
# load_dotenv()




    #---------------------------------------------------------------------------------------------

    # import streamlit as st
# import datetime


# option = st.selectbox(
#     'D-day앱',
#     ('D-day Count', 'Week Count', 'Day Count'))

# st.write(f'{option}를 선택하셨습니다.', )

# if option == 'D-day Count':
#     day("")


# 다이어리 개발

# 버튼 1 : 일기 작성
# 버튼 2 : chatBot

# 심리상담 chatBot 
# 심리상담 데이터 가지고 와서 이를 기반으로 chatBot 구현

# 심리상담 결과 알려주기
# 너무 힘들어보이는 상황이면 자살 예방 방지 동영상이나 캠폐인 동영상 보여주기


# 버튼 3 : To-do 리스트 작성

# 오늘의 운세 작성
# 오늘의 일기 작성할 수 있도록 하기
#  + 오늘의 일기에 장소 기록할 수 있도록 하기

import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu



# title 가운데에 배치 
def main():
    # Markdown을 사용하여 텍스트 가운데로 배치
    st.markdown("<h1 style='text-align: center;'>💬Diary💬</h1>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()


# def write_diary():
#     with st.form("write"):
#         st.title("Feeling Slider")

#         # 기분 슬라이더
#         st.write("- **오늘 너의 기분(상태)를 퍼센트로 표현해봐!**")
#         feeling = st.slider('', 0, 100, 25)
#         st.write("**오늘의 내 기분 퍼센트는** ", feeling, '**% !**')


#         # 만약 0-25 면 오늘 힘들었군요 고생많았다는 문구
#         # 25-50면 
#         # 50-75면
#         # 75-100면 오늘 기분 좋은 하루를 

#         #그래프 사용

#         st.subheader('', divider='gray')

#         # now_time = datetime.now()
#         # formatted = now_time.strftime("%Y-%m-%d")
#         # st.write("**Today Date:** ",formatted)
    
#         # if st.button(label ="**날짜 변경**"):
#         new_Date = st.date_input(label='**날짜 변경을 원하시면 날짜 변경하세요**', format="YYYY/MM/DD")
#         st.write(new_Date,"**일엔 어떤 하루였어?**")
#             # change_day = st.data_input("변경할 날짜를 고르세요!")
#             # st.write(change_day)

#         types = st.multiselect(
#         label="**오늘 기분 어때?**",
#         options=['😄','😍','😌','😕','😖','😭','😪','😶'],
#         max_selections=3,
#             )
        
#         diary = st.text_input(label="**오늘의 일기를 작성해봐! :** ")
    
#         submitted = st.form_submit_button("Submit")

#         if submitted:
#             st.write(diary)
#             st.write("오늘의 일기 저장 완료!")
#         st.stop()

# def use_chat_bot():
#     import streamlit as st
#     from streamlit_chat import message
#     import pandas as pd
#     from sentence_transformers import SentenceTransformer #sentenceBERT 모델 사용
#     from sklearn.metrics.pairwise import cosine_similarity
#     import json
#     import joblib


#         # model = joblib.load('data/AI_chatbot.pkl')
#     df = pd.read_csv('data/wellness_dataset.csv')
#     df['embedding'] = df['embedding'].apply(json.loads)

#     # allow_output_mutation=True
#     @st.cache_data()
#     def cached_model():
#     # model = joblib.load('data/AI_chatbot.pkl')
#         model = SentenceTransformer('jhgan/ko-sroberta-multitask')
#         return model

#     @st.cache_resource()
#     def get_dataset():
#         df = pd.read_csv('data/wellness_dataset.csv')
#         df['embedding'] = df['embedding'].apply(json.loads)
#         return df

#     model = cached_model()
#     df = get_dataset()

#     st.header('Chat Bot')

#     if 'generated' not in st.session_state:
#         st.session_state['generated'] = []

#     if 'past' not in st.session_state:
#         st.session_state['past'] = []

#     # 텍스트를 입력하여 봇과 대화 할 수 있는 폼 생성
#     # clear_on_submit 옵션을 통해서 submit 하면 폼의 내용이 지워짐
#     with st.form('form', clear_on_submit=True):
#         user_input = st.text_input('You : ', '')
#         submitted = st.form_submit_button('전송')

#         # 메시지를 입력 후 전송을 누를 경우
#     if submitted and user_input:
#         embedding = model.encode(user_input) # 유저가 입력한 문장을 벡터라이징
#         # 입력한 메시지의 유사도를 확인하여 가장 유사한 답변을 제시
#         df['similarity'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
#         answer = df.loc[ df['similarity'].idxmax() ] # 가장 유사한 답변을 저장

#         # 유저와 챗봇의 대화 내용을 저장
#         st.session_state.past.append(user_input)
#         st.session_state.generated.append(answer['챗봇'])

#         # 저장된 대화 내용 보여주기
#         for i in range(len(st.session_state['past'])):
#             message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
#             if len(st.session_state['generated']) > i:
#                 message(st.session_state['generated'][i], key=str(i) + '_bot')

        # submitted_chat = st.form_submit_button("Submit")

        # if submitted_chat:
        #     st.write(" 챗봇 종료! ")

# st.button("Reset", type="primary", use_container_width=True)
# if st.button('Write Diary', use_container_width =True):
#     write_diary()

            

# elif st.button ('To-do', use_container_width =True):
#     st.write()

# elif st.button('Chat Bot',type="primary", use_container_width=True):
#     use_chat_bot()


# with st.sidebar:
#     choose = option_menu("App Gallery", ["Write Diary", "To-do", "today's horoscope","Chat Bot"],
#                          icons=['bi bi-pencil', 'bi bi-calendar-check-fill', 'bi bi-arrow-through-heart','bi bi-chat-heart-fill'],
#                          menu_icon="app-indicator", default_index=0,
#                          styles={
#         "container": {"padding": "5!important", "background-color": "#fafafa"},
#         "icon": {"color": "black", "font-size": "20px"}, 
#         "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "#EAAEE0"},
#     }
#     )








# write Dairy 눌렀을 때 사용하는 함수
    



























