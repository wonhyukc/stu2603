# **[최종] 웹프로그래밍(E트랙) 교육 과정**

본 교육 과정은 서울신학대학교 컴퓨터소프트웨어학과 1학년(국제학부생 위주) 학생들을 대상으로 하며, 모국에서 컴퓨터 교육을 받지 않은 초심자들의 진입 장벽을 낮추기 위해 **직관적인 실생활 예제 중심**으로 프로그래밍 논리 이해도를 높이는 것을 최우선 목표로 합니다. 생성형 AI를 공학적 파트너로 활용하여 대면 실습을 진행하는 **거꾸로 수업(Flipped Learning)** 방식을 채택합니다.

---

## **[참고] 학교 시스템 입력용 기본 정보**
*본 내용은 종합정보시스템 [수업계획서관리] 입력 양식에 맞춘 참고용 텍스트입니다. 가이드라인에 맞추어 복사-붙여넣기 하실 수 있습니다.*

* **수업운영방식 (선택):** 대면수업
* **교과목개요 (20자 이상):** 
  * (교육과정위원회 심의 완료된 사전 승인 내용 기입 요망. 예: 웹 프로그래밍의 기초인 HTML, CSS, JavaScript를 실생활 예제로 이해하여 동적인 웹 페이지를 구현한다.)
* **핵심·전공역량순위 및 비율:** 
  * (예: 전공역량A 50% / 전공역량B 30% / 전공역량C 20% - 학과 기준 지표 합산 100% 필수)
* **학습목표:** 
  1. 친숙한 실생활 예제를 통해 HTML, CSS, JavaScript의 기초 문법과 알고리즘 논리를 쉽게 이해한다.
  2. 사전 컴퓨터 교육 배경이 없는 초보자도 생성형 AI 도구를 활용해 간단한 웹 UI/UX의 오류를 분석하고 수정할 수 있다.
  3. 사용자 친화적인 웹 인터페이스를 기획하고 프론트엔드 환경을 구축하는 능력을 기른다.
* **수업유형 (체크):** 대면수업, 거꾸로 수업(Flipped Learning), 실습 위주
* **수업진행방법 (항목별 20자 이상, 3개):**
  1. (사전학습) 매주 제공되는 eCampus 온라인 영상 강의를 통해 예제 중심 웹 프로그래밍 이론을 선행 학습함.
  2. (본수업) 사전 학습 내용을 바탕으로 직관적인 예제 웹 페이지 제작 실습을 수행하며 즉각적인 피드백을 제공.
  3. (코드비평) 복잡한 코딩 대신 AI 도구로 초기 형태를 생성하고, 스스로 예제의 논리 오류를 찾는 훈련 진행.
  4. (동료평가) 동료 평가를 기본으로 한 상호 코드 리뷰를 통해 학습 결과물을 공유하고 복습의 효과를 극대화함.
* **전년도 변경·개선사항 (20자 이상, 3개):**
  1. 국제학부생 대다수가 컴퓨터 교육 경험이 없음을 고려해, 높은 진입장벽을 낮춘 '실생활 예제 중심'으로 커리큘럼 개편.
  2. 복잡한 이론이나 마크업 암기 시간을 대폭 줄이고, AI가 생성한 예제 코드를 눈으로 확인하고 고쳐보는 대면 실습 강화.
* **기타/온라인수업 유의사항:** Flipped Learning 영상 시청 관련 eCampus 장애 시 정보전산원에 즉각 문의 혹은 교수자에게 이메일 요망.
* **과제물:** 매주 A4 0.5페이지 내외의 '마이크로 과제' 제출 (AI 질의응답 및 자체 검증 결과 포함).
* **주/부교재:** 
  * **주교재:** W3Schools (온라인 무료 제공) - 시각적이고 직관적인 온라인 인터랙티브 예제를 주 레퍼런스로 활용.
  * **참고도서:** 《HTML and CSS: Design and Build Websites》 (Jon Duckett 저) - 기초 문법의 형태학적·시각적 이해를 돕기 위한 참고 도서.

