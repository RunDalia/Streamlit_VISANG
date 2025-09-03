import streamlit as st
import os

# 페이지 제목 설정
st.title("AI 음원 파일 재생 목록")

# --- 탭(Tabs)을 사용하여 기능 구분 ---
tab1, tab2 = st.tabs(["AI 목소리 후보 목록", "View Plus AI 음원 목록"])

# --- 첫 번째 탭: AI 목소리 후보 목록 ---
with tab1:
    st.header("AI 목소리 후보 목록")
    st.write("아래에서 AI 목소리를 들어보세요.<br>문장은 <b>'I touch the door. I touch the duck eggs. I touch the frog.'</b> 입니다.",
             unsafe_allow_html=True)

    # 음원 파일이 저장된 폴더 경로
    audio_folder = "audio_files"

    # 음원 파일 목록 불러오기 (파일명에서 직접 이름 추출)
    try:
        audio_files = sorted(os.listdir(audio_folder))
        audio_data = []
        for f in audio_files:
            if f.endswith('.mp3'):
                name = os.path.splitext(f)[0]
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

    st.markdown("(참고) Typecast 유료 플랜")
    image_path = "images/program_plan.png"

    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.warning(f"경고: 이미지 파일 '{image_path}'를 찾을 수 없습니다. 경로를 확인해주세요.")

# --- 두 번째 탭: View Plus AI 음원 목록 ---
with tab2:
    st.header("View Plus AI 음원 목록")
    st.write("다양한 AI 목소리를 들어보세요. 문장은 아래를 참고해주세요.")
    code_block = """
    ```markdown
    ▫️photographer
      - The photographer takes pictures of nature.
    
    ▫️look like
      - The dog looks like a lion.
    
    ▫️thank
      - I thank my friends for coming to my birthday party.
    
    ▫️disappointed
      - I was disappointed with the chef’s dish.
    """
    st.write(code_block)


    # 두 번째 탭을 위한 별도 음원 폴더 경로 (이름을 적절히 변경하여 사용하세요)
    viewplus_audio_folder = "viewplus_audio_files"

    try:
        viewplus_audio_files = sorted(os.listdir(viewplus_audio_folder))
        viewplus_audio_data = [{"name": os.path.splitext(f)[0], "file_path": os.path.join(viewplus_audio_folder, f)} for
                               f in viewplus_audio_files if f.endswith('.mp3')]
    except FileNotFoundError:
        st.error(f"'{viewplus_audio_folder}' 폴더를 찾을 수 없습니다. 두 번째 탭에 표시할 음원 파일을 해당 폴더에 넣어주세요.")
        st.stop()
    except Exception as e:
        st.error(f"음원 폴더를 읽는 중 오류가 발생했습니다: {e}")
        st.stop()

    if viewplus_audio_data:
        # 2열 생성
        cols = st.columns(2)

        # 음원 파일을 2개의 열에 교대로 배치
        for i, item in enumerate(viewplus_audio_data):
            col_index = i % 2  # 0 또는 1

            # 첫 번째 열
            if col_index == 0:
                with cols[0]:
                    st.subheader(f"{i + 1}. {item['name']}")
                    st.audio(item['file_path'], format="audio/mp3")
                    st.markdown("---")
            # 두 번째 열
            else:
                with cols[1]:
                    st.subheader(f"{i + 1}. {item['name']}")
                    st.audio(item['file_path'], format="audio/mp3")
                    st.markdown("---")
    else:
        st.info("음원 파일이 없습니다. 'viewplus_audio_files' 폴더에 `.mp3` 파일을 넣어주세요.")

    st.markdown("(참고) Typecast AI Voice 유료 플랜")
    image_path = "images/program_plan02.png"
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.warning(f"경고: 이미지 파일 '{image_path}'를 찾을 수 없습니다. 경로를 확인해주세요.")
