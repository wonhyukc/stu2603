# 3주차: 입력 폼 기초 / Week 3: Input Forms Basics

**강사 / Instructor:** Wonhyuk William Chung (wonhyukc@stu.ac.kr)

---

## [S1] 웹과 소통하기: 폼 태그의 구성 / [S1] Communicating with the Web: Form Tags Breakdown

- **웹의 쌍방향 소통 채널** 
  - 정적 명함에서 방문자와 상호작용하는 폼(Form) 추가
- **Two-way Communication Channel on the Web**
  - Adding a Form that interacts with visitors to your static business card

- **핵심 태그 삼총사**
  - `<form>`: 서류를 담는 빈 폴더 (입력 구역 설정)
  - `<input>`: 실제 펜으로 글씨를 적는 입력 칸
  - `<button>`: 작성한 폼을 전송하는 역할
- **The Core Tag Trio**
  - `<form>`: An empty folder for documents (sets the input area)
  - `<input>`: The input field where you actually write text
  - `<button>`: Submits the completed form

- **마법의 `type` 속성**
  - `text`, `password`, `email`, `date` 등 목적에 따라 모습 변환
- **The Magical `type` Attribute**
  - Changes appearance based on purpose: `text`, `password`, `email`, `date`, etc.

---

## [S2] 방명록 폼 만들기 데모 / [S2] Building the Guestbook Form Demo

- **온라인 명함에 방명록 달기**
  - 이름, 이메일, 남길 메시지를 받는 레이아웃 구성
- **Adding a Guestbook to the Online Business Card**
  - Structuring a layout to receive name, email, and a message

- **다양한 입력 필드 활용**
  - `<label>`: 이름표 붙이기
  - `<textarea>`: 여러 줄의 긴 메시지 입력 공간 마련
- **Utilizing Various Input Fields**
  - `<label>`: Attaching a name tag
  - `<textarea>`: Providing space for long, multi-line messages

- **브라우저의 기본 폼 전송 방식**
  - 제출 시 페이지가 강력하게 '새로고침' 되는 정상적인 작동 원리 이해
- **The Browser's Default Form Submission Method**
  - Understanding the normal operating principle of the page 'refreshing' upon submission

---

## [S3] 태그 디버깅 및 AI 폼 유효성 검사 / [S3] Tag Debugging & AI Form Validation

- **웹 개발의 꽃, 디버깅**
  - 닫지 않은 태그(`</form>`)로 인해 전체 구조와 레이아웃이 깨지는 흔한 오류 해결
- **The MVP of Web Development, Debugging**
  - Fixing common errors where the overall structure and layout break due to unclosed tags (`</form>`)

- **똑똑한 브라우저의 유효성 검사**
  - `type="email"` 지정 시 '@' 기호 누락을 스마트하게 잡아내는 기능
- **The Smart Browser's Validation Check**
  - The built-in feature that smartly catches missing '@' symbols when `type="email"` is assigned

- **AI 조수 활용 및 맹점 비평**
  - 복잡한 가입 폼을 AI에게 요청하여 신속하게 뼈대 구축
  - 코드의 맹점(예: 잘못된 `type` 할당 등)을 비판적으로 직접 검증하는 실습 
- **Utilizing AI Assistants and Critiquing Blind Spots**
  - Requesting the AI to rapidly build the skeleton for complex signup forms
  - Practicing critical, hands-on validation to find blind spots in the code (e.g., incorrect `type` assignment)
