# 6주차 강의 가이드 (lecture): 박스 모델 및 고급 정보 검색
# Week 6 Lecture Guide: Box Model & Advanced Information Search

**강의명:** 웹프로그래밍(E트랙)
**Course:** Web Programming (E-Track)
**주차:** 6주차
**Week:** Week 6
**강사:** Wonhyuk William Chung
**Instructor:** Wonhyuk William Chung
**이메일:** wonhyukc@stu.ac.kr
**Email:** wonhyukc@stu.ac.kr

## 1. 수업 목표 및 개요
## 1. Class Objectives & Overview

### 1.1. 이번 주 핵심 목표
### 1.1. Key Objectives for This Week
1. CSS 박스 모델(margin, border, padding) 구조를 명확히 이해합니다.
1. Clear understanding of the CSS Box Model structure (margin, border, padding).
2. [Build-up] 기존에 제작한 명함 요소들의 간격을 보기 좋게 조절하고 정돈합니다.
2. [Build-up] Adjust and align the spacing of elements in the previously created digital business card for better aesthetics.
3. 겹친 요소 사이에서 발생하는 마진 상쇄 (Margin Collapsing) 현상을 이해하고 해결 방법을 배웁니다.
3. Understand Margin Collapsing between overlapping elements and learn how to resolve it.
4. **[생존 기본기 훈련]** 구글 렌즈 번역 및 고급 구글링 연산자를 활용한 정보 탐색 능력을 배양합니다.
4. **[Survival Basics Training]** Develop information gathering skills using Google Lens translation and advanced Google search operators.

---

## 2. 블록별 강의 진행 가이드 (총 75분)
## 2. Block-by-Block Lecture Guide (75 Minutes Total)

### **[S1] 순수 이론 강의: 박스 모델 해부학 (25분)**
### **[S1] Pure Theory: Anatomy of the Box Model (25 Mins)**
- **주제:** 요소 주변의 공백 다루기. 박스 모델 기초.
- **Topic:** Managing spacing around elements. Box Model basics.
- **주요 내용:**
- **Main Contents:**
  - 개발자 관점에서의 웹 페이지 요소는 모두 네모난 액자(박스)라는 점을 시각적으로 설명합니다 (액자와 사진 비유).
  - Visually explain that from a developer's perspective, every web page element is a rectangular frame (box) (using the analogy of a picture frame).
  - 테두리(border), 안쪽 여백(padding), 바깥쪽 여백(margin)의 개념과 위치 관계를 설명합니다.
  - Explain the concepts and positional relationships of borders, inner spacing (padding), and outer spacing (margin).
  - StackBlitz에 띄워진 샘플 요소에 border를 주어 눈에 보이게 만들고, margin과 padding 수치를 변경할 때 박스의 위치와 크기가 어떻게 달라지는지 라이브 데모로 보여줍니다.
  - Apply a border to a sample element in StackBlitz to make it visible, and provide a live demo showing how changing margin and padding values affects the box's position and size.

### **[S2] 실습 시연: 요소 정렬 및 개발자 도구 (25분)**
### **[S2] Practical Demo: Element Alignment and Developer Tools (25 Mins)**
- **주제:** 마진과 패딩을 이용해 여백 주도하기.
- **Topic:** Taking control of spacing using margin and padding.
- **주요 내용:**
- **Main Contents:**
  - 패딩(`padding: 10px`)과 마진(`margin: 20px`)의 극명한 차이를 눈으로 보여줍니다.
  - Visually demonstrate the stark difference between padding (`padding: 10px`) and margin (`margin: 20px`).
  - 브라우저의 개발자 도구(F12)를 열어, 'Computed(계산됨)' 탭에 있는 박스 모델 시각화 도구를 보여줌으로써 브라우저가 요소를 어떻게 해석하고 있는지 눈으로 확인하는 방법을 설명합니다.
  - Open the browser's Developer Tools (F12) and use the Box Model visualization under the 'Computed' tab to explain how to visually check how the browser interprets spacing.
  - 여백 요소들의 값을 콘솔에서 바꿔가며 실시간으로 간격이 조절되는 데모를 진행합니다.
  - Perform a demo adjusting margin/padding values via the console to observe real-time spacing changes.

