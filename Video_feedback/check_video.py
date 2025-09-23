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

cols = st.columns(2)
for idx, v in enumerate(videos):
    with cols[idx % 2]:
        st.subheader(os.path.basename(v))
        st.video(v)

        feedback = st.text_area(f"💬 피드백 입력", key=v)
        if st.button(f"send", key=f"btn_{v}"):
            with open("feedback.txt", "a", encoding="utf-8") as f:
                f.write(f"{v}: {feedback}\n")
            st.success(f"{v} 피드백이 저장되었습니다.")
