import streamlit as st
import os

st.set_page_config(page_title="예비 초등 따라쓰기 영상 모아보기", layout="wide")
st.title("🎬 따라쓰기 영상 피드백")

# 클라우드 영상 URL 리스트
videos = [
    "https://felcms.allviacms.com/fileRoot/question/temp/a_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/b_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/c_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/d_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/d1_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/e_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/f_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/g_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/h_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/i_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/j_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/J1_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/k_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/L_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/m_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/n_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/o_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/p_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/q_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/r_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/s_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/t_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/t1_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/u_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/v_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/w_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/x_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/y_FN.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/z_FN.mp4"

]

# st.session_state에 'feedbacks' 리스트가 없으면 초기화
if 'feedbacks' not in st.session_state:
    st.session_state.feedbacks = []

# 피드백을 저장하고 화면에 표시하는 함수
def save_feedback(video_url, feedback_text):
    # 피드백이 빈 문자열이 아닐 경우에만 저장
    if feedback_text:
        st.session_state.feedbacks.append({
            "video_url": video_url,
            "feedback": feedback_text
        })
        # feedback.txt 파일에 피드백 추가 저장
        with open("feedback.txt", "a", encoding="utf-8") as f:
            f.write(f"{video_url}: {feedback_text}\n")
        st.success(f"피드백이 저장되었습니다.")
        st.rerun()  # 화면 새로고침

cols = st.columns(2)
for idx, v in enumerate(videos):
    with cols[idx % 2]:
        st.subheader(os.path.basename(v))
        st.video(v)




