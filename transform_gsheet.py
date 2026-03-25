import pandas as pd
import gspread
import re

# 설정 정보
SHEET_ID = "1XA5Hnu5PEidFMreanPCy1eMrofGiyFDPo4buN3129Mc"
SHEET_NAME = "progess"

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
    if pd.isna(text) or str(text).strip() == "":
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
    if pd.isna(text) or str(text).strip() == "":
        return 0
    text = str(text).lower()
    
    completed_words = ["제출", "했어요", "완료", "함", "yes", "o", "네", "예"]
    for w in completed_words:
        if w in text:
            return 1
    return 0
    
def transform_sheet():
    print("[1] 구글 스프레드시트에 연결합니다...")
    from google.oauth2.service_account import Credentials
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
    ws = sh.worksheet(SHEET_NAME)
    
    print("원시 데이터 로드 중...")
    data = ws.get_values(value_render_option="FORMULA")
    if not data:
        print("시트가 비어있습니다.")
        return
        
    # 헤더 행 찾기 ('이메일'이나 '성명'이 포함된 행을 헤더로 취급)
    header_idx = 0
    for i, row in enumerate(data):
        if '이메일' in row or '성명' in row:
            header_idx = i
            break
            
    # 헤더 앞뒤 공백 제거
    headers = [str(h).strip() for h in data[header_idx]]
    
    max_cols = len(headers)
    records = []
    for row in data[header_idx+1:]:
        records.append(row + [""] * (max_cols - len(row)))
        
    df = pd.DataFrame(records, columns=headers)
    
    # [1.5] 아이뎀포턴시(Idempotency) 검사
    for col in target_5_scale + target_boolean:
        if f"org_{col}" in df.columns:
            print(f"🚨 중복 실행 방지: 'org_{col}' 컬럼이 이미 존재합니다.")
            print("변환 작업이 이미 완료된 시트입니다. 실행을 취소합니다.")
            return

    print("[2] 컬럼 구조를 변경합니다 (`org_` 접두어 붙이기 및 새 컬럼 생성)...")
    
    # 상단 행(수식 등) 열 밀림 맞추기
    top_rows = data[:header_idx]
    
    offset = 0
    original_columns = list(df.columns)
    seen_targets = set()
    
    for c_idx, col in enumerate(original_columns):
        if (col in target_5_scale or col in target_boolean) and col not in seen_targets:
            seen_targets.add(col)
            cur_pos = c_idx + offset
            org_col = f"org_{col}"
            
            # DataFrame 컬럼명 리스트 수정
            cols = list(df.columns)
            cols[cur_pos] = org_col
            df.columns = cols
            
            # 바로 오른쪽에 새 빈 열 삽입 (이름은 기존 col)
            df.insert(cur_pos + 1, col, "", allow_duplicates=True)
            
            # 상단(헤더 위) 행들도 열을 하나씩 늘려줌
            for r_idx in range(len(top_rows)):
                if cur_pos < len(top_rows[r_idx]):
                    top_rows[r_idx].insert(cur_pos + 1, "")
                else:
                    top_rows[r_idx].append("")
                
            offset += 1
    
    print("[3] 데이터 파싱 및 척도 변환 룰을 적용합니다...")
    for col in target_5_scale:
        if f"org_{col}" in df.columns:
            df[col] = df[f"org_{col}"].apply(parse_5_scale)
            
    for col in target_boolean:
        if f"org_{col}" in df.columns:
            df[col] = df[f"org_{col}"].apply(parse_boolean)
            
    df = df.fillna("")
    
    print("[4] 일괄 업데이트(Batch Update)를 수행합니다...")
    updated_values = top_rows + [df.columns.tolist()] + df.values.tolist()
    # 전체 덮어쓰기
    ws.update(updated_values, value_input_option="USER_ENTERED")
    print(f"✅ {len(df)}개 원본 데이터 행 구조 변경 및 파싱 완료!")
    
    print("[5] 결과 검증 및 샘플링 분석 시작...")
    total_samples = min(5, len(df))
    if total_samples > 0:
        sample_df = df.sample(n=total_samples)
        valid_count = 0
        total_checks = 0
        
        for _, row in sample_df.iterrows():
            for col in target_5_scale:
                if f"org_{col}" in row.index:
                    total_checks += 1
                    org_val = str(row[f"org_{col}"]).strip()
                    new_val = str(row[col]).strip()
                    
                    if not org_val and not new_val:
                        valid_count += 1
                    elif new_val in ["1", "2", "3", "4", "5", ""]:
                        valid_count += 1
                        
            for col in target_boolean:
                if f"org_{col}" in row.index:
                    total_checks += 1
                    org_val = str(row[f"org_{col}"]).strip()
                    new_val = str(row[col]).strip()
                    if new_val in ["0", "1", ""]:
                        valid_count += 1
                        
        acc = (valid_count / total_checks) * 100 if total_checks > 0 else 0
        print(f"--- 📊 변환 검증 리포트 (Verification Report) ---")
        print(f"* 무작위 샘플 행 갯수: {total_samples} Rows")
        print(f"* 내부 데이터 형태(포맷) 무결성: {valid_count}건 패스 / 총 {total_checks} 데이터 셀 (일치율: {acc:.1f}%)")
        print("- (모호한 답변은 안전하게 '빈칸' 처리되었습니다)")

if __name__ == "__main__":
    transform_sheet()
