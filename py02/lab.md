# [2주차] 실습: 개발 환경 세팅과 에러 디버깅 체험

---

## 1. 필수 개발 도구 설치 (Environment Setup)
여러분의 PC를 전문가의 훈련소로 만들 시간입니다. 이 과정을 한 번만 성공하면 학기 내내 편안합니다. 자신의 컴퓨터 운영체제(Windows 또는 Mac)에 맞게 설치하세요.

### Step 1: Python 설치 (언어 엔진)
1. 구글에서 'Python download'를 검색하거나 `https://www.python.org/downloads/`에 접속합니다.
2. 최신 버전을 다운로드하고 실행합니다.
3. 🚨 **[매우 중요 - Windows 사용자]** 🚨
   * 설치 화면(Install Python 3.x.x) 하단에 있는 **`Add python.exe to PATH`** 체크박스를 **반드시** 선택한 후 설치(`Install Now`)를 누르세요. 이것을 빼먹으면 컴퓨터가 파이썬이 어디 있는지 찾지 못합니다.

### Step 2: VS Code 설치 (코드 에디터 / IDE)
1. 구글에서 'VS Code download'를 검색하거나 `https://code.visualstudio.com/`에 접속합니다.
2. 다운로드 및 기본 설정대로 설치를 완료합니다.

### Step 3: 파이썬 확장 프로그램 설치
1. VS Code를 실행합니다.
2. 왼쪽 메뉴 바에서 네모 상자 모양의 확장 프로그램(Extensions, 단축키 `Ctrl+Shift+X`) 아이콘을 클릭합니다.
3. 검색창에 `Python`을 검색합니다.
4. Microsoft에서 공식 지원하는 'Python' 확장 프로그램을 찾아 `설치(Install)`를 누릅니다.

---

## 2. 첫 번째 스크립트 실행 실습

### Task 1: 파일 만들고 실행하기
1. 컴퓨터 바탕화면에 영어로 된 이름의 새 폴더를 만듭니다. (예: `python_class`)
2. VS Code에서 `파일(File) > 폴더 열기(Open Folder)`를 클릭하여 방금 만든 폴더를 엽니다.
3. 왼쪽에 폴더 이름 옆의 아이콘(새 파일)을 눌러 `hello.py` 파일을 생성합니다. (`.py`는 파이썬 파일의 확장자입니다)
4. 아래 코드를 입력합니다.
   ```python
   print("나의 첫 파이썬 코드입니다.")
   ```
5. 화면 오른쪽 위에 있는 `▶` 모양(재생 버튼, Run Python File)을 누릅니다.
6. 화면 밑부분(터미널 창)에 글자가 정상적으로 뜨는지 확인합니다!

---

## 3. 에러 발생 유도 및 오류 디버깅 훈련 (Bug Hunting)

**🚨 완벽하게 동작하는 코드를 망가뜨려서 어떤 에러가 나는지 확인하는 것이 진짜 공부입니다.**

1. `print()`의 따옴표나 괄호를 하나씩 지우고 실행해보세요. 에러 메시지를 잘 보세요.
   * `SyntaxError: unterminated string literal` (문자열이 안 끝났어!) 등등
2. `print`를 `printf`나 `prnt`처럼 오타를 내고 실행해보세요.
   * `NameError: name 'prnt' is not defined` ('prnt'가 뭔지 정의되지 않았어!)
3. 파이썬은 대문자와 소문자를 엄격하게 구별합니다. `Print("안녕")`을 실행해보고 차이를 느껴보세요.

어떤 에러 메시지가 여러분이 자주 겪게 될 메시지인지 눈에 익혀두는 것이 핵심입니다!