---

## **1. 1학년 공통 기초 가이드 (1주차 및 상시 적용)**

### **[1주차] 오리엔테이션: 대학 생활과 AI 협업의 기초 (수업 축소)**

* **강의 소개:** AI 시대의 개발자 역량 정의 및 거꾸로 수업(Flipped Learning) 운영 방식 안내.  
* **LMS(e-Class) 활용법:** 서울신학대학교 eCampus 및 포털 접속, 공지 확인, 주차별 영상 시청, 과제 제출 방법 가이드.  
* **프로페셔널 커뮤니케이션:**  
  * **이메일 원칙:** 비지니스 이메일 작성 원칙  
  * **게시판/질문 원칙:** '이게 안 돼요' 식의 질문 지양. **[발생 상황 / 본인이 시도해본 것 / 에러 메시지 전문 / AI에게 물어본 결과]**를 포함하여 질문하는 '엔지니어식 질문법' 의무화.  
* **개발 환경 구축:** 클라우드 IDE(StackBlitz) 접속 및 활용, GitHub 계정 연동 (별도의 로컬 프로그램 설치 과정 없음).

### **[상시 과제] 과제 0.1:** 

* **목적:** AI 결과물을 무비판적으로 수용하지 않고, 자신의 로직으로 통제하는 습관 배양.  
* **형식:** 매주 제출되는 **마이크로 과제**로, 분량은 **A4 0.5페이지** 내외로 제한하여 기본적 대학 소양을 키우는 것이 목적  
* **예시**  
  1. **AI Prompt:** 이번 주 주제와 관련하여 AI에게 던진 핵심 질문.  
  2. **AI Critique:** AI 답변 중 '맞는 부분'과 '틀리거나 위험한 부분'을 **한 문장**으로 요약 비평.  
  3. **Final Result:** AI의 초안을 바탕으로 본인이 직접 검증하고 수정한 최종 코드나 논리적 결론.
---

## **2. UX 프로그래밍 (HTML, CSS, JavaScript 기초)**

