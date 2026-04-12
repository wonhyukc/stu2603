# Week 1 Handout — Orientation & Intro to the Web
# 1주차 핸드아웃 — 오리엔테이션과 웹 입문

> **Web Programming | Week 1 | Student Reference**
> **웹프로그래밍 | 1주차 | 학생 배포용 참고 자료**
> Use this as a reference during class and for review afterward.
> 수업 중 참고하거나, 수업 후 복습 자료로 활용하세요.

---

## Section 1: Concept Reference / 개념 참고 영역

---

### What This Course Is About / 이 수업이 추구하는 것

| What we do NOT do / 하지 않는 것 | What we DO / 하는 것 |
|:---|:---|
| Memorize HTML tags | **Read and verify** code that AI generates |
| Copy AI output and submit | **Understand** the logic, then complete it with AI as a partner |
| Ask "Why doesn't it work?" | Ask engineer-style questions with **4 required items** |

---

### How the Web Works / 웹이 작동하는 원리

```
You type google.com → Browser sends a REQUEST →
Server finds the HTML file → Server sends a RESPONSE →
Browser RENDERS the HTML file → You see the webpage
```

```
주소창에 google.com 입력 → 브라우저가 요청(REQUEST) 전송 →
서버가 HTML 파일 탐색 → 서버가 응답(RESPONSE) 전송 →
브라우저가 HTML 렌더링 → 화면에 웹 페이지 표시
```

- **HTML** = Structure / 구조 (what content exists and what type it is)
- **CSS** = Style / 스타일 (how it looks — colors, fonts, spacing)
- **JavaScript** = Behavior / 동작 (interactivity — buttons, animations, logic)

---

### Brief Web History / 웹의 짧은 역사

| Year / 연도 | Event / 사건 |
|:---|:---|
| **1989** | Tim Berners-Lee proposes the World Wide Web at CERN |
| **1991** | First public website goes live |
| **1994** | W3C (web standards body) founded |
| **1995** | JavaScript created (Netscape, 10 days) |
| **2004** | Web 2.0 era — users create content (YouTube, Facebook) |
| **2015+** | Responsive design, mobile-first, progressive web apps |
| **2023+** | AI-assisted coding becomes mainstream |

---

### Course Methodology — Flipped Learning / 수업 방식

```
Before class     →  Watch eCampus lecture video (집/이동 중)
In class         →  Hands-on practice + Q&A + AI discussion (교실)
After class      →  Submit Micro-Assignment (다음 수업 전날 23:59)
```

> If you come to class without watching the video, you will struggle to follow the exercises.
> 영상을 보지 않고 수업에 오면 실습을 따라가기 어렵습니다.

---

### Semester Roadmap / 한 학기 로드맵

| Period / 기간 | Content / 내용 | Environment / 환경 |
|:---|:---|:---|
| Weeks 1–8 | HTML & CSS Fundamentals | **StackBlitz** (cloud IDE, no install) |
| Week 8 | Midterm — code reading + bug fixing (open-book) | — |
| Weeks 9–14 | JavaScript + Dynamic Pages | **VS Code + Live Server** (local) |
| Week 15 | Final — project demo + code logic explanation | — |

---

### Business Email 5 Principles / 비즈니스 이메일 5원칙

| # | Principle / 원칙 | Key Rule / 핵심 |
|:---|:---|:---|
| 1 | **Bottom Line Up Front (두괄식)** | Main point goes in the **first sentence** |
| 2 | **Specific Subject Line / 구체적인 제목** | `[Student ID Name] Content` format |
| 3 | **Attach First / 첨부 파일 먼저** | Add attachments before writing body |
| 4 | **Distinguish To / CC / 수신자 구분** | To = must reply, CC = needs to know |
| 5 | **Reply Within 24 Hours / 24시간 이내 답변** | If unresolved, send "Received" first |

**Bad subject / 나쁜 제목**: `Hello` / `안녕하세요`
**Good subject / 좋은 제목**: `[20251234 Gil-dong Hong] Week 1 Assignment Deadline Inquiry`

---

### Engineer-Style Questioning / 엔지니어식 질문법 (4 items required / 4항목 필수)

When stuck, include all four items. "It doesn't work" is not a question.
막혔을 때 아래 4가지를 **반드시 포함**합니다. "이거 왜 안 돼요?"는 답변 불가입니다.

