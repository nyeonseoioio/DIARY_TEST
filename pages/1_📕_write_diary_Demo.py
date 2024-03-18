import streamlit as st
from datetime import datetime

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
        st.write("- **오늘 너의 기분(상태)를 퍼센트로 표현해봐!**")
        feeling = st.slider(
            '',
            0.0, 100.0)
        if feeling:
            st.write("**오늘의 내 기분 퍼센트는** ", feeling, '**% !**')


        # 만약 0-25 면 오늘 힘들었군요 고생많았다는 문구
        # 25-50면 
        # 50-75면
        # 75-100면 오늘 기분 좋은 하루를 

        #그래프 사용
        submitted = st.form_submit_button("저장")

        if submitted:
            st.write("Feeling slider 저장!")
        st.stop()

def Writedatediary():
        now_time = datetime.now()
        formatted = now_time.strftime("%Y-%m-%d")
        st.write(" **Today Date :** ",formatted)

        

        # 날짜 변경도 하고 싶지만.. 실패
        # buttom =st.button(label ="**날짜 변경**")
        # if buttom:
        #     new_Date = st.date_input(label='**날짜 변경하세요**', format="YYYY-MM-DD")
        #     if new_Date:
        # st.write(new_Date,"**일엔 어떤 하루였어?**")


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
        # st.stop()

# feelingslider()
Writedatediary()