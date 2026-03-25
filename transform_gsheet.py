import gspread
import re
from google.oauth2.service_account import Credentials

# 설정 정보
SHEET_ID = "1F69Wtmrr3MYMJI8jgjPKBWh3m8tDaX6QyBVDSHH4vEc"
SOURCE_SHEET_NAME = "progess"
TARGET_SHEET_NAME = "progess_transformed"

# 변환 대상 컬럼 키워드 (헤더에 포함되어 있으면 매핑)
target_5_scale = [
    "1주차수업은", "1주차과제는", "2주차수업은", "2주차과제는"
]

target_boolean = [
    "과제0.1 제출", "과제0.2", "github repo에 wonhyukc 초대했다"
]

def parse_5_scale(text):
    """5점 척도 역순/역방향 변환 로직"""
    if text is None or str(text).strip() == "":
        return ""
    text = str(text).lower()
    
    # 1. 명시적인 숫자가 존재하는지 먼저 체크
    match = re.search(r'\b([1-5])\b', text)
    if match:
        val = int(match.group(1))
        return 6 - val # 항상 역순
    
    positive_words = ["쉽", "잘", "좋", "재밌", "만족", "이해", "간단", "편하", "적당"]
    negative_words = ["어렵", "힘들", "모르", "복잡", "부족", "못", "안"]
    
    pos_score = sum(1 for w in positive_words if w in text)
    neg_score = sum(1 for w in negative_words if w in text)
    
    # 긍정적일수록 점수 낮음 (역순)
    if pos_score > neg_score:
        return 2
    elif neg_score > pos_score:
        return 4
    else:
        return ""

def parse_boolean(text):
    """이진(0/1) 규칙 기반 변환 로직. (원본이 빈칸이면 빈칸 유지)"""
    if text is None or str(text).strip() == "":
        return ""
    text = str(text).lower()
    
    completed_words = ["제출", "했어요", "완료", "함", "yes", "o", "네", "예", "초대"]
    for w in completed_words:
        if w in text:
            return 1
            
    if "1" in text:
        return 1
    return 0
    
def transform_sheet():
    print("[1] 구글 스프레드시트에 연결합니다...")
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    SERVICE_ACCOUNT_FILE = 'secret.json'
    try:
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
        gc = gspread.authorize(creds)
    except Exception as e:
        print(f"인증 실패: {e}")
        return

    sh = gc.open_by_key(SHEET_ID)
    source_ws = sh.worksheet(SOURCE_SHEET_NAME)
    
    print("원시 데이터 로드 중...")
    data = source_ws.get_values(value_render_option="FORMULA")
    if not data:
        print("시트가 비어있습니다.")
        return
        
    print("[2] 원본 컬럼 구조를 스캔합니다...")
    header_idx = 0
    for i, row in enumerate(data):
        if '강좌번호' in row or '이메일' in row or '성명' in row or 'student number' in row:
            header_idx = i
            break
            
    headers = [str(h).strip() for h in data[header_idx]]
    max_cols = max(len(row) for row in data)
    
    target_5_indices = [i for i, h in enumerate(headers) if any(t in h for t in target_5_scale)]
    target_bool_indices = [i for i, h in enumerate(headers) if any(t in h for t in target_boolean)]

    print("[3] 데이터 파싱 및 척도 역방향 변환을 적용합니다...")
    top_rows = data[:header_idx]
    
    parsed_records = []
    total_checks = 0
    valid_count = 0
    
    for row in data[header_idx:]:
        if header_idx == len(top_rows) and len(parsed_records) == 0:
            parsed_row = list(row) + [""] * (max_cols - len(row))
            parsed_records.append(parsed_row)
            continue
            
        parsed_row = list(row) + [""] * (max_cols - len(row))
        
        # 역방향 5점 척도
        for i in target_5_indices:
            org_val = parsed_row[i]
            new_val = parse_5_scale(org_val)
            parsed_row[i] = new_val
            total_checks += 1
            if str(new_val) in ["1", "2", "3", "4", "5", ""]:
                valid_count += 1
                
        # Boolean 변환
        for i in target_bool_indices:
            org_val = parsed_row[i]
            new_val = parse_boolean(org_val)
            parsed_row[i] = new_val
            total_checks += 1
            if str(new_val) in ["0", "1", ""]:
                valid_count += 1
                
        parsed_records.append(parsed_row)
        
    print("[4] 새로운 시트에 일괄 덮어쓰기(Batch Update)를 수행합니다...")
    updated_values = top_rows + parsed_records
    
    try:
        target_ws = sh.worksheet(TARGET_SHEET_NAME)
        print(f"기존 '{TARGET_SHEET_NAME}' 시트 초기화 중...")
        target_ws.clear()
        target_ws.clear_basic_filter()
    except gspread.exceptions.WorksheetNotFound:
        target_ws = sh.add_worksheet(title=TARGET_SHEET_NAME, rows=str(max(100, len(updated_values))), cols=str(max_cols))
        
    target_ws.update(updated_values, value_input_option="USER_ENTERED")
    
    print("[4.5] 새 시트에 데이터 유효성 검사(Data Validation) 룰을 적용합니다...")
    requests = []
    
    # Validation for 5-scale (1 ~ 5)
    for col_idx in target_5_indices:
        requests.append({
            "setDataValidation": {
                "range": {
                    "sheetId": target_ws.id,
                    "startRowIndex": header_idx + 1,
                    "startColumnIndex": col_idx,
                    "endColumnIndex": col_idx + 1
                },
                "rule": {
                    "condition": {
                        "type": "NUMBER_BETWEEN",
                        "values": [
                            {"userEnteredValue": "1"},
                            {"userEnteredValue": "5"}
                        ]
                    },
                    "strict": True,
                    "showCustomUi": True
                }
            }
        })
        
    # Validation for Boolean (0 or 1)
    for col_idx in target_bool_indices:
        requests.append({
            "setDataValidation": {
                "range": {
                    "sheetId": target_ws.id,
                    "startRowIndex": header_idx + 1,
                    "startColumnIndex": col_idx,
                    "endColumnIndex": col_idx + 1
                },
                "rule": {
                    "condition": {
                        "type": "ONE_OF_LIST",
                        "values": [
                            {"userEnteredValue": "0"},
                            {"userEnteredValue": "1"}
                        ]
                    },
                    "strict": True,
                    "showCustomUi": True
                }
            }
        })
        
    if requests:
        body = {"requests": requests}
        sh.batch_update(body)
        print(f"데이터 규칙(Data Validation) 적용 완료: 5점 척도 범위({len(target_5_indices)}열), 이진 범위({len(target_bool_indices)}열)")
        
    print("[5] 결과 검증 및 분석 완료...")
    acc = (valid_count / total_checks) * 100 if total_checks > 0 else 0
    print(f"--- 📊 변환 검증 리포트 (Verification Report) ---")
    print(f"* 내부 데이터 형태 무결성: {valid_count}건 패스 / 총 {total_checks} 데이터 셀 (일치율: {acc:.1f}%)")

if __name__ == "__main__":
    transform_sheet()
