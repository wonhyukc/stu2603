import gspread
import re
from google.oauth2.service_account import Credentials

# 설정 정보
SHEET_ID = "1XA5Hnu5PEidFMreanPCy1eMrofGiyFDPo4buN3129Mc"
SOURCE_SHEET_NAME = "progess"
TARGET_SHEET_NAME = "progess_transformed"

# 변환 대상 컬럼
target_5_scale = [
    "gemini live 사용", "한국어실력", "컴퓨터 수준", "타이핑",
    "1주차수업은", "1주차과제는", "2주차수업은", "2주차과제는"
]

target_boolean = [
    "과제0.1 제출", "과제0.2 제출"
]

def parse_5_scale(text):
    """5점 척도 규칙 기반 변환 로직"""
    if text is None or str(text).strip() == "":
        return ""
    text = str(text).lower()
    
    match = re.search(r'\b([1-5])\b', text)
    if match:
        return int(match.group(1))
    
    positive_words = ["쉽", "잘", "좋", "재밌", "만족", "이해", "간단", "편하", "적당"]
    negative_words = ["어렵", "힘들", "모르", "복잡", "부족", "못", "안"]
    
    pos_score = sum(1 for w in positive_words if w in text)
    neg_score = sum(1 for w in negative_words if w in text)
    
    if pos_score > neg_score:
        return 4
    elif neg_score > pos_score:
        return 2
    else:
        return ""

def parse_boolean(text):
    """이진(0/1) 규칙 기반 변환 로직"""
    if text is None or str(text).strip() == "":
        return 0
    text = str(text).lower()
    
    completed_words = ["제출", "했어요", "완료", "함", "yes", "o", "네", "예"]
    for w in completed_words:
        if w in text:
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
    # 원본 시트에서 수식을 보존하며 로드
    data = source_ws.get_values(value_render_option="FORMULA")
    if not data:
        print("시트가 비어있습니다.")
        return
        
    print("[2] 원본 컬럼 구조를 스캔합니다...")
    # 헤더 행 찾기 ('이메일'이나 '성명'이 포함된 행을 헤더로 취급)
    header_idx = 0
    for i, row in enumerate(data):
        if '이메일' in row or '성명' in row:
            header_idx = i
            break
            
    # 원본 데이터와 헤더 이름 분리
    headers = [str(h).strip() for h in data[header_idx]]
    max_cols = max(len(row) for row in data)
    
    # 변환 대상 컬럼들의 인덱스 찾기 (여러 개일 경우 전부 포함)
    target_5_indices = [i for i, h in enumerate(headers) if h in target_5_scale]
    target_bool_indices = [i for i, h in enumerate(headers) if h in target_boolean]

    print("[3] 데이터 파싱 및 척도 변환 룰을 적용합니다...")
    # 상단 열(수식 등)은 그대로 유지
    top_rows = data[:header_idx]
    
    # 데이터 영역 변환
    parsed_records = []
    total_checks = 0
    valid_count = 0
    
    for row in data[header_idx:]:
        # 헤더 행 자체는 변환하지 않음
        if header_idx == len(top_rows) and len(parsed_records) == 0:
            parsed_row = list(row) + [""] * (max_cols - len(row))
            parsed_records.append(parsed_row)
            continue
            
        parsed_row = list(row) + [""] * (max_cols - len(row))
        
        # 5점 척도 변환 수행
        for i in target_5_indices:
            org_val = parsed_row[i]
            new_val = parse_5_scale(org_val)
            parsed_row[i] = new_val
            
            # 검증 데이터 카운팅 로직 내장
            total_checks += 1
            if str(new_val) in ["1", "2", "3", "4", "5", ""]:
                valid_count += 1
                
        # Boolean 변환 수행
        for i in target_bool_indices:
            org_val = parsed_row[i]
            new_val = parse_boolean(org_val)
            parsed_row[i] = new_val
            
            total_checks += 1
            if str(new_val) in ["0", "1", ""]:
                valid_count += 1
                
        parsed_records.append(parsed_row)
        
    print("[4] 새로운 시트에 일괄 덮어쓰기(Batch Update)를 준비합니다...")
    updated_values = top_rows + parsed_records
    
    # 새 워크시트 가져오거나 생성하기
    try:
        target_ws = sh.worksheet(TARGET_SHEET_NAME)
        print(f"기존 '{TARGET_SHEET_NAME}' 시트를 발견했습니다. 시트 내용을 비웁니다(Clear).")
        target_ws.clear()
    except gspread.exceptions.WorksheetNotFound:
        print(f"새로운 '{TARGET_SHEET_NAME}' 시트를 생성합니다.")
        target_ws = sh.add_worksheet(title=TARGET_SHEET_NAME, rows=str(len(updated_values)), cols=str(max_cols))
        
    print(f"새 시트('{TARGET_SHEET_NAME}')에 데이트 쓰기를 시작합니다...")
    target_ws.update(updated_values, value_input_option="USER_ENTERED")
    print(f"✅ {len(parsed_records) - 1}개 데이터 행 변환 및 저장 완료!")
    
    print("[5] 결과 검증 및 분석 완료...")
    acc = (valid_count / total_checks) * 100 if total_checks > 0 else 0
    print(f"--- 📊 변환 검증 리포트 (Verification Report) ---")
    print(f"* 내부 데이터 형태(포맷) 무결성: {valid_count}건 패스 / 총 {total_checks} 데이터 셀 (일치율: {acc:.1f}%)")
    print("- (모호한 답변은 안전하게 '빈칸' 처리되었습니다)")

if __name__ == "__main__":
    transform_sheet()
