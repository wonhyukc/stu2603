# [Week 1] Lab: Environment Setup & Your First Web View
# [1주차] 실습: 환경 구축 및 첫 번째 웹 뷰어

---

## 👋 Welcome to Web Programming (E-Track)! 
## 👋 웹프로그래밍(E트랙)에 오신 것을 환영합니다!

Before we start our hands-on session, remember our **AI-Native Mindset**: 
실습을 시작하기 전에, 우리 수업의 **AI-Native 정신**을 기억해 주세요:

1. **AI is your Co-pilot**: Use it to explore, not just copy. 
   (AI는 여러분의 부조종사입니다: 따라만 쓰지 말고 탐구하는 데 활용하세요.)
2. **Understand the Structure**: Focus on 'Why' and 'How', not 'What to memorize'.
   (구조를 이해하세요: '무엇을 외울까'가 아니라 '왜/어떻게'에 집중하세요.)
3. **Professional Questioning**: When you get stuck, follow the **"Engineer-style Questioning"** rule.
   (프로페셔널하게 질문하기: 막혔을 때는 **"엔지니어식 질문법"**을 따르세요.)

---

## 👂 Quick Reminder: How to Get Help (Engineer-Style)
## 💡 도움을 받는 현명한 방법 (엔지니어식 질문법)

If something doesn't work, don't just say "Help!". Tell us:
무언가 작동하지 않을 때, 단순히 "도와주세요!"라고 하지 말고 아래 내용을 말씀해 주세요:

1. **Purpose**: What are you trying to do? (무엇을 하려 했나요?)
2. **Action**: What did you try yourself? (무엇을 스스로 시도해 보았나요?)
3. **Error**: What is the error message? (에러 메시지가 무엇인가요?)
4. **AI Output**: What did AI suggest? (AI는 어떻게 답변했나요?)

---

## 1. Cloud IDE Setup (클라우드 환경 접속)
We will use **StackBlitz**, a powerful Cloud IDE that looks and works exactly like VS Code, but runs entirely in your web browser. No installation is needed!
학기 내내 사용할 클라우드 개발 환경인 **StackBlitz**에 접속할 것입니다. 브라우저에서 실행되며 설치가 필요 없습니다.

### Step 1: Login to GitHub (GitHub 로그인)
StackBlitz accounts are best linked with GitHub.
1. Go to: [github.com](https://github.com)
2. Create an account if you don't have one, or log in.
3. (GitHub 계정이 없다면 가입하고 로그인하세요.)

### Step 2: Access StackBlitz (StackBlitz 접속)
1. Go to: [stackblitz.com](https://stackblitz.com/)
2. Click **"Sign in"** at the top right, and choose **"Continue with GitHub"**.
3. (우측 상단의 로그인 버튼을 눌러 GitHub로 계속하기를 선택합니다.)

### Step 3: Create a Blank HTML Project (새 프로젝트 생성)
1. On the StackBlitz dashboard, look for the **Popular** or **Vanilla** tab.
2. Click the **"Static (HTML/JS/CSS)"** template with the orange HTML5 shield icon 🛡️.
3. You will see a file explorer on the left, an editor in the middle, and a live preview on the right!
4. (대시보드의 Popular/Vanilla 탭에서 주황색 HTML5 방패 모양 아이콘이 있는 **`Static (HTML/JS/CSS)`** 템플릿을 찾아 클릭합니다. 왼쪽에는 파일, 중간에는 코드, 오른쪽에는 실시간 미리보기가 나타납니다!)

---

## 2. Lab Activity: "Magic! From Text to View"
Let's see how a simple text file becomes a website.
실제 텍스트 파일이 어떻게 웹사이트로 변하는지 마법 같은 과정을 확인해 봅시다.

### Task 1: Create a simple text file (텍스트 파일 만들기)
1. In StackBlitz, you will see a default `index.html`. For now, let's create a new file.
2. Click the **"New File"** icon in the file explorer and name it `hello.txt`.
3. Type: `Hello, I am [Your Name]. This is my first web page.`
4. To view this text file, simply type its name in the URL bar of the preview panel on the right (e.g., `...stackblitz.io/hello.txt`), or right click the file and choose to preview.
5. **What do you see?** Just a simple text in the browser.

### Task 2: Rename and Add a Tag (파일 이름 변경 및 태그 추가)
1. Rename `hello.txt` to `hello.html`.
2. Wrap your name with `<h1>` tag:
   ```html
   <h1>Hello, I am [Your Name]. This is my first web page.</h1>
   ```
3. Save the file (Ctrl+S or Cmd+S).
4. **Look at the browser again!**
   - **What changed?** The text became Big and Bold!
   - **Lesson:** HTML 'tags' define the structure and look of your content.

---

## 🚀 Lab Finish!
Make sure you can easily log into StackBlitz for next week.
다음 주 수업을 위해 StackBlitz 로그인이 원활한지 다시 확인하세요!
