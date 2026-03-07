---
marp: true
theme: default
---

# wb01 Slides — Orientation & Intro to the Web
# wb01 슬라이드 개요 — 오리엔테이션과 웹 입문

> **Instructor PPT reference document. / 강사용 PPT 제작 기준 문서입니다.**
> Each slide defines the title and key bullets. Visual assets are marked with `[IMAGE]`.
> 각 슬라이드의 제목과 핵심 bullet을 정의합니다. 시각 자료는 `[이미지]` 태그로 표시합니다.
> Total slides: **21** | Total lecture time: 75 min (25 min × 3 sections)
> 총 슬라이드: **21장** | 총 강의 시간: 75분 (25분 × 3섹션)

---

## Section 1 — The Web & Course Introduction / 웹 입문과 강의 소개 (25 min, Slides 1–9)

---

### Slide 1 — Cover / 표지

**Title**: Web Programming
**Subtitle**: Week 1: Orientation & Intro to the Web
**Bottom**: Wonhyuk William Chung (정원혁) | Seoul Theological University

---

### Slide 2 — Honest Question / 솔직한 질문

**Title**: Why are you here? / 여기 왜 왔나요?

- "I heard web skills lead to good jobs."
- "It's a required course."
- "I think I need to learn to code."

> **Instructor note**: "All valid reasons — but this course tells a slightly different story."
> **강사 멘트**: "그 이유, 다 괜찮습니다. 그런데 이 수업에서는 조금 다른 이야기를 합니다."

---

### Slide 3 — What Is the Web? / 웹이 뭘까요?

**Title**: Internet ≠ Web / 인터넷 ≠ 웹

- **Internet** = global network (highway) / 전 세계 컴퓨터를 연결하는 네트워크 (고속도로)
- **Web** = one service on the internet (delivery trucks on the highway) / 인터넷 위에서 작동하는 서비스 (고속도로 위의 트럭)
- Created by **Tim Berners-Lee** at CERN, 1989

`[IMAGE: Simple diagram — client → request → server → response → browser renders]`

---

### Slide 4 — Brief Web History Timeline / 웹 역사 타임라인

**Title**: 30 Years in 30 Seconds / 30년을 30초에

| Year | Event |
|:---

### Slide 5 — The Client-Server Model / 클라이언트-서버 모델

**Title**: How a Webpage Reaches You / 웹 페이지가 화면에 나타나기까지

```
You type URL → Browser sends REQUEST →
Server finds HTML file → Server sends RESPONSE →
Browser RENDERS HTML → You see the page
```

> Three languages of the web: **HTML** (structure) · **CSS** (style) · **JS** (behavior)
> 웹의 세 언어: **HTML**(구조) · **CSS**(스타일) · **JS**(동작)

---

### Slide 6 — AI in 2025 / AI 시대의 현실

**Title**: AI writes code. So why are we here? / AI가 코드를 씁니다. 그러면 왜 배워야 할까요?

- Ask ChatGPT "Build me a webpage" → working code in 5 seconds
- But **AI confidently produces wrong code**
- If you can't read it → you submit the bug

| Role disappearing / 사라지는 역할 | Role surviving / 살아남는 역할 |
|:---|:---|
| Typing code into a file | **Judging** what to build |
| Memorizing syntax | **Verifying** what AI produced |

---

---|:---|
| 1989 | Tim Berners-Lee proposes the web |
| 1991 | First public website |
| 1995 | JavaScript invented (10 days!) |
| 2004 | Web 2.0 — user-generated content |
| 2015+ | Mobile-first, responsive design |
| 2023+ | AI-assisted coding goes mainstream |

`[IMAGE: timeline graphic]`

---

### Slide 7 — Flipped Learning / 거꾸로 수업

**Title**: Flipped Learning (거꾸로 수업)

```
Traditional:   Classroom → Lecture  /  Home → Homework
Flipped:       Home → Watch video   /  Classroom → Hands-on + Q&A
```

