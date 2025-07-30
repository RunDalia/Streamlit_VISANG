import re

def process_and_save_data(input_filepath, output_filepath):
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        # 오류 발생 시 False 반환
        print(f"오류: '{input_filepath}' 파일을 찾을 수 없습니다.")
        return False # <-- 수정: False를 명확하게 반환
    except Exception as e:
        # 오류 발생 시 False 반환
        print(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        return False # <-- 수정: False를 명확하게 반환

    # 각 항목을 분리할 정규 표현식 (발음 기호는 이제 선택적)
    pattern = re.compile(r'(?s)(\d{3})\n([^\n]+)\n(?:\[.*?\]\n)?(.*?)(?=\n\d{3}|\Z)')

    processed_lines = []

    # 정규 표현식으로 모든 매칭되는 항목 찾기
    for match in pattern.finditer(data):
        item_number = match.group(1).strip()
        word = match.group(2).strip()
        description = match.group(3).strip()

        if processed_lines:
            processed_lines.append("")

        processed_lines.append(item_number)
        processed_lines.append(word)
        processed_lines.append(description)

    # 결과를 새로운 TXT 파일로 저장
    try:
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(processed_lines))
        print(f"데이터 처리가 완료되었고, '{output_filepath}' 파일에 저장되었습니다.")
        return True # <-- 성공적으로 처리되었음을 알림
    except Exception as e:
        # 오류 발생 시 False 반환
        print(f"파일을 쓰는 중 오류가 발생했습니다: {e}")
        return False # <-- 수정: False를 명확하게 반환
