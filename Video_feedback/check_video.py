import streamlit as st
import os

st.set_page_config(page_title="팀 영상 리뷰", layout="wide")
st.title("🎬 따라쓰기 영상 피드백")

# 클라우드 영상 URL 리스트
videos = [
    "https://felcms.allviacms.com/fileRoot/question/temp/a.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/b.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/c.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/d.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/d1.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/e.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/f.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/g.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/h.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/i.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/j.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/J1.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/k.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/L.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/m.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/n.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/o.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/p.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/q.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/r.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/s.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/t.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/t1.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/u.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/v.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/w.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/x.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/y.mp4",
    "https://felcms.allviacms.com/fileRoot/question/temp/z.mp4"

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