| 주차 | 주제 | 핵심 기강 및 실생활 예제 학습 | 코드 비평 및 실무 활동 파악 |
| :---- | :---- | :---- | :---- |
| 1 | 웹과 입문 | **[수업 축소]** 어떻게 웹사이트가 보일까? (쉬운 비유로 웹의 원리 소개) | 텍스트만 있는 문서가 어떻게 웹사이트로 변하는지 구경하기 |
| 2 | HTML 기초 | 나만의 '온라인 명함' 뼈대 만들기 (제목, 글, 사진 넣기) | 완성된 명함 코드에서 빠진 이미지 태그 찾아 넣기 |
| 3 | 입력 폼(Form) 기초 | 사용자 정보 받기 (예: 간단한 회원가입 폼 만들기) | 회원가입 폼에서 입력창이 안 눌리는 원인 찾기 |
| 4 | CSS 기초 | 내 명함 꾸미기 (글자 색상, 폰트, 배경색 등 직관적 적용) | 안 보이는 글자색(배경색과 겹치는 색상) 오류 수정하기 |
| 5 | 박스 모델 여백 | 액자 속 사진처럼 공간 만들기 (Margin, Padding 기본) | 너무 다닥다닥 붙어있는 버튼들의 간격 넓혀보기 |
| 6 | 레이아웃 기초 | 화면에 가구 배치하듯 요소 옮기기 (나란히 메뉴 놓기 등) | 세로로 어긋난 메뉴바 규칙을 찾아 가로 정렬로 고치기 |
| 7 | 중간 복습 및 훈련 | 1~6주차 총정리: 쉬운 조립식 '자기소개서 페이지' 만들기 | 주어진 템플릿에 내 정보 채우고 스스로 간단한 스타일 보완하기 |
| **8** | **중간고사** | **[시험 주간]** (평가 방식: 오픈북, 간단한 실습 등) | HTML/CSS 예제 코드 구조를 제대로 이해했는지 기초 확인 점검 |
| 9 | JavaScript 기초 | 자바스크립트로 생명 불어넣기 (예: "클릭하면 팝업 알림 띄우기") | 버튼 눌러도 반응 없는 예제 코드 구조 점검해보기 |
| 10 | 조건문 이해 (IF) | 만약 ~라면? (예: 성인이면 "환영", 아니면 "불가" 표시기) | 조건 논리가 반대로 뒤집힌 나이 확인 로직 바로잡기 |
| 11 | 동적 웹 예제 (1) | 웹 페이지 버튼 조작하기 (클릭 시 화면이 어두워지는 다크모드) | 다크모드 버튼 클릭 시 폰트 색이 변경 안 되는 문제 해결 |
| 12 | 동적 웹 예제 (2) | 버튼 눌러서 이미지 바꾸기 (Day/Night 그림 교체 예제) | 스크립트 연결이 끊어져 원본과 다르게 동작하는 문제 찾기 |
| 13 | 미니 예제 조립 (1) | '오늘의 투두리스트'나 '간단계산기' 등 실생활 예제 체험 기능 기획 | 완성된 예제의 버튼과 입력창을 살펴보고 동작 흐름 토론 |
| 14 | 미니 예제 조립 (2) | 실제 조립 완료 후 모바일 화면(반응형) 체크해보기 | 스마트폰 화면 밖으로 삐져나가는 요소의 크기(width) 수정 |
| **15** | **기말고사** | **[시험 주간]** 예제 결과물 설명 (온라인 화상 구술 등) | 본인이 만들고 수정한 결과물의 부분별 예제 의미 설명하기 |
| 16 | 보강 주간 | **[학사 일정 지정]** 결손 수업 보강 및 성과 리뷰 | 타국에서 프로그래밍 첫 경험 한 학기 회고 및 상호 피드백 |

---

## **3. 평가 (Evaluation)**
* **기말고사/프로젝트 (Final Exam/Project):** 40%
* **중간고사 (Midterm Exam):** 20%
* **과제 (Assignments):** 20%
* **수업 참여도 (Class Participation):** 20%
* **(합계: 100%)**

국제학부생의 수준을 고려하여 **어려운 암기 위주의 지필 평가보다 '본인이 코드를 어느 정도 이해(이해도)했는가'에 초점**을 맞춥니다. AI 코드 생성은 적극 장려됩니다.

* **비동기 설명 영상:** 기말 프로젝트 시 본인의 코드 로직을 직접 설명하는 영상을 제출받아 이해도를 검증합니다.  
* **작업 이력 분석:** IDE 로그(CodeWatcher 등)를 통해 AI의 코드를 단순히 복사했는지, 아니면 한 줄씩 고민하며 수정했는지 확인합니다.  
* **소그룹 면접:** 실시간 세션을 통해 AI가 제안한 코드의 특정 부분을 바꾸면 어떻게 될지 묻는 '압박 질문'을 진행합니다.

**교수자 제언:** 본 과정은 AI가 단순 암기나 반복 코딩 업무를 분담하기 때문에 가능한 설계입니다. 학생들은 기본 문법을 '외우는 대상'이 아닌 **'AI를 통제하기 위한 무기'**로 배우게 되므로, 실제 학습 수준은 오히려 더 깊어집니다.

<br><br><br>

# **[Final] Web Programming (E-Track) Curriculum**

This curriculum is designed primarily for 1st-year International Students in the Computer Software Department at Seoul Theological University. Recognizing that many students lack prior computing education in their home countries, the course aims to lower the barrier to programming by relying heavily on **intuitive, real-world examples** to build logic understanding. It adopts a **Flipped Learning** methodology, utilizing generative AI as a helpful engineering partner during in-class practice.

