import re
import pandas as pd
import os # os 모듈을 import 해두는 것이 좋습니다.

def parse_and_save_to_excel_flexible_pos_v3(input_filepath, output_excel_filepath):
    """
    주어진 TXT 파일에서 데이터를 파싱하고, '복'이 포함된 특정 줄만 제외하며,
    발음 기호가 없는 경우, 품사가 없는 경우, 그리고 특히 한글 의미가 예문으로
    오인되지 않도록 수정하고, 한글 예문에 영어가 포함된 경우도 올바르게
    인식하도록 개선하여 엑셀 파일로 저장합니다.
    """
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"오류: '{input_filepath}' 파일을 찾을 수 없습니다.")
        return False # <-- 수정: False 반환
    except Exception as e:
        print(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        return False # <-- 수정: False 반환

    # 각 항목을 분리할 정규 표현식 (발음 기호는 선택적)
    pattern = re.compile(r'(?s)(\d{3})\n([^\n]+)\n(?:\[.*?\]\n)?(.*?)(?=\n\d{3}|\Z)')

    parsed_rows = []

    for match in pattern.finditer(data):
        index = match.group(1).strip()
        word = match.group(2).strip()
        description_raw = match.group(3).strip()

        # '복'이 포함된 줄을 제외하고 필터링
        lines = [line.strip() for line in description_raw.split('\n') if line.strip() and '복 ' not in line]

        pos_meaning_lines_extracted = []
        sentence_pairs = []

        pos_keywords = ['명', '동', '형', '부', '전', '감', '관', '대', '수', '접']

        current_line_idx = 0

        # 1단계: 품사/의미 줄 추출
        while current_line_idx < len(lines):
            line = lines[current_line_idx]

            is_pos_line = False
            first_word = line.split(' ')[0]
            if first_word in pos_keywords:
                is_pos_line = True

            # 영어 문장처럼 보이는지 판단하는 휴리스틱
            looks_like_english_sentence_candidate = bool(re.search(r'[a-zA-Z]', line)) and \
                                                    not bool(re.search(r'[가-힣]', line)) and \
                                                    (line[0].isupper() or any(c in '.,?!' for c in line) or len(
                                                        line.split()) > 3)

            if is_pos_line or not looks_like_english_sentence_candidate:
                pos_meaning_lines_extracted.append(line)
                current_line_idx += 1
            else:
                break

        # 2단계: 남은 줄에서 예문 추출
        while current_line_idx < len(lines):
            if current_line_idx + 1 < len(lines):
                eng_sentence = lines[current_line_idx].strip()
                kor_sentence = lines[current_line_idx + 1].strip()

                is_valid_eng_sentence = bool(re.search(r'[a-zA-Z]', eng_sentence)) and \
                                        not bool(re.search(r'[가-힣]', eng_sentence))

                is_valid_kor_sentence = bool(re.search(r'[가-힣]', kor_sentence))

                if is_valid_eng_sentence and is_valid_kor_sentence:
                    sentence_pairs.append((eng_sentence, kor_sentence))
                    if len(sentence_pairs) >= 2:
                        break
                    current_line_idx += 2
                else:
                    break
            else:
                break

        # 여러 품사/의미를 결합
        combined_pos_list = []
        combined_meaning_list = []

        for pm_line in pos_meaning_lines_extracted:
            first_part = pm_line.split(' ', 1)[0]
            if first_part in pos_keywords:
                parts = pm_line.split(' ', 1)
                combined_pos_list.append(parts[0])
                if len(parts) > 1:
                    combined_meaning_list.append(parts[1])
                else:
                    combined_meaning_list.append("")
            else:
                combined_pos_list.append("")
                combined_meaning_list.append(pm_line)

        pos = " / ".join([p for p in combined_pos_list if p])
        meaning = " / ".join(combined_meaning_list)

        # 예문을 컬럼에 할당
        sentence_eng_1 = ""
        sentence_kor_1 = ""
        sentence_eng_2 = ""
        sentence_kor_2 = ""

        if len(sentence_pairs) > 0:
            sentence_eng_1 = sentence_pairs[0][0]
            sentence_kor_1 = sentence_pairs[0][1]
        if len(sentence_pairs) > 1:
            sentence_eng_2 = sentence_pairs[1][0]
            sentence_kor_2 = sentence_pairs[1][1]

        parsed_rows.append({
            "index": index,
            "word": word,
            "POS": pos,
            "meaning": meaning,
            "sentence(eng)": sentence_eng_1,
            "sentence(kor)": sentence_kor_1,
            "sentence2(eng)": sentence_eng_2,
            "sentence2(kor)": sentence_kor_2
        })

    df = pd.DataFrame(parsed_rows)
    try:
        df.to_excel(output_excel_filepath, index=False, engine='openpyxl')
        print(f"데이터가 성공적으로 '{output_excel_filepath}' 파일에 저장되었습니다.")
        return True # <-- 수정: 성공 시 True 반환
    except Exception as e:
        print(f"엑셀 파일 저장 중 오류가 발생했습니다: {e}")
        return False # <-- 수정: False 반환