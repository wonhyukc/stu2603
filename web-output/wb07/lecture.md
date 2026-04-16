# wb07 주차 (E트랙 7주차) - 강의안 (Instructor's Note) / Week 07 (E-Track Week 7) - Instructor's Note

## 강의 기본 정보 / Class Basic Info
* **주제**: 레이아웃 (Flex) 및 전반기 총정리 + 윈도우 필수 생존 기술 (컴퓨터 활용도)
* **Topic**: Layout (Flex) and First-Half Review + Essential Windows Survival Skills (Computer Proficiency)
* **목표** / **Objectives**:
  1. Flexbox 배치 원리를 파악하고 기초 포트폴리오 조립을 완성한다.
  1. Understand Flexbox alignment principles and complete the basic portfolio assembly.
  2. 복합 페이지에서 발생하는 기초 배치 오류를 리팩터링한다.
  2. Refactor basic alignment errors that occur in complex pages.
  3. 윈도우 파일 시스템 통제(정렬, 클라우드) 및 필수 생존 단축키 5가지를 익힌다.
  3. Master Windows file system control (sorting, cloud) and 5 essential survival shortcut keys.
* **소요 시간**: 총 75분 (S1 15분, S2 15분, S3 15분, S4 30분)
* **Duration**: Total 75 minutes (S1 15 min, S2 15 min, S3 15 min, S4 30 min)

## 강의 진행 체크리스트 (Instructor Checklist) / Instructor Checklist
* *(Instructor Note: 본 7주차는 파이썬(K트랙)의 진도를 참고하여, 기존 '팀플 폭탄 대비 문서 도구' 특강 대신 '컴퓨터 활용 팁 5가지'로 대체되었습니다.)*
* *(Instructor Note: Referring to the progress of Python (K-Track), this week 7 has replaced the previous 'Document Tools to Survive Team Project Bombs' special lecture with '5 Computer Proficiency Tips'.)*
- [ ] 학생들에게 Flexbox의 주요 개념(가로정렬, 세로정렬, 간격)의 직관적 이해를 돕는 시각 데모 준비 여부 확인.
- [ ] Check if visual demos are prepared to help students intuitively understand key Flexbox concepts (horizontal alignment, vertical alignment, spacing).
- [ ] 컴퓨터 활용도 실습 대조군을 위해, 바탕화면이 지저분한 상태(혹은 정돈 안 된 예제 파일)를 준비해 둘 것.
- [ ] For the computer proficiency lab control group, ensure a messy desktop state (or disorganized example files) is prepared.
- [ ] **실무 팁 안내**: 단순히 문법을 암기하는 것이 아닌, AI와 함께 문제를 어떻게 해결할 지 강조.
- [ ] **Practical Tip Guidance**: Emphasize how to solve problems together with AI, rather than just memorizing syntax.

---

## 섹션별 상세 시간 배분 및 진행 가이드 / Detailed Time Allocation and Conduction Guide by Section

### [S1] Flexbox 배치 원리 및 전반기 총정리 (15분) / [S1] Flexbox Principles & First Half Review (15 min)
1. **오프닝 및 전반기 리뷰 (5분) / Opening and First-Half Review (5 min)**
   - 1~6주차 동안 배운 HTML 뼈대, CSS 옷 입히기, Box Model 크기 조절의 여정 요약.
   - Summarizing the journey of HTML skeleton, CSS clothing, and Box Model sizing learned during weeks 1~6.
2. **Flexbox의 원리 (10분) / Principles of Flexbox (10 min)**
   - CSS 배치의 마법사 `display: flex` 강연.
   - Lecture on the wizard of CSS alignment, `display: flex`.
   - 가로 정렬(`flex-direction: row`), 수직/수평 가운데 정렬 등의 개념 설명.
   - Explain concepts like horizontal alignment (`flex-direction: row`), vertical/horizontal centering, etc.

