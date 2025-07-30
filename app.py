import streamlit as st
import os

# 기존 TXT 처리 스크립트 임포트
from parsing_data import process_and_save_data

# 새 TXT to Excel 스크립트 임포트
from txt_to_xlsx import parse_and_save_to_excel_flexible_pos_v3

st.set_page_config(page_title="New Voca", layout="centered")

st.title("txt 파일 변환기")
st.write("아래의 기능을 통해 원본 데이터 전처리와 엑셀 파일 변환이 가능합니다.")

# --- 탭을 사용하여 기능 구분 ---
tab1, tab2 = st.tabs(["1차 전처리", "최종 xlsx 파일 생성"])

# --- 첫 번째 탭: TXT 파일 형식 변환 ---
with tab1:
    st.header("원본 데이터 1차 전처리")
    st.write("원본 txt 파일을 업로드하면, 1차 전처리가 완료된 txt 파일을 다운로드할 수 있습니다.")

    uploaded_file_txt_process = st.file_uploader("변환할 txt 파일을 업로드하세요", type=["txt"], key="txt_process_uploader")

    if uploaded_file_txt_process is not None:
        original_filename = uploaded_file_txt_process.name
        base_name, extension = os.path.splitext(original_filename)
        custom_output_filename = f"{base_name}(pp){extension}"

        input_filepath = "uploaded_input_for_txt_process.txt"
        output_filepath = "processed_output_for_txt_process.txt"

        try:
            with open(input_filepath, "wb") as f:
                f.write(uploaded_file_txt_process.getbuffer())
            st.success(f"'{original_filename}' 파일이 성공적으로 업로드되었습니다. 이제 '1차 전처리 시작' 버튼을 눌러주세요.")
        except Exception as e:
            st.error(f"파일 저장 중 오류가 발생했습니다: {e}")
            if os.path.exists(input_filepath):
                os.remove(input_filepath)
            st.stop()

        if st.button("1차 전처리 시작", key="process_txt_button"):
            st.info("txt 파일을 처리 중입니다. 잠시만 기다려주세요...")

            processing_successful = process_and_save_data(input_filepath, output_filepath)

            if processing_successful:
                st.success("txt 파일 형식 변환이 완료되었습니다!")

                if os.path.exists(output_filepath):
                    with open(output_filepath, "rb") as f:
                        st.download_button(
                            label=f"결과 파일 다운로드 ({custom_output_filename})",
                            data=f.read(),
                            file_name=custom_output_filename,
                            mime="text/plain"
                        )
                else:
                    st.error("오류: 처리된 'processed_output_for_txt_process.txt' 파일을 찾을 수 없습니다. 스크립트를 확인해 주세요.")
            else:
                st.error("txt 파일 형식 변환 중 오류가 발생했습니다. 스크립트의 로그 또는 콘솔 출력을 확인해 주세요.")

            if os.path.exists(input_filepath):
                os.remove(input_filepath)
            if os.path.exists(output_filepath):
                os.remove(output_filepath)

# --- 두 번째 탭: TXT to Excel 변환 ---
with tab2:
    st.header("최종 xlsx 파일 생성")
    st.write("txt 파일을 업로드하면, 최종 `.xlsx` 파일을 다운로드할 수 있습니다.")

    uploaded_file_excel_convert = st.file_uploader("xlsx 파일로 변환할 txt 파일을 업로드하세요", type=["txt"], key="excel_convert_uploader")

    if uploaded_file_excel_convert is not None:
        original_excel_filename = uploaded_file_excel_convert.name
        base_name_excel, _ = os.path.splitext(original_excel_filename)
        # Excel 파일명은 .xlsx 확장자로 고정
        custom_excel_output_filename = f"{base_name_excel}.xlsx"

        input_filepath_excel = "uploaded_input_for_excel_convert.txt"
        output_excel_filepath = "converted_output.xlsx"

        try:
            with open(input_filepath_excel, "wb") as f:
                f.write(uploaded_file_excel_convert.getbuffer())
            st.success(f"'{original_excel_filename}' 파일이 성공적으로 업로드되었습니다. 이제 '최종 파일 변환 시작' 버튼을 눌러주세요.")
        except Exception as e:
            st.error(f"파일 저장 중 오류가 발생했습니다: {e}")
            if os.path.exists(input_filepath_excel):
                os.remove(input_filepath_excel)
            st.stop()

        if st.button("TXT to Excel 변환 시작", key="convert_to_excel_button"):
            st.info("TXT를 Excel로 변환 중입니다. 잠시만 기다려주세요...")

            conversion_successful = parse_and_save_to_excel_flexible_pos_v3(input_filepath_excel, output_excel_filepath)

            if conversion_successful:
                st.success("최종 파일 생성이 완료되었습니다!")

                if os.path.exists(output_excel_filepath):
                    with open(output_excel_filepath, "rb") as f:
                        st.download_button(
                            label=f"결과 파일 다운로드 ({custom_excel_output_filename})",
                            data=f.read(),
                            file_name=custom_excel_output_filename,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # Excel MIME 타입
                        )
                else:
                    st.error("오류: 변환된 'converted_output.xlsx' 파일을 찾을 수 없습니다. 스크립트를 확인해 주세요.")
            else:
                st.error("TXT to Excel 변환 중 오류가 발생했습니다. 스크립트의 로그 또는 콘솔 출력을 확인해 주세요.")

            if os.path.exists(input_filepath_excel):
                os.remove(input_filepath_excel)
            if os.path.exists(output_excel_filepath):
                os.remove(output_excel_filepath)