```
1. Situation   → What were you trying to do?
2. What tried  → What steps did you take?
3. Error msg   → Paste the exact error text (full copy)
4. AI result   → Did you ask the AI? What did it say?
```

```
1. 발생 상황    → 무엇을 하려고 했는가
2. 시도해본 것  → 어떻게 해봤는가
3. 에러 메시지  → 정확히 어떤 내용이 나왔는가 (전문 복사)
4. AI 질문 결과 → AI에게 먼저 물어봤는가, 결과는 어떠했는가
```

---

### AI Collaboration Principles / AI 활용 원칙

**Wrong approach / 잘못된 방법**:
"Build me a webpage with a nav bar" → Copy → Submit

**Right approach / 올바른 방법**:
"I'm learning HTML. Can you explain what the `<nav>` tag does and why it's better than just using `<div>`?" → Understand → Apply → Verify → Submit

> **Problem-solving partner**: When stuck or encountering errors, actively use AI for hints and solutions rather than struggling alone.
> **문제 해결 파트너**: 과제가 어렵거나 에러가 생기면 혼자 오래 고민하지 말고 **적극적으로 AI를 활용해 힌트와 해결책을 찾아보세요.**
> But AI makes mistakes — never trust code you haven't tested in a browser yourself.
> 단, AI는 틀릴 수 있으니 브라우저에서 실행해서 확인하지 않은 코드는 믿지 마세요.

---

### Micro-Assignment Format / 마이크로 과제 형식 (Starting Week 2 / 2주차부터 적용)

| Item / 항목 | Content / 내용 |
|:---|:---|
| **AI Prompt** | The core question you posed to the AI this week / AI에게 던진 핵심 질문 |
| **AI Critique** | One sentence: what AI got right vs. wrong / AI 답변의 맞는 부분 / 틀리거나 위험한 부분 (한 문장) |
| **Final Result** | Code or conclusion you verified and modified yourself / 내가 검증·수정한 최종 코드 또는 결론 |

Length / 분량: **~0.5 pages A4** | Submit via / 제출: eCampus submission box

---

### Today's Checklist / 오늘 해야 할 일

- [ ] Open StackBlitz, create HTML project, type first `<h1>` tag and see live preview
- [ ] Create GitHub account + set up private assignment repository
- [ ] Invite instructor (`wonhyukc`) as Collaborator
- [ ] Verify this course appears in your eCampus enrollment list
- [ ] Create ChatGPT or Google Gemini account
- [ ] Ask AI: "What is HTML?" — read the response critically

---

## Section 2: Lab / 실습 섹션 — Orientation & Intro to the Web

> **Step-by-step in-class exercises. Follow along with the instructor's screen.**
> **수업 중 학생이 직접 실행하는 단계별 실습입니다. 강사의 화면을 보면서 순서대로 따라 해주세요.**
> - Total time / 총 시간: **75 min**
> - Environment / 실습 환경: Any browser (Chrome recommended) / 브라우저 (Chrome 권장)

---

### Lab 1. StackBlitz — First HTML Tag / 첫 HTML 태그 체험 (25 min)

StackBlitz is a cloud-based code editor you access entirely in your browser. No downloads, no installation — you can start coding immediately.
StackBlitz는 브라우저에서 바로 접근하는 클라우드 코드 에디터입니다. 다운로드나 설치 없이 즉시 코딩을 시작할 수 있습니다.

**Step 1: Open StackBlitz**
- Type `stackblitz.com` in your browser address bar and press Enter.
  브라우저 주소창에 `stackblitz.com`을 입력하고 Enter를 누릅니다.
- Click **"Start a new project"** → choose **"Static"** template.
  **"Start a new project"** 클릭 → **"Static"** 템플릿 선택.

**Step 2: Explore the Interface**
- Left panel: file tree (you will see `index.html`)
  왼쪽 패널: 파일 트리 (`index.html` 파일 확인)
- Center: code editor
  가운데: 코드 에디터
- Right: live browser preview — updates as you type
  오른쪽: 라이브 미리보기 — 타이핑하는 순간 업데이트

**Step 3: Type Your First Tag**
- Click on `index.html` in the file tree.
  파일 트리에서 `index.html`을 클릭합니다.