- Every week: lecture video uploaded to eCampus by 18:00 the day before class
  매주: 수업 전날 18:00까지 eCampus 영상 업로드
- **Must watch before attending class** / **수업 전 반드시 시청**

---

### Slide 8 — Semester Roadmap / 한 학기 로드맵

**Title**: Where We're Going / 우리가 가는 길

| Period | Content | Environment |
|:---|:---|:---|
| Weeks 1–8 | HTML & CSS Basics | **StackBlitz** (cloud) |
| Week 8 | Midterm — open-book bug fixing | — |
| Weeks 9–14 | JavaScript + Dynamic Pages | **VS Code + Live Server** |
| Week 15 | Final — project demo + logic explanation | — |

---

## Section 2 — Professional Communication / 프로페셔널 커뮤니케이션 (25 min, Slides 10–15)

---

### Slide 9 — First Assignment Is an Email / 첫 과제는 이메일

**Title**: This week's assignment: Send me an email / 이번 주 과제: 강사에게 이메일 보내기

- Not a coding assignment
- **Business email** done correctly is the first assignment
- Why: web developers communicate, not just code

> "Poor email habits signal unprofessionalism even when the code is excellent."
> "이메일을 못 쓰면 아무리 코딩을 잘해도 팀에서 신뢰를 잃습니다."

---

### Slide 10 — Bad vs. Good Email / 나쁜 이메일 vs. 좋은 이메일

**Title**: Bottom Line Up Front / 두괄식이란?

**Bad**:
> "Hello. I'm a first-year student… the weather has been cold… could I possibly find out the deadline?"

**Good**:
> "Hello, Professor Chung. I'm writing to confirm the Week 1 assignment deadline. — Gil-dong Hong"

> **Rule**: Main point in the **first sentence** / 하고 싶은 말을 **첫 문장**에

---

### Slide 11 — Business Email 5 Principles / 비즈니스 이메일 5원칙

**Title**: Communication standards for this entire semester / 이번 학기 내내 쓸 소통 규칙

1. **Bottom Line Up Front** — main point first
2. **Specific subject** — `[Student ID Name] Content`
3. **Attach first** — before writing the body
4. **To / CC distinction** — To = must reply
5. **Reply within 24 hours** — even just "Received"

---

### Slide 12 — Engineer-Style Questioning / 엔지니어식 질문법

**Title**: "It doesn't work" is not a question / "이거 왜 안 돼요?"는 답할 수 없습니다

**4 required items / 좋은 질문 4항목**:

1. **Situation** — what were you trying to do?
2. **What you tried** — what steps did you take?
3. **Full error message** — paste exact text
4. **AI result** — what did you ask AI? What did it say?

> "Forming this question often leads you to solve it yourself."
> "이렇게 질문하다 보면 스스로 해결하는 경우가 많습니다."

---

### Slide 13 — eCampus Usage / eCampus 사용법

**Title**: Everything goes on eCampus / 모든 공지는 eCampus에서

| Task | How |
|:---|:---|
| Watch lecture video | eCampus → Week N materials |
| Check announcements | eCampus → Announcements |
| Submit assignments | eCampus → Week N submission box |

> "No KakaoTalk or text message notifications. 'I didn't know' is not an excuse."
> "카카오톡·문자 공지 없습니다. 'eCampus 몰랐어요'는 이유가 되지 않습니다."

---

### Slide 14 — Section 2 Summary / Section 2 요약

**Title**: Professional Communication Core / 프로페셔널 커뮤니케이션 핵심

- Business email 5 principles → **see handout**
- Engineer-style questioning 4 items → **applies all semester**
- Email subject for Assignment A: `[Student ID Name] Self-Introduction Email`

---

## Section 3 — AI Partner & Developer Tools / AI 파트너와 개발 도구 (25 min, Slides 16–21)

---

### Slide 15 — StackBlitz

