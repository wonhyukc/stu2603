---
marp: true
theme: default
paginate: true
---

# Web Programming: Week 2
# 웹프로그래밍: 2주차

**Topic: HTML Basics**
**주제: HTML 기초**

Wonhyuk William Chung
wonhyukc@stu.ac.kr

---

# Today's Goal
# 오늘 수업의 목표

1. **Understand HTML structure (HTML 문서 구조 이해)**
   - `<h1>`, `<p>`, `<img>`
2. **Build your 1st web page (첫 웹 페이지 조립)**
   - Digital business card skeleton (디지털 명함 뼈대 만들기)
3. **Debugging experience (디버깅 경험)**
   - Finding and fixing missing tags (빠진 태그 찾고 채우기)

---

# [S1] What is HTML?
# [S1] HTML이란 무엇인가?

- **H**yper**T**ext **M**arkup **L**anguage
- The absolute core skeleton of the web
  웹의 가장 핵심적인 뼈대
- A markup language (tags), NOT a logic programming language
  태그로 표시하는 마크업 언어 (복잡한 논리를 짜는 프로그래밍 언어가 아님!)

---

# Human Body Analogy
# 인체에 비유해봅시다

- `<html>`: The entire human! (인간 그 자체)
- `<head>`: The brain (Metadata, invisible secrets). (뇌 - 메타데이터 등 보이지 않는 정보)
- `<body>`: The physical body (What you actually see on screen). (몸통 - 모니터에서 눈으로 보는 모든 것)

---

# StackBlitz Demo
# StackBlitz 데모

- Let's create an empty HTML project in our browser.
  브라우저에서 직접 빈 HTML 프로젝트를 만들어 봅시다.
- Typing `<h1>` and `<p>` in live action.
  `<h1>`과 `<p>` 태그 라이브 코딩 구동 데모.

---

# [S2] Adding Images (The `<img>` tag)
# [S2] 이미지 넣기 (`<img>` 태그)

- The single most important media tag.
  가장 중요한 미디어 태그.
- Wait... this tag has no closing tag! (예외: 닫는 태그가 없습니다!)
- Emphasize the `src` attribute (Source).
  이미지의 출처를 가리키는 `src` 속성 강조.

---

# Debugging the "Broken Image"
# 엑스박스 이미지 디버깅

- Why is my image a broken icon?
  내 이미지는 왜 깨진 아이콘으로 보일까요?
- A typo in the `src` URL causes broken images entirely.
  `src` URL의 단순한 오타 하나가 이미지를 날려 먹습니다.
- Let's fix this live!
  지금 바로 고쳐봅시다!

---

# [S3] Building Your Digital Business Card
# [S3] 디지털 명함 조립하기

- Starting with a broken initial template.
  일부러 망가뜨린 초기 템플릿부터 시작합니다.
- Finding missing `<p>` tags and broken `<img>` links.
  누락된 `<p>` 태그와 연결이 끊어진 `<img>`를 찾아 수정합니다.

---

# Micro-Assignment time!
# 마이크로 과제 시간!

- **AI Prompt:** Ask AI for a digital business card HTML structure.
  **AI 질문표:** AI에게 디지털 명함 뼈대 HTML 작성 요청하기.
- **AI Critique:** Which tag looks good? Which part seems overly complicated?
  **AI 비평:** 어떤 태그가 마음에 드나요? 어디가 불필요하게 복잡해 보이나요?
- **Result:** Delete/Modify at least ONE annoying tag, and show me the final code/screen!
  **최종 결과:** 마음에 안 드는 태그 1개 이상을 직접 삭제하거나 변형하고 결과물 보여주기!
