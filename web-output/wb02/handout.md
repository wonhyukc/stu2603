# 2주차 핸드아웃: HTML 기초
# Week 2 Handout: Introduction to HTML

**강사:** Wonhyuk William Chung (wonhyukc@stu.ac.kr)
**Instructor:** Wonhyuk William Chung (wonhyukc@stu.ac.kr)

웹프로그래밍 2주차에 오신 것을 환영합니다! 이번 주에는 모든 웹사이트의 뼈대가 되는 HTML의 기본을 배웁니다. 나만의 디지털 명함이라는 첫 웹페이지를 만들어 볼 것입니다.
Welcome to Week 2 of Web Programming! This week, we will learn the basics of HTML, which forms the skeleton of all websites. We will create our first web page: a digital business card.

---

## 1. 핵심 개념 정리
## 1. Core Concepts Summary

HTML(HyperText Markup Language)은 웹페이지를 만드는 데 사용되는 표준 마크업 언어입니다. 사람의 뼈대와 같이 페이지의 구조를 제공합니다.
HTML (HyperText Markup Language) is the standard markup language used to create web pages. It provides the structure of the page, much like a human skeleton.

### 필수 HTML 구조
### Essential HTML Structure

- `<html>`: 모든 것을 감싸는 루트(최상위) 요소입니다.
- `<html>`: The root element that wraps everything.
- `<head>`: 메타데이터, 제목, 보이지 않는 설정들을 포함합니다. (뇌와 같이 중요하지만 보이지 않습니다.)
- `<head>`: Contains metadata, title, and invisible settings. (Like the brain: important but invisible.)
- `<body>`: 웹페이지의 보이는 콘텐츠를 포함합니다. (사용자가 실제로 보는 모든 것)
- `<body>`: Contains the visible content of the web page. (Everything the user actually sees.)

### 자주 사용하는 태그
### Frequently Used Tags

| 태그 (Tag) | 설명 (Description) | 예시 (Example) |
|---|---|---|
| `<h1> ~ <h6>` | 제목. `<h1>`이 가장 크고 중요합니다. (Headings. `<h1>` is the largest and most important.) | `<h1>안녕하세요</h1>` |
| `<p>` | 텍스트 문단입니다. (A paragraph of text.) | `<p>제 이름은 ...</p>` |
| `<img>` | 이미지를 삽입합니다. **닫는 태그가 없습니다** (빈 태그). (Inserts an image. **It has no closing tag** (empty tag).) | `<img src="url">` |

### 이미지 경로: 절대경로 vs 상대경로
### Image Paths: Absolute vs. Relative Paths

| 유형 (Type) | 사용 시기 (When to use) | 예시 (Example) |
|---|---|---|
| **절대경로 (Absolute Path)** | 인터넷 상의 이미지 링크 (Link to an image on the internet) | `https://example.com/photo.jpg` |
| **상대경로 (Relative Path)** | 같은 폴더 내의 이미지 링크 (Link to an image in the same folder) | `./images/photo.jpg` |

> **팁:** `src` URL에 오타가 있으면 깨진 이미지 아이콘('엑스박스')이 나타납니다. 항상 경로를 다시 한 번 확인하세요!
> **Tip:** If there is a typo in the `src` URL, a broken image icon will appear. Always double-check your paths!

---

## 2. 실습: 첫 HTML 코드 작성해보기
## 2. Lab Activity: Writing Your First HTML Code

수업 중에는 브라우저에서 **StackBlitz** (stackblitz.com)를 열고 강사의 라이브 코딩 시연을 따라 해보세요. 별도의 설치가 필요 없습니다.
During class, open **StackBlitz** (stackblitz.com) in your browser and follow along with the instructor's live coding demonstration. No separate installation is required.

### 단계별 실습 가이드
### Step-by-Step Lab Guide