### [S2] 메뉴바 정렬 라이브 코딩 및 데모 (15분) / [S2] Menu Bar Alignment Live Coding and Demo (15 min)
1. **메뉴바 수평 정렬 데모 (15분) / Menu Bar Horizontal Alignment Demo (15 min)**
   - `lecture-demo/index.html` 파일을 이용해 1~6주차 배운 태그들을 모두 모은 '포트폴리오' 기초 조립 시연.
   - Demonstrate assembling a basic 'portfolio' combining all tags learned in weeks 1~6 using the `lecture-demo/index.html` file.
   - `<ul>`, `<li>` 에 Flex를 주어 가로 방향의 내비게이션 바로 변환하는 라이브 코딩.
   - Live coding applying Flex to `<ul>` and `<li>` to transform them into a horizontal navigation bar.

### [S3] 레이아웃 리팩터링 (15분) / [S3] Layout Refactoring (15 min)
1. **디버깅 & 리팩터링 라이브 쇼 (15분) / Debugging & Refactoring Live Show (15 min)**
   - 무너진 레이아웃(겹치거나 레이아웃 밖으로 튀어나간 요소)을 개발자 도구를 이용해 원인 파악 및 수정 시연.
   - Demonstrate identifying causes and fixing broken layouts (overlapping or overflowing elements) using Developer Tools.
   - AI(Gemini)에게 잘못된 CSS 코드를 주고 수정 방안을 묻는 디버깅 데모.
   - Debugging demo showing incorrect CSS code to an AI (Gemini) and asking for a fix.

### [S4] [특강] 컴퓨터 활용도 (30분) / [S4] [Special Lecture] Computer Proficiency (30 min)
1. **컴퓨터 활용도 1, 2 (10분) / Computer Proficiency 1, 2 (10 min)**
   - 파일 탐색기 트리 구조, 정렬 및 파악(Search, Don't Sort), 확장자(.exe, .jpg 등 가짜 확장자 구별법) 개념 설명.
   - Explain File Explorer tree structure, sorting and locating (Search, Don't Sort), and how to distinguish fake extensions (like .exe disguised as .jpg).
   - **Win + V (클립보드 히스토리)**: 복사 붙여넣기를 극대화하는 멀티 클립보드 시연.
   - **Win + V (Clipboard History)**: Demonstrate multi-clipboard to maximize copy-pasting.
   - **Win + Shift + S (화면 캡처 마스터)**: 불필요한 전체 화면 캡처가 아닌 지정 영역만 캡처하여 붙여넣는 방법 시연.
   - **Win + Shift + S (Screen Capture Master)**: Demonstrate pasting captured specific areas instead of unnecessary full screens.
2. **컴퓨터 활용도 3 (10분) / Computer Proficiency 3 (10 min)**
   - 대형 모니터가 없을 때의 생존법.
   - Survival methods when you don't have a large monitor.
   - **Win + 방향키**: 화면 절반 나누기로 문서와 코드를 정확히 반반씩 놓고 쓰는 방법 시연.
   - **Win + Arrow Keys**: Demonstrate splitting the screen in half to put documents and code exactly 50/50.
   - **Win + Tab**: 가상 데스크톱을 생성해 작업 공간을 분리하는 방법 설명 및 시연.
   - **Win + Tab**: Explain and demonstrate creating virtual desktops to separate workspaces.
3. **컴퓨터 활용도 4, 5 및 마무리 (10분) / Computer Proficiency 4, 5 and Closing (10 min)**
   - **Ctrl + Shift + Esc (작업 관리자)**: 응답 없는 프로그램을 안전하게 강제 종료(Kill)하는 방법 상황 연출 및 시연.
   - **Ctrl + Shift + Esc (Task Manager)**: Reenact and demonstrate safely force-killing unresponsive programs.
   - **압축 해제의 개념 (Zip)**: 압축 파일 내부에서 그냥 실행 시 경로 오류가 나는 이유를 디렉토리 구조와 연관지어 설명하고 올바른 우클릭 압축 해제 방법 시연.
   - **Concept of Extraction (Zip)**: Explain why running from inside an archive causes path errors linking to directory structures, and demonstrate correct right-click extraction.
   - 다음 주중(8주차) 있을 중간고사 및 대체 평가(타임어택 종합장)에 대한 가벼운 오리엔테이션.
   - Light orientation regarding next week's (Week 8) midterm exam and alternative assessment (Time Attack Comprehensive Project).

---
*(End of Instructor's Note)*