---

## **[Reference] Basic Info for University System Entry**
*(These texts correspond to the syllabus registration fields in the university's integrated information system. You can copy and paste them as needed.)*

* **Class Operation Method:** Face-to-Face class (대면수업)
* **Course Overview (20+ chars):** 
  * (Please enter the officially approved overview by the Curriculum Committee. e.g., Implement dynamic web pages by understanding HTML, CSS, and JS through intuitive real-world examples.)
* **Core/Major Competency Rankings & Ratios:** 
  * (e.g., Competency A 50% / Competency B 30% / Competency C 20% - Must total 100%)
* **Learning Objectives:**
  1. Easily grasp basic syntax and algorithms of HTML/CSS/JS through familiar, real-world examples.
  2. Enable even complete beginners to use AI tools for analyzing and fixing simple UI/UX errors.
  3. Develop the ability to plan user-friendly web interfaces and set up front-end environments.
* **Class Type (Checkboxes):** Face-to-Face class, Flipped Learning, Practice-oriented
* **Class Progression Method (Max 3 items, 20+ chars each):**
  1. (Pre-learning) Learn theory primarily through example-centric online instruction videos on eCampus weekly.
  2. (Main Class) Perform intuitive, visual web page creation exercises using real-world examples with immediate feedback.
  3. (Code Critique) Use AI to skip complex typing; instead, practice finding logic flaws and fixing examples visually.
  4. (Peer Review) Maximize the effectiveness of review units by implementing structured peer evaluation and mutual code feedback.
* **Changes/Improvements from Last Year (Max 3 items, 20+ chars each):**
  1. Redesigned to be highly 'Example-Centric' to drastically lower the entry barrier for international students lacking computer backgrounds.
  2. Substituted tedious theory/memorization with visual verification and face-to-face guidance on fixing AI-generated templates.
* **Online Class Precautions:** In case of eCampus technical issues during Flipped Learning video viewings, promptly contact IT support or the instructor.
* **Assignments:** Weekly 'Micro-assignments' (max 0.5 A4 page) including AI prompts, self-verification, and final code.
* **Textbook/Materials:**
  * **Main Textbook:** W3Schools (Free Online Resource) - Utilized as the primary reference for interactive, visual, and intuitive examples.
  * **Reference Book:** *HTML and CSS: Design and Build Websites* (by Jon Duckett) - Highly recommended for reading foundational concepts visually and intuitively.

---

## **1. Common Basics Guide for 1st-Year Students (Week 1 & Ongoing)**

### **[Week 1] Orientation: University Life & Basics of AI Collaboration (Reduced Class Load)**

*   **Course Introduction:** Definition of developer capabilities in the AI era and guidelines for the Flipped Learning methodology.
*   **LMS (e-Class) Usage:** Guide on accessing the STU eCampus and Portal, checking announcements, watching weekly videos, and submitting assignments.
*   **Professional Communication:**
    *   **Email Principles:** Guidelines for writing business emails.
    *   **Q&A/Forum Principles:** Discouraging vague questions like "It doesn't work." Enforcing an 'engineer-style questioning method' that must include: **[The situation / What you have tried / Full error message / Results from asking AI]**.
*   **Dev Environment Setup:** Accessing Cloud IDE (StackBlitz) and linking GitHub accounts (No local installations needed).

### **[Ongoing Assignment] Assignment 0.1:**

*   **Objective:** Cultivating the habit of controlling AI logic independently rather than unconditionally accepting AI outputs.
*   **Format:** A **Micro-assignment** submitted weekly, limited to **approx. 0.5 pages in A4** to foster foundational academic literacy.
*   **Example:**
    1.  **AI Prompt:** The core question posed to the AI related to the week's topic.
    2.  **AI Critique:** A **one-sentence** summary critique identifying what the AI got 'right' versus 'wrong or risky'.
    3.  **Final Result:** The final code or logical conclusion verified and modified manually based on the AI's draft.
---

## **2. UX Programming (HTML, CSS, JavaScript Basics)**

| Week | Topic | Core Example-Based Learning | Code Critique & Practical Check |
| :---- | :---- | :---- | :---- |
| 1 | Intro to Web | **[Reduced]** How does a website appear? (Easy analogies for web principles) | Visually observing how plain text transforms into a website. |
| 2 | HTML Basics | Building the skeleton of my 'Online Business Card' (Titles, text, images). | Finding and inserting a missing image tag in a finished business card code. |
| 3 | Input Forms | Receiving user info (e.g., Simple Sign-up Form). | Finding the root cause of an unclickable input box in a sign-up form. |
| 4 | CSS Basics | Decorating my business card (Colors, fonts, backgrounds intuitively). | Fixing invisible text errors (text color blending with the background). |
| 5 | Box Model (Space) | Creating space like a photo frame (Margin, Padding basics). | Widening the gaps between buttons that appear too cramped together. |
| 6 | Layout Basics | Moving elements like arranging furniture (Aligning menus horizontally). | Fixing vertically broken menu bar rules to re-align them horizontally. |
| 7 | Midterm Review | Weeks 1-6 Review: Creating an easy 'Static Resume Page'. | Filling a provided template with personal info and fixing simple styles. |
| **8** | **Midterm Exam** | **[Exam Week]** (Evaluation: Open-book, simple practical task, etc.) | Verifying basic understanding of HTML/CSS example structures. |
| 9 | JS Basics | Breathing life with JavaScript (e.g., "Pop up an alert on click"). | Inspecting example code structure where a button click does nothing. |
| 10 | Control (IF) Logic | "What if...?" logic (e.g., Show "Welcome" if adult). | Correcting age-verification logic where condition checks are reversed. |
| 11 | Dynamic Example (1) | Operating web buttons (Dark Mode background invert on click). | Troubleshooting why font color fails to update during Dark Mode toggle. |
| 12 | Dynamic Example (2) | Changing images on click (Day/Night picture swap swap example). | Finding a broken script link causing deviations from intended behavior. |
| 13 | Mini Example (1) | Planning features for a 'Daily To-Do List' or 'Simple Calculator' example. | Examining buttons & inputs of a finished layout to discuss flow. |
| 14 | Mini Example (2) | Completing assembly and checking mobile screen (responsiveness). | Fixing the width of elements that overflow outside the smartphone screen. |
| **15** | **Final Exam** | **[Exam Week]** Explaining example results (Online verbal presentation, etc.). | Explaining the logical meaning of various parts of the completed work. |
| 16 | Make-up Week | **[Academic Schedule]** Make-up classes and performance review. | Retrospective & feedback on the first programming experience in a foreign country. |

---

## **3. Evaluation**
* **Final Exam/Project:** 40%
* **Midterm Exam:** 20%
* **Assignments:** 20%
* **Class Participation:** 20%
* **(Total: 100%)**

Considering the level of international students, **the focus is entirely on 'how well the student understands the code structure' rather than difficult memorization-based written exams.** The use of AI code generation tools is highly encouraged.

*   **Asynchronous Explanation Video:** For the final project, students submit a video directly explaining their code logic to verify their understanding.
*   **Work History Analysis:** Using IDE logs (e.g., CodeWatcher) to check whether AI code was blindly copy-pasted or modified after line-by-line consideration.
*   **Small Group Interviews:** Real-time sessions involving 'pressure testing' questions—asking what happens if specific parts of the AI-suggested code are changed.

**Professor's Endorsement:** This course design is possible precisely because AI takes over rote memorization and repetitive coding tasks. Students learn basic syntax not as something to 'memorize', but as a **'weapon to control AI'**, meaning the actual depth of learning is far greater.