1. **StackBlitz 열기:** [stackblitz.com](https://stackblitz.com)에 접속하여 "Blank Project" -> "Static (HTML/JS/CSS)"를 클릭합니다.
1. **Open StackBlitz:** Go to [stackblitz.com](https://stackblitz.com) and click "Blank Project" -> "Static (HTML/JS/CSS)".

2. **기본 뼈대 살펴보기:** `index.html` 파일을 열어보세요. 표준 HTML 구조(`<html>`, `<head>`, `<body>`)를 확인할 수 있습니다.
2. **Examine the Basic Skeleton:** Open the `index.html` file. You can see the standard HTML structure (`<html>`, `<head>`, `<body>`).

3. **내용 추가하기:** `<body>` 태그 안에 다음 내용을 지우고 자기소개를 입력해 보세요. **취미, 고향의 좋은 점, 컴퓨터 사용 경험**을 포함해 보세요:
3. **Add Content:** Inside the `<body>` tag, clear the existing content and enter your self-introduction. Make sure to include your **hobbies, good things about your hometown, and your computer experience**:
   ```html
   <h1>안녕하세요, 저는 [이름]입니다!</h1>
   <h1>Hello, I am [Name]!</h1>
   <p>제 디지털 명함에 오신 것을 환영합니다. 저는 [취미]를 좋아하고, 제 고향은 [고향 명소/특징]로 유명한 [고향]입니다. 저는 컴퓨터 사용 경험이 [거의 없습니다/어느 정도 있습니다].</p>
   <p>Welcome to my digital business card. I like [Hobbies], and my hometown is [Hometown], famous for [Attractions/Features]. I have [very little/some] experience using computers.</p>
   ```

4. **이미지 추가하기:** `<img>` 태그를 사용하여 프로필 사진을 추가해 보세요. 온라인에서 원하는 이미지 URL을 복사해 `src` 속성에 붙여넣습니다.
4. **Add an Image:** Use the `<img>` tag to add your profile picture. Copy a desired image URL from the internet and paste it into the `src` attribute.
   ```html
   <img src="https://example.com/your-image.jpg" width="200">
   ```
   홈페이지니까 공개 되는게 원칙입니다. 공개하면 안되는 내용을 올리지 마세요.
   Since it's a homepage, it is public by default. Do not upload content that should not be shared publicly.

5. **실시간 미리보기:** 코드를 입력하면서 오른쪽 Preview 패널이 즉시 업데이트되는 것을 확인하세요! 이것이 바로 첫 웹 페이지입니다.
5. **Live Preview:** As you type your code, notice that the Preview panel on the right updates instantly! This is your very first web page.

6. **AI와 함께 버전 관리 학습하기:** AI에게 다음 개념들을 물어보고 학습하세요: Git과 GitHub은 무엇이고 왜 사용하는가? 커밋(Commit)이란 무엇인가? 리포지토리(Repository)란 무엇인가? Public 리포지토리와 Private 리포지토리의 차이점은 무엇인가? 오늘 다 몰라도 됩니다. 앞으로 이건 평생 친구하며 사용하고, 계속 알아갈 겁니다.
6. **Learn Version Control with AI:** Ask AI to explain the following concepts and learn them: What are Git and GitHub, and why do we use them? What is a Commit? What is a Repository? What is the difference between Public and Private repositories? You don't need to understand everything today. You will use these like lifelong friends and continue to learn about them.
   
   1주차에 과제로 제출한 repo와는 다른, 새로운 gitrepo를 만드세요. 이름을 my-intro 라고 합시다. 공개 repo를 만들어야합니다. 
   Create a new git repo, different from the one you submitted as an assignment in Week 1. Let's name it `my-intro`. You must create a public repo.

7. **GitHub에 업로드하기:** 작성한 HTML 코드를 자신의 GitHub 리포지토리에 올리세요. 자신의 GitHub 리포지토리를 반드시 **Public(공개)**으로 설정해야 합니다.
7. **Upload to GitHub:** Upload your HTML code to your GitHub repository. You must set your GitHub repository to **Public**.

8. **커밋 제출하기:** 이 올렸던 커밋의 해쉬와 URL을 함께 제출해 주세요. 주소 표시줄을 복사하면 됩니다.
8. **Submit the Commit:** Please submit the hash and URL of the commit you just uploaded. You can simply copy it from the address bar.
   - 예시 / Example: `https://github.com/wonhyukc/web-stu/commit/00312a6507c850ddbe778fd843fcc375f6788807` (또는 비슷한 커밋 URL / or a similar commit URL)
   이 내용은 채점할 때까지 제대로 접근 가능해야 합니다.
   This link must be accessible until grading is complete.

---

## 3. 마이크로 과제
## 3. Micro-Assignment

### 과제 0.1: 전체 제출 내용 정리
### Assignment 0.1: Summary of All Submissions

제출물은 A4 용지 절반(1/2) 분량이면 충분합니다. 길게 적지 않아도 됩니다. 다음 항목들을 포함해야 합니다:
The submission should be about half an A4 page long. You do not need to write extensively. It must include the following items:

1. **수업 소감**
1. **Class Reflection**
   - 수업을 들은 소감, 건의 사항 또는 자유로운 코멘트를 작성해 주세요.
   - Please write your thoughts on the class, suggestions, or any free comments.

2. **자신의 사진 첨부**
2. **Attach Your Photo**
   - 여러분을 기억하고자 하는 의도이니 본인의 사진을 첨부해 주세요.
   - This is intended to help us remember you, so please attach a photo of yourself.
   - 사진의 크기는 500Kb를 넘지 않도록 합니다. 너무 큰 사진은 크기를 줄여서 보내주세요. 잘 모르면 '사진 크기 줄이기'로 구글링해서 이번 기회에 직접 배워봅니다.
   - The file size of the photo should not exceed 500Kb. If the photo is too large, please reduce its size before sending. If you don't know how, google "how to reduce photo size" and learn how to do it yourself this time.
   - 사진의 이름은 자신의 이름으로만 지정해 주세요 (학번, 학과는 적지 않습니다). 예시: `정원혁.jpg`
   - Name the photo file exactly with your name only (do not include your student ID or department). Example: `Wonhyuk.jpg`
   - 사진은 가능하면 실물과 비슷한 것으로 해주세요. 지나친 포토샵으로 실제 얼굴을 알아볼 수 없으면 나중에 기억하기 어렵습니다.
   - Please use a photo that looks like you in real life. If it's overly photoshopped and your real face is unrecognizable, it will be hard to remember you later.

3. **eCampus에 자신의 사진 등록**
3. **Register Your Photo on eCampus**
   - 현대에는 온라인에서 많은 활동이 일어납니다. 그곳에서 익명으로만 지내는 것은 오히려 손해를 가져올 때가 많습니다. 내성적인 성격이시더라도 꼭 등록해 보세요.
   - Nowadays, many activities happen online. Staying completely anonymous there can often be disadvantageous. Even if you are introverted, please try to register it.
   - 아울러 eCampus에 등록된 정보(특히 메일 주소)가 틀리다면 올바르게 수정해 주세요. 모두에게 공개할 필요는 없습니다. (메일에는 등록완료 라고만 적으면 됩니다.)
   - Furthermore, if the information registered on eCampus (especially your email address) is incorrect, please fix it. You don't need to make it public. (In your email, just write "Registration complete".)

4. **크롬 및 AdBlock 사용 소감**
4. **Experience with Chrome and AdBlock**
   - 크롬(Chrome)을 설치하고 로그인하여 사용해 보세요. 
   - Install Chrome, log in, and try using it.
   - 그 후 AdBlock 확장 프로그램을 설치 및 사용해 보고 소감을 적어주세요. (확장 프로그램을 확실히 보고 유사한 악성 확장을 설치하지 않도록 조심하세요.)
   - After that, install and use the AdBlock extension, and write your thoughts. (Make sure you verify the extension so you don't accidentally install a similar malicious extension.)

5. **단축키 공부**
5. **Study Keyboard Shortcuts**
   - 윈도우 단축키 및 크롬 단축키를 스스로 찾아 다섯 개 이상 공부하고 그 목록과, 소감을 적어주세요.
   - Search for Windows and Chrome keyboard shortcuts on your own, learn at least five of them, and write down the list and your thoughts.

6. **AI 사용 경험**
6. **AI Usage Experience**
   - **AI 프롬프트 (AI Prompt):** AI에게 질문한 정확한 내용을 기재합니다. (예: *"git이란 무엇이야?"*) / Write the exact prompt you asked the AI. (e.g., *"What is git?"*)
   - **AI 결과물 비평 (AI Critique):** AI의 답변을 한 문장으로 분석하세요. (예: *"설명이 어려웠다. 그래서 쉽게 다시 설명해달라고 했다."*) / Analyze the AI's response in one sentence. (e.g., *"The explanation was difficult, so I asked it to explain it more easily."*)   

---

### 마이크로 과제 제출 안내
### Micro-Assignment Submission Guide

이 마이크로 과제는 email로 제출합니다. 
This micro-assignment should be submitted via email.

- **제출처 (Submit to):** `wonhyuk@stu.ac.kr`
- **제목 (Subject):** `과제0.1 학번` (예 / Example: `과제0.1 20240001`)
- **⚠️ 주의사항 (Warning):** 코드로 메일을 자동 필터링하기 때문에 규칙을 지키지 않으면 채점에서 누락됩니다. 반드시 지킵니다. 제목에는 "과제0.1", 하나 이상의 빈칸, 그리고 "학번" 이렇게만 적어야 합니다. 다른 어떠한 문자도 포함하지 마세요.
- **⚠️ Warning:** Since emails are automatically filtered by code, if you do not follow the rules, your submission will be missed during grading. You must follow them. The subject line must contain ONLY "과제0.1", one or more spaces, and your "Student ID". Do not include any other characters.