### **[S3] 코드 비평 및 디버깅: 마진 상쇄 및 버그 수정 (25분)**
### **[S3] Code Critique & Debugging: Margin Collapsing and Bug Fixes (25 Mins)**
- **주제:** 실전 레이아웃 오류 원인 분석
- **Topic:** Root cause analysis of practical layout errors.
- **주요 내용:**
- **Main Contents:**
  - 버튼 두 개가 여백 없이 찰싹 붙어 있는 버그 상황을 시연합니다.
  - Demonstrate a bug scenario where two buttons are stuck together with zero spacing.
  - 여유 공간을 주기 위해 학생들과 함께 마진 값을 부여해 보고, 기대한 값과 달라지는 현상(마진 상쇄 문제 등)을 살펴봅니다.
  - Apply a margin value along with students to create space, and observe the phenomenon where it behaves differently than expected (e.g., margin collapsing issue).
  - 이를 해결하기 위한 구체적이고 안전한 CSS 속성 부여 및 라이브 코딩을 통해 수정을 완료합니다.
  - Resolve the issue through live coding by assigning specific, robust CSS properties as a workaround.

---

## 3. 생존 기본기 훈련 가이드 (특강: 정보 사냥꾼)
## 3. Survival Basics Training Guide (Special Lecture: Information Hunter)

이 훈련은 코딩 역량을 넘어선 실전 디지털 생존 능력 강화에 집중합니다. 정규 강의 외 별도 실습 시간 또는 Flipped Learning 세션 시 적극 지도합니다.
This training focuses on strengthening practical digital survival skills beyond coding ability. Continually instruct students during extra lab sessions or Flipped Learning periods.

* **[외국어 장벽 허물기]**: 구글 렌즈(Google Lens)를 활용하여 원서 및 기사를 캡처 혹은 스캔하여 텍스트로 추출합니다. 추출한 텍스트를 크롬에서 복사해, AI 번역 툴(Gemini 등)을 거쳐 자연스러운 한국어 문장으로 바로 교정하는 워크플로우를 반복 연습합니다.
* **[Breaking Down the Language Barrier]**: Use Google Lens to capture or scan foreign textbooks and articles to extract digital text. Copy this text via Chrome, run it through AI translation tools (like Gemini), and correct it into natural Korean sentences. Practice this workflow repeatedly.
* **[정보 쓰레기 걸러내기]**: 구글 검색 연산자를 익힙니다.
* **[Filtering Out Information Trash]**: Master Google Search Operators.
  - 정확한 문장 단위 검색(쌍따옴표 `""`)
  - Exact sentence matching using quotation marks (`""`)
  - 관련 없는 내용 제외하기(빼기 기호 `-`)
  - Excluding irrelevant terms using the minus sign (`-`)
  - 특정 신뢰성 있는 사이트 내 검색(`site:`) 기능을 조합하여 구글링 속도와 퀄리티를 비약적으로 상승시키는 검색 시연을 진행합니다.
  - Conduct a search demo combining the `site:` operator to quickly boost search speed and quality by targeting reliable websites.
  - 무의미한 낚시성 페이지를 육안으로 배제하는 원칙을 지도합니다.
  - Teach the principle of visually identifying and filtering out meaningless clickbait pages.

---

## 4. 실습 및 과제 진행 안내 
## 4. Lab and Assignment Instructions

* **실습 환경:** StackBlitz (클라우드 환경)
* **Lab Environment:** StackBlitz (Cloud IDE)
* **과제 지시 (AI 활용):** AI 파트너(ChatGPT 또는 Gemini)에게 "margin과 padding의 차이를 10살 아이에게 설명해줘"라고 질문합니다. AI가 비유를 들어 설명해 준 부분에 대해 어떻게 생각하는지 짧은 비평안(Critique)을 더하여 이메일 과제로 제출하도록 가이드합니다.
* **Assignment Instructions (AI Usage):** Ask your AI partner (ChatGPT or Gemini), "Explain the difference between margin and padding to a 10-year-old." Add a short critique of its analogy-based explanation, and submit the response as an email assignment.
  - **이메일 제목 형식 (필수):** `과제0.6 학번`
  - **Email Subject Format (Mandatory):** `과제0.6 학번` (Example: 과제0.6 20240001)
