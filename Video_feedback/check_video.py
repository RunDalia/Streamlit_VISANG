import streamlit as st
import os

st.set_page_config(page_title="팀 영상 리뷰", layout="wide")
st.title("🎬 따라쓰기 영상 피드백")

# 영상이 들어있는 폴더 지정 (예: videos 폴더 안)
VIDEO_DIR = "C:/Users/user/Desktop/예비초등/따라쓰기 영상 외주 관련/0923_output"

if not os.path.exists(VIDEO_DIR):
    st.error(f"'{VIDEO_DIR}' 폴더를 만들어서 영상을 넣어주세요.")
else:
    videos = [f for f in os.listdir(VIDEO_DIR) if f.endswith((".mp4", ".mov", ".webm"))]

    if not videos:
        st.warning("영상 파일이 없습니다. videos 폴더에 mp4/mov/webm 파일을 넣어주세요.")
    else:
        # 2열 레이아웃 만들기
        cols = st.columns(2)
        for idx, v in enumerate(videos):
            with cols[idx % 2]:  # 홀수는 왼쪽, 짝수는 오른쪽
                st.subheader(v)
                st.video(os.path.join(VIDEO_DIR, v))

                feedback = st.text_area(f"💬 {v} 피드백 입력", key=v)
                if st.button(f"send", key=f"btn_{v}"):
                    with open("feedback.txt", "a", encoding="utf-8") as f:
                        f.write(f"{v}: {feedback}\n")
                    st.success(f"피드백이 저장되었습니다.")