**Title**: Your code environment for Weeks 1–8 / 1~8주차 실습 환경

- No installation required — runs in any browser
- Create HTML project → code editor + **live preview** updates as you type
- Today: open `stackblitz.com` and type your first `<h1>` tag

`[IMAGE: StackBlitz interface screenshot — file tree, editor, live preview]`

---

### Slide 16 — GitHub

**Title**: Your code portfolio / 코드 포트폴리오 공간

- Every piece of code this semester lives on GitHub
- Create a **private repository** + invite instructor as Collaborator
- Employer & graduate school tip: a clean GitHub profile matters

> "If I'm not invited as a Collaborator, I cannot see your private repository → 0 points."
> "강사가 초대되지 않으면 Private 저장소 접근 불가 → 0점"

---

### Slide 17 — AI Tools: Choose One Today / AI 도구 선택

**Title**: Pick your AI partner today / 오늘 AI 파트너를 선택하세요

| | **ChatGPT** | **Google Gemini** |
|:---|:---|:---|
| Provider | OpenAI | Google |
| Free tier | Yes | Yes |
| Best for | Code Q&A | Google account integration |

> You may use both, or try others. Have at least one ready today.
> 둘 다 써도 됩니다. 최소 하나는 오늘 준비하세요.

---

### Slide 18 — How to Use AI / AI를 어떻게 쓰는가

**Title**: Partner vs. vending machine / 파트너로 쓸 것인가, 자판기로 쓸 것인가

**Wrong / 잘못된 방법**:
> "Write me an `<img>` tag." → Copy → Submit

**Right / 올바른 방법**:
> "I'm learning HTML for the first time. Explain what `src` and `alt` in `<img>` do and why browsers need `alt` text." → Understand → Apply

`[IMAGE: two prompts side by side for comparison]`

---

### Slide 19 — AI Makes Mistakes / AI는 틀립니다

**Title**: Trust AI, but verify / AI를 믿되, 직접 확인하세요

- Invents attributes that don't exist / 존재하지 않는 속성을 만들어냅니다
- Gives code that breaks in certain browsers / 특정 브라우저에서 깨지는 코드를 줍니다
- Describes outdated practices as current / 구식 방법을 최신이라고 설명합니다
- Says "this works" — but it doesn't / "이렇게 하면 됩니다" — 실제로는 안 됩니다

> **Rule**: Any AI-generated code must be tested in a browser before submitting.
> **원칙**: AI가 준 코드는 반드시 브라우저에서 테스트한 후 제출합니다.

---

### Slide 20 — This Week + Next Week / 이번 주 + 다음 주

**Title**: Today's summary & what comes next / 오늘 정리 + 다음 주 예고

**Today in class / 오늘 수업에서 한 것**:
- Understood how the web works (client-server model)
  웹 작동 원리 이해 (클라이언트-서버 모델)
- Business email 5 principles + engineer-style questioning
  비즈니스 이메일 5원칙 + 엔지니어식 질문법
- StackBlitz + GitHub + AI tool setup
  StackBlitz + GitHub + AI 도구 계정 설정

**This week's assignments (due 23:59 the day before next class)**:
- Assignment A: Self-introduction email to instructor
- Assignment B: `week01.md` on GitHub with 3 verification items → paste URL on eCampus

**Next week (wb02)**: HTML Basics — building an "Online Business Card" with `<h1>`, `<p>`, `<img>`
**다음 주(wb02)**: HTML 기초 — `<h1>`, `<p>`, `<img>`로 '온라인 명함' 만들기

> Watch the **wb02 video on eCampus** before next class.
> 다음 수업 전에 eCampus에서 **wb02 강의 영상**을 반드시 시청해 오세요.

---

*Total slides: 21 | Section 1: 9 / Section 2: 6 / Section 3: 6*
*총 슬라이드: 21장 | 섹션 1: 9장 / 섹션 2: 6장 / 섹션 3: 6장*
