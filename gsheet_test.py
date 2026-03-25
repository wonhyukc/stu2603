import gspread
from google.oauth2.service_account import Credentials

# 권한 범위 설정
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# 서비스 계정 키 파일 경로
SERVICE_ACCOUNT_FILE = 'secret.json'

def main():
    try:
        # 인증 및 클라이언트 생서
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
        client = gspread.authorize(creds)

        # 스프레드시트 열기 (URL 사용)
        spreadsheet_url = "https://docs.google.com/spreadsheets/d/1XA5Hnu5PEidFMreanPCy1eMrofGiyFDPo4buN3129Mc/edit"
        sheet = client.open_by_url(spreadsheet_url)

        # 'AGY_TEST' 워크시트 생성 (이미 있으면 열기)
        try:
            worksheet = sheet.add_worksheet(title="AGY_TEST", rows="100", cols="20")
            print("Created new worksheet 'AGY_TEST'.")
        except gspread.exceptions.APIError:
            worksheet = sheet.worksheet("AGY_TEST")
            print("Found existing worksheet 'AGY_TEST'.")

        # 테스트 데이터 추가
        test_row = ["99999999", "TEST AGENT", "테스트 에이전트", "test@example.com", "AI", "SUCCESS"]
        worksheet.append_row(test_row)

        print("Successfully appended a test row to 'AGY_TEST' sheet.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