- Find the `<body>` section and type the following inside it (type it, don't paste):
  `<body>` 섹션을 찾고 그 안에 다음을 직접 타이핑합니다 (복사-붙여넣기 말고 직접 타이핑):

  ```html
  <h1>Hello, Web!</h1>
  ```

- Watch the right panel — your text should appear instantly as a large heading.
  오른쪽 패널을 보세요 — 텍스트가 즉시 큰 제목으로 나타나야 합니다.

**Step 4: Try One More**
- On the next line, type:
  다음 줄에 입력합니다:

  ```html
  <p>My name is [your name].</p>
  ```

- Replace `[your name]` with your actual name.
  `[your name]` 자리에 본인 이름을 씁니다.

**Step 5: Copy the Project URL**
- Look at the browser address bar at the top. Copy the full URL of your StackBlitz project.
  브라우저 주소창을 확인하세요. StackBlitz 프로젝트의 전체 URL을 복사해둡니다.
- You will need this URL for Assignment B.
  과제 B에서 필요합니다.

> **Checkpoint**: Two lines of content appear in the preview. Lab 1 complete.
> **확인 사항**: 미리보기에 두 줄의 내용이 나타나면 Lab 1 완료입니다.

---

### Lab 2. GitHub Account & Repository Setup / GitHub 계정 및 저장소 세팅 (25 min)

GitHub is where your code lives this semester. It is also your professional portfolio — keep it clean and use your real name.
GitHub는 이번 학기에 여러분의 코드가 살아있는 곳입니다. 동시에 전문 포트폴리오이기도 합니다 — 깔끔하게 유지하고 실명을 사용하세요.

**Step 1: Create a GitHub Account**
- Go to `github.com` → click **"Sign up"** in the top-right.
  `github.com` 접속 → 오른쪽 상단 **"Sign up"** 클릭.
- Enter your email, create a password, and choose a username. Use a professional format (e.g., `gil-dong-hong` or `gildonghong`).
  이메일, 비밀번호를 입력하고 아이디(username) 선택. 전문적인 형식 권장 (예: `gil-dong-hong`).
- In Settings, update your display name to your real name.
  Settings에서 표시 이름을 본명으로 업데이트합니다.
- Email verification may take a few minutes. If it is delayed, continue to the next step and complete it later.
  이메일 인증이 몇 분 걸릴 수 있습니다. 지연되면 다음 단계를 진행하고 나중에 완료하세요.

**Step 2: Create an Assignment Repository**
- Click the **"+"** button in the top-right → **"New repository"**.
  오른쪽 상단 **"+"** 클릭 → **"New repository"**.
- Repository name: `web-assignments` (or any name you choose).
  저장소 이름: `web-assignments` (또는 자유 이름).
- Visibility: **Private** (other students cannot see your code).
  공개 여부: **Private** (다른 학생이 내 코드를 볼 수 없습니다).
- Check **"Add a README file"**.
  **"Add a README file"** 체크.
- Click **"Create repository"**.
  **"Create repository"** 클릭.

**Step 3: Invite the Instructor as Collaborator**
- In your new repository, click the **"Settings"** tab.
  저장소 화면에서 **"Settings"** 탭 클릭.
- In the left sidebar, click **"Collaborators"** → **"Add people"**.
  왼쪽 메뉴에서 **"Collaborators"** → **"Add people"** 클릭.
- Search for instructor ID **`wonhyukc`** (or email `wonhyukc@stu.ac.kr`) → click the result → **"Add to this repository"**.
  강사 아이디 **`wonhyukc`** (또는 이메일 `wonhyukc@stu.ac.kr`) 검색 → 클릭 → **"Add to this repository"** 클릭.
- Once the instructor accepts, grading is possible.
  강사가 초대를 수락하면 채점이 가능해집니다.

> **Checkpoint**: Note your repository URL (e.g., `github.com/your-id/web-assignments`).
> **확인 사항**: 저장소 주소창 URL(예: `github.com/내아이디/저장소이름`)을 기억해둡니다.

---

### Lab 3. eCampus Check + AI Account / eCampus 확인 + AI 계정 생성 (25 min)

**Step 1: Verify eCampus Enrollment**
- Log in to eCampus.
  eCampus에 접속합니다.
- Check that **Web Programming** (웹프로그래밍) appears in your enrolled courses.
  수강 중인 과목 목록에 **웹프로그래밍** 과목이 있는지 확인합니다.
- If it does not appear, notify the instructor immediately.
  없다면 강사에게 즉시 알립니다.
- If it does appear, navigate to the Week 1 materials tab.
  있다면 1주차 강의 자료 탭을 확인합니다.

**Step 2: Set Up an AI Account**

Choose one of the following. Both are free and sufficient for this course.
아래 중 하나를 선택합니다. 둘 다 무료이며 이 수업에 충분합니다.

| AI Tool | URL | Notes |
|:---|:---|:---|
| **ChatGPT** (recommended) | `chat.openai.com` | Most widely used, strong for code explanations |
| **Google Gemini** | `gemini.google.com` | Login with Google account, no extra sign-up |

You may use both, or try others (Claude at `claude.ai`, Perplexity at `perplexity.ai`). At minimum, have one ready today.
둘 다 사용하거나 다른 것을 써도 됩니다 (Claude: `claude.ai`, Perplexity: `perplexity.ai`). 최소 하나는 오늘 준비해야 합니다.

**Step 3: First AI Conversation**

After creating your account, type this question exactly:
계정 생성 후 아래 질문을 입력합니다:

```
What is HTML? I'm a first-year university student with no coding background. Explain it simply.
```

Read the response. In your head, note what made sense and what was confusing.
응답을 읽습니다. 이해된 부분과 이해가 안 된 부분을 머릿속으로 체크합니다.

**Step 4: Push Back on the AI**

Now ask this follow-up:
이번에는 이 질문을 합니다:

```
In your previous answer, is there anything that might be wrong, outdated, or oversimplified? Be honest.
```

See how the AI responds. Does it defend itself or admit limitations?
AI가 어떻게 대답하는지 봅니다. 자신을 방어하나요, 아니면 한계를 인정하나요?

> **Checkpoint**: If the AI says "everything I said is correct," treat that answer with extra skepticism.
> **체크포인트**: AI가 "제가 말한 모든 것이 맞습니다"라고 하면 그 AI를 더 조심해야 합니다.

---

### Today's Lab Completion Checklist / 오늘 실습 완료 체크리스트

| Item / 항목 | Done / 완료 |
|:---|:---|
| StackBlitz HTML project created + `<h1>` and `<p>` tags typed + URL copied | |
| GitHub account created + private repo created | |
| Instructor `wonhyukc` invited as Collaborator | |
| eCampus enrollment confirmed for this course | |
| AI account (ChatGPT or Gemini) created and logged in | |
| Asked AI "What is HTML?" and read the response | |

Keep the StackBlitz URL handy. You will need it for Assignment B.
StackBlitz URL을 기억해두세요. 과제 B에서 필요합니다.

---

## Section 3: Assignment / 과제 섹션 — Micro-Assignment

> **Submission / 제출**: eCampus → Week 1 submission box
> **Deadline / 제출 기한**: 23:59 the day before the next class / 다음 수업 전날 23:59
> **Length / 분량**: ~0.5 pages A4

---

### Assignment A: Self-Introduction Email to the Instructor

Apply the Business Email 5 Principles to send a self-introduction email to the instructor.
비즈니스 이메일 5원칙에 따라 강사에게 자기소개 이메일을 보냅니다.

**To / 수신**: wonhyukc@stu.ac.kr

**Required Content / 이메일에 반드시 포함해야 할 내용**

| Item / 항목 | Content / 내용 |
|:---|:---|
| Subject / 제목 | `[Student ID Name] Self-Introduction Email` — e.g., `[20251234 Gil-dong Hong] Self-Introduction Email` |
| Greeting / 인사 | Short greeting to the recipient |
| First sentence / 본문 첫 문장 | "I am writing to introduce myself." (Bottom Line Up Front) |
| Body / 자기소개 | Your name, student ID, and one sentence about what you hope to learn from this course |
| Closing / 끝맺음 | Your name + affiliation |

**Checklist (verify before sending / 전송 전 확인)**
- [ ] Did you add any attachment before writing the body? (Use Drive links if needed)
      첨부 파일이 필요한 경우 내용을 쓰기 전에 먼저 추가했는가?
- [ ] Does the subject line alone communicate the purpose?
      제목만 읽어도 내용을 알 수 있는가?
- [ ] Does the opening include a brief greeting to the instructor?
      본문 앞부분에 수신자에게 짧은 인사가 있는가?
- [ ] Is the main point stated in the first sentence? (Bottom line up front)
      본문 첫 문장에 요점이 바로 등장하는가?
- [ ] Did you spell-check before sending?
      전송 전에 맞춤법·문법 오류를 확인했는가?
- [ ] Is the instructor's email (`wonhyukc@stu.ac.kr`) correctly entered in the To field? (Add To last)
      To(받는 사람)에 강사 이메일(`wonhyukc@stu.ac.kr`)이 정확히 입력됐는가? (To는 가장 마지막에 작성)

---

### Assignment B: Account Setup Verification via GitHub

Instead of uploading screenshots to eCampus, use the GitHub repository you created in Lab 2.
이미지를 eCampus에 업로드하는 대신, Lab 2에서 만든 GitHub 저장소를 활용합니다.

**Step 1: Create `week01.md` in Your Repository**
- Go to your assignment repository (e.g., `github.com/your-id/web-assignments`).
  과제 저장소에 들어갑니다.
- Click **"Add file"** → **"Create new file"**.
  **"Add file"** → **"Create new file"** 클릭.
- Enter `week01.md` as the file name.
  파일 이름 칸에 `week01.md` 입력.
- In the body, include the following three items:
  본문에 아래 세 가지를 포함합니다:
  1. The URL of your StackBlitz project from Lab 1 (make sure the project is accessible via link)
     Lab 1에서 만든 StackBlitz 프로젝트 URL (링크 공유 가능하게 설정 확인)
  2. Your GitHub profile URL
     내 GitHub 프로필 URL
  3. The full text of your AI conversation where you asked "What is HTML?" (or a share link if the AI supports it)
     AI에게 "HTML이 뭐야?"를 물어본 대화 텍스트 전문 (또는 AI 공유 링크)
- Click **"Commit changes..."** to save. (Commit message: `Create week01.md`)
  하단 **"Commit changes..."** 클릭하여 저장. (커밋 메시지: `Create week01.md`)

**Step 2: Submit for Peer Evaluation / 사설 평가 시스템 제출 및 상호평가 준비**
- Open the `week01.md` file you just created and copy the **full URL from the browser address bar**.
  방금 만든 `week01.md` 파일 화면의 **브라우저 주소창 전체 URL**을 복사합니다.
- Copy the **commit hash** of your latest change to the repository.
  저장소에 반영된 최신 **커밋 해시값(hash)**도 복사합니다.
- In the eCampus Week 1 submission board, **paste the URL and the hash and submit**.
  eCampus 1주차 과제 게시판 텍스트 입력란에 **해당 URL과 해시값을 붙여넣고 제출**합니다.
  - **Deadline:** Submit before 23:59 the day before the next class.
    **제출 기한:** 다음 수업 전날 23:59까지

**Step 3: Conduct Peer Evaluation / 동료 상호평가 수행**
- **Period / 평가 기간**: The day of the next class ~ for 48 hours / 다음 수업 당일 0:00부터 48시간 동안
- After the submission deadline, the instructor will announce a **Peer Evaluation Matching Table** and a **Google Form Link for Grading**.
  제출 마감 이후, 교수님이 **'상호평가 대상자 매칭표'**와 **'채점용 구글 폼 링크'**를 공지합니다.
- Check the table, open the `week01.md` links of the 3 peers assigned to you.
  매칭표를 확인하여 자신에게 배정된 동료 학생 3명의 `week01.md` 링크를 엽니다.
- Review their repository setup and submit your grading scores via the provided Google Form based on the rubric (3 points: O/X).
  저장소 세팅을 확인한 후, 채점용 구글 폼에 접속하여 루브릭(O/X 3점 기준)에 따라 점수를 입력하고 제출합니다.
- **Warning:** You must complete the evaluations for all 3 assigned peers to receive your own participation points.
  **주의:** 지정된 세 명의 친구 과제를 기한 내에 구글 폼으로 모두 채점해야만 본인의 채점(참여) 점수를 받을 수 있습니다.

---

### Assignment C: Web History Experience / 과제 C: 웹의 역사 체험

Visit the first website in history and experience the evolution of the web, then write your impressions.
역사상 최초의 웹사이트를 방문하고 웹의 진화 과정을 체험한 후 소감을 작성합니다.

**Step 1: Visit the First Website / 최초의 웹사이트 방문**
- Go to [info.cern.ch](https://info.cern.ch/).
  최초의 웹사이트인 [info.cern.ch](https://info.cern.ch/)에 접속합니다.
- Browse the simple text and hyperlinks.
  텍스트와 하이퍼링크만 있는 단순한 구조를 살펴봅니다.

**Step 2: Experience Web History / 웹 역사 체험**
- Go to [Web Rewind](https://www.web-rewind.com/?utm_source=opcom&utm_medium=internal&utm_campaign=web-rewind&utm_content=homepage-banner).
  [Web Rewind](https://www.web-rewind.com/?utm_source=opcom&utm_medium=internal&utm_campaign=web-rewind&utm_content=homepage-banner)에 접속합니다.
- Look around to see how web design and technology have evolved.
  과거부터 현재까지 웹 디자인과 기술이 어떻게 변해왔는지 살펴봅니다.

**Step 3: Write Your Impressions / 소감 작성**
- In your `week01.md` file from Assignment B, add a new section for Assignment C at the bottom.
  과제 B에서 만든 `week01.md` 파일 하단에 과제 C 섹션을 추가합니다.
- Write a short paragraph (3-4 sentences) about how the web has changed and what you felt.
  과거 웹과 현재 웹의 차이점, 느낀 점 등 짧은 소감(3~4문장)을 작성하여 추가합니다.

---

### Grading Notes & Tips / 평가 기준 및 팁

- If the instructor account (`wonhyukc`) is not invited as a Collaborator, the Private repository is inaccessible → **0 points**. (Recheck Lab 2)
  강사 계정(`wonhyukc`)이 초대되지 않으면 Private 저장소 접근 불가 → **0점** 처리됩니다. (Lab 2 재확인)
- Submissions after the deadline (23:59 the day before the next class) are treated as **not submitted**.
  제출 기한(수업 전날 23:59) 이후 제출은 **미제출** 처리됩니다.

---

> **Instructor note**: Week 1 does not apply the standard Micro-Assignment format (AI Prompt / AI Critique / Final Result). Account setup and business email practice are the primary objectives. The standard three-item format begins from Week 2.
> **강사 메모**: 1주차는 마이크로 과제 표준 형식(AI Prompt / AI Critique / Final Result)을 적용하지 않습니다. 계정 생성과 비즈니스 이메일 실습이 주 목적입니다. 2주차부터 표준 형식을 적용합니다.

---

## Next Week Preview / 다음 주(2주차) 예고

Topic / 주제: **HTML Basics — Building an Online Business Card**
`<h1>`, `<p>`, `<img>` tags | Finding and fixing missing tags

> Watch the **wb02 lecture video on eCampus** before class. / 수업 전에 eCampus에서 **wb02 강의 영상**을 반드시 시청해 오세요.

---

## Appendix: Cross-Platform Compatibility Issues (macOS vs. Windows)

**1. Broken Filenames (NFD vs. NFC Normalization)**
macOS typically uses the **NFD (Normalization Form Canonical Decomposition)** method for handling Unicode, which separates characters into base letters and combining marks (e.g., separating Korean characters into distinct consonants and vowels). Windows, however, uses the **NFC (Normalization Form Canonical Composition)** method, storing characters as a single, precomposed block. Consequently, when a file created on a Mac is moved to a Windows system, the filename may render improperly, appearing as separated phonetic components.

**2. Broken Text Content (UTF-8 vs. ANSI / Windows-1252)**
Modern macOS and Linux environments, along with most of the web, default to **UTF-8**, a comprehensive global standard for character encoding. Conversely, legacy Windows applications (like Notepad on older systems) often rely on limited system-specific encodings such as **Windows-1252 (ANSI)** in Western regions or **CP949 (EUC-KR)** in Korea. If a UTF-8 encoded document created on a Mac is opened in a Windows editor expecting ANSI or CP949, the bytes are misinterpreted, resulting in garbled text or "gibberish."

**3. Line Endings Mismatch (CRLF vs. LF)**
Different operating systems record the action of advancing to a new line differently, a holdover from the era of mechanical typewriters. Windows systems use a two-character sequence, **CRLF (`\r\n`)**—Carriage Return followed by Line Feed. In contrast, Unix-based systems like macOS and Linux use a single character, **LF (`\n`)**. Due to this difference, code written on a Mac may appear as a single, unbroken line when opened in older Windows text editors, while files created on Windows may display unexpected hidden characters (like `^M`) at the end of each line when executed in Mac or Linux terminal environments, potentially causing script errors.

* https://www.revk.uk/2022/02/crlf-has-long-history.html
* https://youtu.be/-qH3XO9nKtk?si=hbqZsBGUE5qHsqvw


