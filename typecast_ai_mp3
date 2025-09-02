import streamlit as st
import os

# 페이지 제목 설정
st.title("AI 음원 파일 재생 목록")
st.write("아래에서 AI 목소리를 들어보세요.<br>문장은 <b>'I touch the door. I touch the duck eggs. I touch the frog.'</b> 입니다.", unsafe_allow_html=True)
# 음원 파일이 저장된 폴더 경로
audio_folder = "audio_files"

# 음원 파일 목록 불러오기 (파일명에서 직접 이름 추출)
try:
    audio_files = sorted(os.listdir(audio_folder))
    # MP3 파일만 필터링하고, 확장자를 제거한 파일명을 이름으로 사용
    audio_data = []
    for f in audio_files:
        if f.endswith('.mp3'):
            name = os.path.splitext(f)[0]  # 확장자 제거
            audio_data.append({"name": name, "file_path": os.path.join(audio_folder, f)})
except FileNotFoundError:
    st.error(f"'{audio_folder}' 폴더를 찾을 수 없습니다. 음원 파일을 폴더에 넣어주세요.")
    st.stop()
except Exception as e:
    st.error(f"음원 폴더를 읽는 중 오류가 발생했습니다: {e}")
    st.stop()

# 음원 데이터가 있는 경우에만 표시
if audio_data:
    # --- 이름과 음원 파일을 순서대로 페이지에 표시 ---
    for i, item in enumerate(audio_data):
        name = item["name"]
        file_path = item["file_path"]

        # 이름과 함께 음원 파일 표시
        st.subheader(f"{i + 1}. {name}")
        st.audio(file_path, format="audio/mp3")
        st.markdown("---")
else:
    st.info("음원 파일이 없습니다. 'audio_files' 폴더에 `.mp3` 파일을 넣어주세요.")

st.markdown("(참고) Typecast 유료 플랜") # 이미지 위에 제목을 붙이고 싶다면
image_path = "images/program_plan.png" # 이미지 파일 경로를 지정합니다.

if os.path.exists(image_path):
    st.image(image_path)
else:
    st.warning(f"경고: 이미지 파일 '{image_path}'를 찾을 수 없습니다. 경로를 확인해주세요.")
