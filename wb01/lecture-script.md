# wb01 Lecture Script — Orientation & Intro to the Web
# wb01 강의 스크립트 — 오리엔테이션과 웹 입문

> **Instructor script for Flipped Learning video production and in-class reference.**
> **강사용 대본입니다. Flipped Learning 영상 제작 및 강의실 진행 기준 문서입니다.**
> - Total duration / 총 분량: **75 min** (25 min × 3 sections)
> - Language / 언어: Bilingual — English (primary) / Korean (parallel) | 영한 병용
> - Environment / 실습 환경: StackBlitz (browser-based cloud IDE)

---

## Section 1 — The Web & Course Introduction / 웹이란 무엇인가·강의 소개 (25 min)

### [Opening / 오프닝 — 4 min]

Welcome to Web Programming. I'm Wonhyuk William Chung, and I'll be your instructor for this course throughout the semester.

웹프로그래밍 수업에 오신 걸 환영합니다. 저는 이 수업을 담당하는 강사 정원혁입니다. 앞으로 한 학기 동안 함께하게 됩니다.

Today is orientation week, which means we are not going to write a complete webpage. We will write exactly one HTML tag — just one. The rest of this session is entirely dedicated to answering two questions: What is the web, really? And how does this course expect you to approach it?

오늘은 오리엔테이션 주차입니다. 완전한 웹 페이지를 만들지는 않습니다. HTML 태그를 딱 하나만 씁니다. 나머지 시간은 두 가지 질문에 답하는 데 씁니다. 웹이란 정말 무엇인가? 그리고 이 수업이 여러분에게 기대하는 것은 무엇인가?

I want to start by telling you something that probably sounds strange coming from a web programming instructor. You do not need to memorize HTML. You do not need to be able to write code from scratch in an exam. What this course genuinely cares about is whether you can read, understand, and critically evaluate what you see in front of you. And increasingly in 2025, that means evaluating what an AI produces for you.

한 가지 솔직한 말씀을 먼저 드리겠습니다. HTML을 외울 필요가 없습니다. 시험에서 코드를 처음부터 작성할 필요도 없습니다. 이 수업이 진짜로 원하는 것은, 여러분이 눈앞에 보이는 것을 읽고, 이해하고, 비판적으로 평가할 수 있는지의 여부입니다. 2025년에는 그것이 AI가 여러분을 위해 생산한 것을 평가하는 것을 의미합니다.

Let me ask an honest question. How many of you are here because you heard that web programming leads to good job prospects? Or because this course is required for your degree? Those are completely valid reasons. But I want to tell you a slightly different story about why this matters.

솔직하게 물어볼게요. "웹 할 줄 알면 취업에 유리하다고 해서 왔습니다" 또는 "졸업 요건이라서 왔습니다"라고 생각하는 분 계신가요? 그 이유, 완전히 괜찮습니다. 그런데 이 수업에서는 왜 이 공부가 중요한지에 대해 조금 다른 이야기를 하려고 합니다.

### [A Brief History of the Web / 웹의 짧은 역사 — 8 min]

Let us start with a question. What do you think the web actually is?

질문을 하나 드리겠습니다. 웹이 뭐라고 생각하시나요?

Most people say "the internet." That is close, but not quite the same thing. The **internet** is the global network of connected computers — it is the physical infrastructure of cables, routers, and satellites that spans the entire planet. The **web** is one service that runs on top of the internet. There are other services too — email runs on the internet, so does video calling, and so do file transfers. But the web, technically called the World Wide Web, is specifically about linked documents that you access through a browser.

대부분 "인터넷"이라고 합니다. 비슷하지만 같지는 않습니다. **인터넷**은 전 세계 컴퓨터를 연결하는 물리적 네트워크, 즉 케이블·라우터·위성으로 이루어진 인프라입니다. **웹**은 그 위에서 작동하는 서비스 중 하나입니다. 이메일도 인터넷 위에서 동작하고, 화상통화도, 파일 전송도 마찬가지입니다. 하지만 World Wide Web, 즉 웹은 특별히 브라우저를 통해 접근하는 링크된 문서들의 시스템을 가리킵니다.

Think of it this way. The internet is the highway system — the physical roads, bridges, and tunnels that connect every city in the country. The web is like the postal delivery service that uses those highways to bring packages to every address. Other services — like phone calls or radio broadcasts — also use the same road infrastructure but operate independently. Understanding this distinction helps you think more precisely about what a web page actually is: it is a document with an address.

이렇게 생각해보세요. 인터넷은 고속도로 시스템 — 전국 모든 도시를 연결하는 물리적 도로, 다리, 터널 — 입니다. 웹은 그 고속도로를 이용해 모든 주소에 택배를 배달하는 서비스와 같습니다. 전화나 라디오 같은 다른 서비스도 동일한 도로 인프라를 사용하지만 독립적으로 작동합니다. 이 구분을 이해하면, 웹 페이지가 실제로 무엇인지 더 정확하게 생각할 수 있습니다. 웹 페이지는 주소가 있는 문서입니다.

The story of the web starts in 1989, at CERN — the particle physics research center in Geneva, Switzerland. A British scientist named Tim Berners-Lee was working there, and he had a practical problem. CERN employed thousands of researchers from dozens of countries, all working on different experiments, and they constantly needed to share technical documents with each other. Emailing large files was impractical. Physical mail was slow. And every researcher's computer ran different software, so even when files were shared, they often could not be opened.

웹의 역사는 1989년 스위스 제네바의 입자물리학 연구소 CERN에서 시작됩니다. 팀 버너스리(Tim Berners-Lee)라는 영국 과학자가 실용적인 문제를 마주했습니다. CERN에는 수십 개국에서 온 수천 명의 연구원이 있었고, 서로 다른 실험에 참여하면서 기술 문서를 공유해야 했습니다. 대용량 파일을 이메일로 보내는 것은 비실용적이었고, 물리적 우편은 느렸습니다. 그리고 각 연구원의 컴퓨터가 서로 다른 소프트웨어를 사용해서 파일을 공유해도 열리지 않는 경우가 많았습니다.

Tim Berners-Lee's solution was elegant and simple. He proposed storing documents on a central server with unique addresses. Any computer — running any software — could request a document from that server by typing its address. The server would send the document back, and the requesting computer would display it. He invented a simple text markup language called HTML to format those documents, a system of addresses called URLs, and a protocol called HTTP to govern how documents are requested and delivered. All three of those inventions are still the foundation of every web page you visit today.

팀 버너스리의 해결책은 우아하고 단순했습니다. 중앙 서버에 문서를 저장하고, 각 문서에 고유한 주소를 부여하는 것이었습니다. 어떤 소프트웨어를 사용하는 어떤 컴퓨터든, 주소를 입력하면 서버에서 그 문서를 요청할 수 있었습니다. 서버는 문서를 돌려보내고, 요청한 컴퓨터가 이를 표시했습니다. 그는 문서를 형식화하는 간단한 마크업 언어인 HTML, 주소 시스템인 URL, 문서를 요청하고 전달하는 방식을 규정하는 프로토콜인 HTTP를 발명했습니다. 이 세 가지 발명이 오늘날 여러분이 방문하는 모든 웹 페이지의 기반입니다.

By 1991, the first public website was online. By 1994, the W3C — the World Wide Web Consortium — was founded to establish web standards, so that everyone building websites would follow the same rules. In 1995, a browser company called Netscape created JavaScript in just ten days — that rushed origin story helps explain some of JavaScript's quirky behaviors, which you will encounter later in the semester.

1991년에 첫 번째 공개 웹사이트가 등장했습니다. 1994년에는 W3C(월드 와이드 웹 컨소시엄)가 설립되어 웹 표준을 제정했습니다. 1995년에 Netscape라는 브라우저 회사가 단 10일 만에 JavaScript를 만들었습니다 — 이 급박한 탄생 배경이 JavaScript의 독특한 동작 방식을 설명하는 데 도움이 됩니다. 학기 후반에 직접 경험하게 될 것입니다.

The core model that Tim Berners-Lee invented — **a client sends a request, a server responds with a document** — is still exactly what happens every time you open a webpage today. Before you type a single line of HTML, understanding this model is the most important thing.

팀 버너스리가 발명한 핵심 모델 — **클라이언트가 요청을 보내면 서버가 문서로 응답한다** — 은 오늘날 웹 페이지를 열 때마다 그대로 동작합니다. HTML 한 줄을 쓰기 전에, 이 모델을 이해하는 것이 가장 중요합니다.

Let me walk through a concrete example. When you type `google.com` in your browser's address bar and press Enter, here is the actual sequence of events. Your browser — Chrome, Safari, or whatever you use — converts that domain name into a numeric IP address using a system called DNS. It then sends a request across the internet to Google's servers: "Please send me the main document at google.com." A Google server receives that request, selects the appropriate HTML file for your request, and sends it back as a response. Your browser receives the HTML file and reads it line by line. Wherever it encounters a tag that says "this is a heading," it renders large text. Wherever it finds a tag that says "this is an image," it makes an additional request to download that image. The final visual result — everything you see on screen — is assembled by your browser from the instructions in that HTML file.

구체적인 예를 들어봅시다. 브라우저 주소창에 `google.com`을 입력하고 Enter를 누를 때 실제로 무슨 일이 일어나는지 순서대로 설명하겠습니다. 브라우저는 먼저 DNS라는 시스템을 사용해 도메인 이름을 숫자 IP 주소로 변환합니다. 그런 다음 인터넷을 통해 Google 서버에 요청을 보냅니다. "google.com의 메인 문서를 보내주세요." Google 서버는 요청을 받고, 적절한 HTML 파일을 선택해 응답으로 돌려보냅니다. 브라우저는 HTML 파일을 받아 한 줄씩 읽습니다. "이건 제목"이라는 태그를 만나면 큰 글자로 렌더링합니다. "이건 이미지"라는 태그를 만나면 해당 이미지를 내려받으려고 추가 요청을 보냅니다. 화면에 보이는 최종 결과물은 브라우저가 HTML 파일의 지시를 조합해 만들어낸 것입니다.

So what are HTML, CSS, and JavaScript in this picture? **HTML** is the language you use to write the document. It tells the browser what elements exist and what type they are — headings, paragraphs, images, links, buttons. **CSS** is a separate language that tells the browser how those elements should look — their colors, fonts, sizes, and positions on screen. **JavaScript** is a programming language that adds behavior — making elements respond to user actions, fetching new data from servers without reloading the page, creating animations, and building dynamic interfaces. This semester, you will learn all three in that order.

그러면 HTML, CSS, JavaScript는 이 그림에서 어떤 역할을 할까요? **HTML**은 문서를 작성하는 언어입니다. 브라우저에게 어떤 요소가 있고 그것이 어떤 종류인지 알려줍니다 — 제목, 문단, 이미지, 링크, 버튼. **CSS**는 요소들이 어떻게 보여야 하는지를 알려주는 별도의 언어입니다 — 색상, 폰트, 크기, 화면 위치. **JavaScript**는 동작을 추가하는 프로그래밍 언어입니다 — 사용자 행동에 반응하고, 페이지를 새로 고침하지 않고 서버에서 데이터를 가져오고, 애니메이션을 만들고, 동적 인터페이스를 구축합니다. 이 세 가지를 이번 학기에 그 순서대로 배웁니다.

### [AI in the Age of Web Development / AI 시대의 웹 개발자 — 8 min]

Here is the honest truth about web development in 2025. If you ask ChatGPT or Gemini to "build me a simple webpage with a button that changes colors," you get working HTML, CSS, and JavaScript within seconds. It formats nicely, it usually works on first try, and it comes with comments explaining what each part does. So why should you learn this yourself?

2025년 웹 개발의 솔직한 현실을 말씀드리겠습니다. ChatGPT나 Gemini에게 "버튼 누르면 색이 바뀌는 간단한 웹 페이지 만들어줘"라고 하면 몇 초 안에 작동하는 HTML, CSS, JavaScript가 나옵니다. 깔끔하게 포매팅되고, 보통 처음부터 작동하며, 각 부분이 무엇을 하는지 설명하는 주석도 붙어있습니다. 그러면 왜 직접 배워야 할까요?

Because **AI confidently produces wrong code**. Not occasionally, and not in obvious ways. It will give you an HTML attribute that the specification removed years ago. It will suggest a CSS feature that works perfectly in Chrome but breaks completely in Safari — with no warning. It will write JavaScript that looks right, passes a quick scan, but crashes in a specific edge case that the AI simply did not consider. And if you cannot read the code at all, you will copy the wrong answer, submit it, and either receive a zero or deploy a broken product.

왜냐하면 **AI는 자신 있게 잘못된 코드를 생성**하기 때문입니다. 가끔 실수하는 게 아니라, 눈에 띄지 않는 방식으로 자주 틀립니다. 사양에서 몇 년 전에 삭제된 HTML 속성을 제안합니다. Chrome에서는 완벽하게 작동하지만 Safari에서는 완전히 깨지는 CSS 기능을 아무 경고 없이 사용합니다. 겉보기에 맞아 보이고 빠른 검토를 통과하지만, AI가 고려하지 않은 특정 예외 상황에서 충돌하는 JavaScript를 작성합니다. 코드를 전혀 읽을 수 없다면, 틀린 답을 그대로 복사하고 제출하거나, 결함 있는 제품을 배포하게 됩니다.

I want to be very clear about what skill this course is actually building. It is not "write HTML from memory." That is a 1990s skill. The skill this course develops is **"read what AI writes and judge whether it is correct."** That judgment ability — reading code, understanding what it is doing, and spotting when something is off — is what makes you genuinely useful in any technology-adjacent career in the next decade.

이 수업이 실제로 키우는 능력에 대해 명확하게 말씀드리겠습니다. "HTML을 외워서 쓰는 것"이 아닙니다. 그것은 1990년대 기술입니다. 이 수업이 개발하는 기술은 **"AI가 쓴 것을 읽고, 맞는지 판단하는 것"**입니다. 코드를 읽고, 무엇을 하는지 이해하고, 뭔가 잘못됐을 때 찾아내는 그 판단 능력이 앞으로 10년간 기술 관련 어떤 직업에서도 여러분을 진정으로 가치 있게 만들어 줍니다.

Let me give you a concrete picture of jobs that will not disappear because of AI — and what they all have in common. A product manager at a software company who can read the code their engineering team writes, and can therefore tell whether the AI's suggestions are being adopted sensibly or blindly. A graphic designer who understands how browsers render CSS, and can therefore look at a responsive design and explain why it breaks on mobile screens. A business analyst who can open an AI-generated spreadsheet formula, verify its logic, and modify it correctly. A marketing professional who can read the HTML behind an email template and understand why it renders differently in Gmail versus Outlook. None of these people are software engineers. None of them write code from scratch every day. But all of them can read code, understand the logic, and catch AI mistakes. That is the target skill level for this course.

AI 때문에 사라지지 않을 직업들의 구체적인 그림을 보여드리겠습니다. 이 직업들의 공통점이 있습니다. 엔지니어링 팀이 작성하는 코드를 읽을 수 있는 소프트웨어 회사의 기획자는, AI 제안이 합리적으로 채택되는지 아니면 맹목적으로 따르는지를 구별할 수 있습니다. 브라우저가 CSS를 어떻게 렌더링하는지 이해하는 그래픽 디자이너는 반응형 디자인을 보고 모바일에서 왜 깨지는지 설명할 수 있습니다. AI가 생성한 스프레드시트 공식을 열어 논리를 검증하고 올바르게 수정할 수 있는 비즈니스 분석가. Gmail과 Outlook에서 왜 다르게 렌더링되는지 이해하기 위해 이메일 템플릿의 HTML을 읽을 수 있는 마케팅 전문가. 이들 중 누구도 소프트웨어 엔지니어가 아닙니다. 매일 코드를 처음부터 작성하지 않습니다. 그러나 모두 코드를 읽고, 논리를 이해하고, AI의 실수를 잡아낼 수 있습니다. 이 수업의 목표 기술 수준이 바로 그것입니다.

### [What You'll Build This Semester / 이번 학기에 만드는 것 — 5 min]

Here is the semester roadmap at a glance.

한 학기 흐름을 간단히 안내합니다.

During **Weeks 1 through 8**, you will work entirely inside **StackBlitz** — a cloud-based code editor that runs directly in your browser with no downloads required. You will learn HTML and CSS fundamentals. The projects you will build include an online business card with your name and contact details, a styled form with input fields, and a personal resume page. Each week builds on the previous one.

**1~8주차** 동안에는 **StackBlitz** — 다운로드 없이 브라우저에서 바로 실행되는 클라우드 코드 에디터 — 안에서 모두 진행합니다. HTML과 CSS 기초를 배웁니다. 만드는 프로젝트에는 이름과 연락처가 담긴 온라인 명함, 입력 필드가 있는 스타일된 폼, 개인 이력서 페이지가 포함됩니다. 매주 이전 주에서 배운 것을 바탕으로 쌓아 올립니다.

At **Week 8**, there is a midterm. This is not a memorization exam. You will receive HTML and CSS code with deliberate mistakes, and your task is to read it, identify the bugs, fix them, and explain why they were wrong. The exam is open-book — you can refer to the handout we give you during the test.

**8주차**에는 중간고사가 있습니다. 암기 시험이 아닙니다. 의도적인 실수가 포함된 HTML과 CSS 코드를 받고, 그것을 읽고, 버그를 찾고, 수정하고, 왜 틀렸는지 설명하는 것이 과제입니다. 시험은 오픈북입니다 — 시험 중 제공된 핸드아웃을 참고할 수 있습니다.

From **Weeks 9 through 14**, you will switch to **VS Code installed on your own computer**, with a plugin called Live Server. The focus shifts to JavaScript. You will make pages interactive — buttons that respond to clicks, content that changes dynamically, forms that validate input before submission. This is where the web starts feeling alive.

**9~14주차**에는 **본인 컴퓨터에 설치된 VS Code**와 Live Server 플러그인으로 전환합니다. JavaScript에 집중합니다. 페이지를 인터랙티브하게 만들 것입니다 — 클릭에 반응하는 버튼, 동적으로 변하는 콘텐츠, 제출 전에 입력을 검증하는 폼. 여기서부터 웹이 살아있다는 느낌이 나기 시작합니다.

At **Week 15**, there is a final exam. You will demonstrate a semester project — a small webpage you built — and explain the code logic in your own words. The point is not that it is perfect, but that you understand what you built and why you made the choices you made.

**15주차**에는 기말고사가 있습니다. 한 학기 프로젝트 — 여러분이 만든 작은 웹 페이지 — 를 시연하고 코드 논리를 본인의 말로 설명합니다. 완벽할 필요는 없습니다. 자신이 무엇을 만들었고 왜 그런 선택을 했는지 이해하고 있으면 됩니다.

### [Flipped Learning / 거꾸로 수업 — 4 min]

This course uses **Flipped Learning**, sometimes called the inverted classroom model. Instead of me lecturing for 75 minutes while you listen passively, and then you doing practice problems alone at home, we reverse that cycle completely.

이 수업은 **거꾸로 수업(Flipped Learning)** 방식, 즉 역전 교실 모델을 사용합니다. 제가 75분 동안 강의하고 여러분이 수동적으로 듣다가 집에서 혼자 연습 문제를 푸는 것이 아니라, 그 순서를 완전히 뒤집습니다.

**Before class each week**: I upload a lecture video to eCampus by 18:00 the day before class. You watch that video at home or wherever is convenient — on your phone, on your laptop, on the bus. This is your "listening to the lecture" time. You can pause it, rewind it, and watch it at your own pace.

**매주 수업 전**: 수업 전날 18:00까지 eCampus에 강의 영상을 업로드합니다. 여러분은 그 영상을 집에서 또는 편한 곳에서 시청합니다 — 스마트폰으로, 노트북으로, 버스에서도. 이것이 "강의 듣는" 시간입니다. 일시정지, 되감기, 본인 속도에 맞춰 시청할 수 있습니다.

**During class**: Instead of re-explaining what you already watched, we spend the entire class doing hands-on practice. I walk around the room while you work, so I can answer questions immediately and one-on-one. You get direct, personalized feedback in the moment rather than after the fact.

**수업 중**: 이미 본 내용을 다시 설명하는 대신, 수업 시간 전체를 직접 실습에 씁니다. 여러분이 작업하는 동안 제가 교실을 돌아다니며 즉각적으로 일대일로 질문에 답합니다. 사후가 아닌 그 순간에 직접적이고 개인화된 피드백을 받습니다.

**After class**: You submit a Micro-Assignment by 23:59 the night before the following class. This assignment connects what you practiced in class to a real question you explored with AI.

**수업 후**: 다음 수업 전날 23:59까지 마이크로 과제를 제출합니다. 이 과제는 수업에서 실습한 것과 AI와 함께 탐구한 실제 질문을 연결합니다.

The most important thing I need you to understand is this. If you come to class without watching the pre-class video, you will not be able to follow the hands-on exercises. The exercises build on what was explained in the video. Please treat the pre-class video as mandatory, not optional. I genuinely mean that.

가장 중요하게 이해해야 할 것이 있습니다. 사전 영상을 보지 않고 수업에 오면, 직접 실습을 따라갈 수 없습니다. 실습은 영상에서 설명한 내용을 기반으로 합니다. 사전 영상 시청을 선택이 아닌 필수로 생각해주세요. 진심으로 그렇습니다.

---

## Section 2 — Professional Communication / 프로페셔널 커뮤니케이션 (25 min)

### [Why This Matters / 비즈니스 이메일이 왜 중요한가 — 4 min]

This section has nothing directly to do with HTML, CSS, or web browsers. But it is, in my opinion, one of the most important things I teach in this entire course.

이번 섹션은 HTML, CSS, 웹 브라우저와 직접적인 관련이 없습니다. 하지만 제 생각에는 이 수업 전체에서 제가 가르치는 가장 중요한 것 중 하나입니다.

Your first assignment this week is to send me a self-introduction email. You might be wondering why that is a graded assignment in a web programming course. Let me explain.

이번 주 첫 번째 과제는 **강사에게 자기소개 이메일을 보내는 것**입니다. 웹 프로그래밍 수업에서 왜 이게 점수가 있는 과제인지 궁금하실 것입니다. 설명드리겠습니다.

Web developers — and really anyone who works in a technology environment — do not just write code. They communicate constantly. They send project status updates to managers. They ask clarifying questions to clients. They coordinate with designers, testers, and other developers. They apply for internships and jobs. All of this communication happens primarily through email. And the quality of that communication directly affects how people perceive your competence and professionalism, often before they ever see a line of your code.

웹 개발자는 — 사실 기술 환경에서 일하는 누구든 — 코드만 짜지 않습니다. 끊임없이 소통합니다. 상사에게 프로젝트 진행 상황을 보고합니다. 클라이언트에게 명확화 질문을 합니다. 디자이너, 테스터, 다른 개발자들과 협력합니다. 인턴십과 취업을 지원합니다. 이 모든 소통이 주로 이메일을 통해 이루어집니다. 그리고 그 소통의 품질이, 코드 한 줄을 보기 전에, 여러분의 능력과 전문성에 대한 사람들의 인식에 직접적으로 영향을 미칩니다.

I have seen excellent programmers lose job opportunities because their email communication was careless or confusing. I have also seen people with modest technical skills advance quickly because they communicated clearly and professionally. Developing this habit now, in your first year, costs you almost nothing. Not developing it costs you opportunities you will not even know you missed.

저는 훌륭한 프로그래머가 이메일 소통이 부주의하거나 혼란스러워서 취업 기회를 잃는 것을 봤습니다. 또한 기술 실력이 보통인 사람이 명확하고 전문적으로 소통해서 빠르게 성장하는 것도 봤습니다. 1학년인 지금 이 습관을 개발하는 데는 거의 아무 비용도 들지 않습니다. 이 습관을 개발하지 않는 것은 여러분이 놓쳤는지도 모를 기회를 잃는 것입니다.

### [Business Email 5 Principles / 비즈니스 이메일 5원칙 — 12 min]

These rules are not invented by me. They are standard professional practice across industries — technology, finance, healthcare, and every other field. They were established before email existed, in the form of professional letter-writing standards, and they transferred directly to digital communication.

이 규칙들은 제가 만든 게 아닙니다. 기술, 금융, 의료 등 모든 업계에서 통용되는 표준 방식입니다. 이메일이 존재하기 전부터 전문적인 편지 작성 표준의 형태로 확립되어 있었고, 디지털 소통으로 그대로 이전됐습니다.

**Principle 1: Bottom Line Up Front (두괄식 작성)**

Write your main point in the first sentence of your email. The reader should be able to understand the entire purpose of your email by reading only the first sentence.

이메일 본문의 첫 번째 문장에 핵심을 씁니다. 첫 문장만 읽어도 이메일의 전체 목적을 파악할 수 있어야 합니다.

Here is a bad example of an email asking about an assignment deadline:

과제 기한을 묻는 이메일의 나쁜 예입니다:

> "Hello. My name is Gil-dong Hong, and I am a first-year student in the Computer Software department, student ID 20251234. I have been settling into university life and things have been quite busy. The weather has also been cold lately and I hope you are well. Last weekend I was hanging out with friends when I suddenly realized I had not yet completed my homework. I was wondering whether it might be possible for me to ask you about when the assignment might be due?"

이 이메일은 핵심을 마지막 문장에 묻었습니다. 상대방이 기다리고 읽어야 합니다.

> "안녕하세요. 저는 컴퓨터소프트웨어학과 1학년 20251234 홍길동입니다. 대학 생활에 적응하느라 바쁘게 지내고 있습니다. 요즘 날씨도 많이 추워졌는데 건강하신지요. 지난 주말에 친구들이랑 놀다가 숙제를 아직 못 했다는 게 생각이 났습니다. 혹시 과제 기한이 언제인지 여쭤봐도 될까요?"

The point is buried in the last line after three sentences of small talk. The reader — who may be handling dozens of emails that day — must read to the end before knowing what action to take.

핵심이 서 줄의 소소한 이야기 끝에 묻혔습니다. 그날 수십 통의 이메일을 처리하는 수신자는 어떤 행동을 취해야 하는지 알기 위해 끝까지 읽어야 합니다.

A better version:

더 나은 버전:

> "Hello, Professor Chung. I am Gil-dong Hong (Student ID: 20251234, Year 1). I am writing to confirm the deadline for the Week 1 Micro-Assignment. Thank you. — Gil-dong Hong"

> "안녕하세요, 정원혁 강사님. 1학년 20251234 홍길동입니다. 1주차 마이크로 과제 제출 기한을 확인하고자 이메일 드립니다. 감사합니다. — 홍길동"

First sentence states the purpose clearly. The reader knows exactly what is needed in two seconds. That is Bottom Line Up Front.

첫 문장이 목적을 명확하게 밝힙니다. 2초 만에 수신자가 무엇이 필요한지 정확히 알 수 있습니다. 이것이 두괄식 작성입니다.

**Principle 2: Specific Subject Line / 제목을 구체적으로**

The subject line of your email should be specific enough that the recipient knows exactly what the email is about without opening it. It should also include an identifier — typically your name and student ID — so the recipient can find your email later when searching.

이메일 제목은 열어보지 않아도 수신자가 내용을 정확히 알 수 있을 만큼 구체적이어야 합니다. 또한 수신자가 나중에 검색할 때 찾을 수 있도록 식별자 — 보통 이름과 학번 — 를 포함해야 합니다.

Bad subject line: `Hello` or `Question` or `Assignment`

나쁜 제목: `안녕하세요`, `질문있어요`, `과제`

Good subject line: `[20251234 Gil-dong Hong] Week 1 Micro-Assignment Deadline Inquiry`

좋은 제목: `[20251234 홍길동] 1주차 마이크로 과제 제출 기한 문의`

The format I recommend is: `[Student ID Full Name] Subject`. Use this format for every email you send to an instructor this semester, and honestly for every professional email you send beyond this course.

제가 권장하는 형식은: `[학번 이름] 내용`입니다. 이번 학기에 강사에게 보내는 모든 이메일에 이 형식을 사용하세요. 솔직히 이 수업 이후의 모든 전문 이메일에도 사용하면 좋습니다.

**Principle 3: Attach First / 첨부 파일 먼저**

If your email requires an attachment, add the attachment before you begin writing the body of the email. This single habit prevents the most common email mistake in professional settings — sending an email that says "please see the attached file" with no attachment. Once you finish writing a detailed email, the emotional energy to go back and fix it is low. Add the attachment first, every time.

이메일에 첨부 파일이 필요하다면, 본문을 쓰기 전에 먼저 첨부 파일을 추가하세요. 이 단순한 습관 하나가 전문적인 환경에서 가장 흔한 이메일 실수를 방지합니다 — "첨부 파일을 확인해주세요"라고 쓰고 정작 첨부 파일은 없는 이메일. 긴 이메일을 다 작성하고 나면 돌아가서 수정할 심리적 에너지가 낮아집니다. 매번, 항상, 첨부 파일 먼저.

**Principle 4: Distinguish To from CC / To와 CC 구분**

The To field is for the person who must take action or respond to your email. The CC field is for people who need to be informed but are not expected to reply. The BCC field is for recipients who should receive the email without the other recipients knowing they were included.

To 필드는 행동을 취하거나 이메일에 응답해야 하는 사람을 위한 것입니다. CC 필드는 정보를 알아야 하지만 답장이 기대되지 않는 사람들을 위한 것입니다. BCC 필드는 다른 수신자들이 모르게 이메일을 받아야 하는 사람들을 위한 것입니다.

Misusing these fields creates confusion. Putting everyone in To implies everyone needs to respond. Putting your team members in CC on a message to a client is correct professional behavior — it keeps them informed without requiring them to participate in the conversation unless needed.

이 필드들을 잘못 사용하면 혼란이 생깁니다. 모든 사람을 To에 넣으면 모두가 응답해야 한다는 의미입니다. 클라이언트에게 보내는 메시지에 팀원을 CC에 넣는 것은 올바른 전문적 행동입니다 — 필요하지 않으면 대화에 참여하도록 요청하지 않으면서 그들에게 정보를 제공합니다.

**Principle 5: Reply Within 24 Hours / 24시간 이내 답변**

If your name is in the To field of an email, you must reply within 24 hours. Not when you feel like it. Not at the end of the week. Within 24 hours. If you cannot resolve the issue within 24 hours, send an acknowledgment: "I received your message and will respond by [specific date]." This acknowledgment is itself the reply. It prevents the sender from wondering whether you saw it, and it sets a clear expectation.

이메일의 To 필드에 내 이름이 있으면, 24시간 이내에 반드시 답장해야 합니다. 내가 하고 싶을 때가 아니라. 주말이 끝날 때까지도 아니라. 24시간 이내에. 24시간 내에 문제를 해결할 수 없다면, 확인 메시지를 보내세요: "메시지를 받았습니다. [특정 날짜]까지 답변 드리겠습니다." 이 확인 자체가 답장입니다. 발신자가 당신이 봤는지 궁금해하는 것을 방지하고, 명확한 기대치를 설정합니다.

These five principles apply throughout this entire semester. When you email me with a question, use them. When you collaborate with teammates on a project, use them. When you apply for an internship, use them. The goal is that by the time you graduate, professional email communication feels natural, not effortful.

이 다섯 원칙은 이번 학기 내내 적용됩니다. 강사에게 질문 이메일을 보낼 때. 팀 프로젝트에서 협력할 때. 인턴십에 지원할 때. 목표는 졸업할 때쯤에는 전문적인 이메일 소통이 힘들지 않고 자연스럽게 느껴지는 것입니다.

### [Engineer-Style Questioning / 엔지니어식 질문법 — 5 min]

The second communication principle is about how to ask questions when something goes wrong — which, in programming, will happen constantly.

두 번째 소통 원칙은 무언가 잘못됐을 때 어떻게 질문하는가에 관한 것입니다. 프로그래밍에서는 이런 일이 끊임없이 일어납니다.

Bad question: "Teacher, this doesn't work."

나쁜 질문: "선생님, 이거 왜 안 돼요."

I hear this many times every semester. And every time, my answer is the same. I cannot help you with that information. I do not know what "this" refers to. I do not know what "doesn't work" means — does it show an error? Does it display incorrectly? Does the page not load at all? I do not know what you tried. I do not know what your code looks like. Without that information, I would need to walk to your desk, look at your screen, and ask four follow-up questions before I could even start helping.

매 학기 수없이 듣는 질문입니다. 그리고 매번 제 답변은 같습니다. 그 정보만으로는 도울 수 없습니다. "이거"가 뭘 가리키는지 모릅니다. "안 된다"는 게 무슨 의미인지 모릅니다 — 오류가 표시되나요? 잘못 표시되나요? 페이지가 전혀 로드되지 않나요? 무엇을 시도했는지 모릅니다. 코드가 어떻게 생겼는지 모릅니다. 그 정보 없이는 여러분의 자리로 걸어가서 화면을 보고 네 가지 후속 질문을 해야 도울 수 있습니다.

The **engineer-style question** solves this by requiring four pieces of information before the question is asked:

**엔지니어식 질문법**은 질문하기 전에 네 가지 정보를 반드시 포함하도록 요구함으로써 이 문제를 해결합니다:

1. **Situation**: What were you trying to accomplish? Describe the goal, not the symptom. / **발생 상황**: 무엇을 달성하려고 했는가? 증상이 아닌 목표를 설명합니다.
2. **What you tried**: What steps did you take to fix the problem? List them specifically. / **시도해본 것**: 문제를 해결하기 위해 어떤 단계를 거쳤는가? 구체적으로 나열합니다.
3. **Full error message**: Copy and paste the exact error text. Do not paraphrase it. / **에러 메시지 전문**: 정확한 에러 텍스트를 복사-붙여넣기 합니다. 바꿔 말하지 않습니다.
4. **AI result**: Did you ask the AI about this problem? What did it say, and did that advice help or not? / **AI에게 물어본 결과**: 이 문제를 AI에게 물어봤는가? 뭐라고 했고, 그 조언이 도움이 됐는가?

Good question example:

좋은 질문 예:

> "I was trying to display an image in my StackBlitz HTML project. I added an `<img>` tag with a `src` attribute pointing to an image URL I copied from Google. The preview panel went completely blank — no text, no image, nothing. I tried removing the img tag and the rest of the page came back. I tried a different image URL and got the same result. I asked Gemini and it said the image URL might have CORS restrictions. I tried using a direct `.jpg` link from Wikipedia instead, and it still went blank. Here is my current code." — [code pasted below]

> "StackBlitz HTML 프로젝트에서 이미지를 표시하려고 했습니다. Google에서 복사한 이미지 URL을 `src` 속성으로 가진 `<img>` 태그를 추가했습니다. 미리보기 패널이 완전히 공백이 됐습니다 — 텍스트도, 이미지도, 아무것도 없었습니다. img 태그를 제거하니 나머지 페이지가 돌아왔습니다. 다른 이미지 URL을 시도해봤지만 같은 결과가 났습니다. Gemini에게 물어봤더니 이미지 URL에 CORS 제한이 있을 수 있다고 했습니다. Wikipedia에서 `.jpg` 직접 링크를 사용해봤지만 여전히 공백이었습니다. 현재 코드는 다음과 같습니다." — [코드 아래에 붙여넣기]

When you ask this way, I can often diagnose the problem immediately — without leaving my chair. And very often, the act of writing out all four items makes you realize the solution yourself before you even send the question. This is called rubber duck debugging in software engineering, and it works.

이렇게 질문하면 강사가 자리에서 일어나지 않고도 즉시 문제를 진단할 수 있는 경우가 많습니다. 그리고 매우 자주, 네 가지 항목을 작성하는 행위 자체가 질문을 보내기 전에 스스로 해결책을 깨닫게 해줍니다. 소프트웨어 엔지니어링에서 이를 고무 오리 디버깅이라고 하며, 실제로 효과가 있습니다.

In this class, incomplete questions — "it doesn't work" or "I don't understand" without any of the four items — will be politely redirected. Please take two minutes to structure your question with all four elements before asking. You will get better answers faster.

이 수업에서 불완전한 질문 — 네 가지 항목 없이 "안 돼요" 또는 "모르겠어요" — 은 정중하게 돌려드립니다. 질문하기 전에 2분을 들여 네 가지 요소로 질문을 구조화해주세요. 더 빠르게 더 나은 답변을 얻을 것입니다.

### [eCampus Usage / eCampus 사용법 — 4 min]

All official communications for this course — announcements, video uploads, assignment deadlines, grade postings — go through **eCampus**. I will not notify you through text messages, KakaoTalk, or any other channel. eCampus is the single source of truth for this course.

이 수업의 모든 공식 소통 — 공지, 영상 업로드, 과제 기한, 성적 등록 — 은 **eCampus**를 통해 이루어집니다. 문자, 카카오톡, 다른 어떤 채널로도 알리지 않습니다. eCampus가 이 수업의 단일 정보 원천입니다.

There are three things you need to do on eCampus for this course. First, **watch the weekly lecture video** before coming to class. The video for the coming week will be uploaded by 18:00 the day before class. If you do not watch it, you will not be prepared for the hands-on exercises. Second, **check announcements** regularly. If I change a deadline, cancel a class, or upload additional materials, it will appear as an announcement on eCampus. "I didn't see the announcement" is not an accepted reason for missing a deadline. Third, **submit your Micro-Assignment** each week through the eCampus submission box. Emailing your assignment to me directly is not an accepted submission.

이 수업에서 eCampus에서 해야 할 세 가지가 있습니다. 첫째, **주차별 강의 영상**을 수업 전에 시청합니다. 다음 주 영상은 수업 전날 18:00까지 업로드됩니다. 시청하지 않으면 직접 실습에 대비할 수 없습니다. 둘째, **공지를 정기적으로 확인**합니다. 기한 변경, 수업 취소, 추가 자료 업로드는 eCampus 공지로 올라갑니다. "공지를 못 봤어요"는 기한을 놓친 이유로 인정되지 않습니다. 셋째, **마이크로 과제**를 매주 eCampus 제출함을 통해 제출합니다. 강사에게 직접 이메일로 과제를 보내는 것은 인정되는 제출 방식이 아닙니다.

I recommend setting up notifications in your eCampus account so that new announcements send you an alert. Take a moment to verify right now — or during the hands-on session — that this Web Programming course appears in your eCampus enrolled courses list. If it does not appear, come talk to me immediately after class.

새 공지가 올라오면 알림이 오도록 eCampus 계정에서 알림 설정을 해두기를 권장합니다. 지금 바로 또는 실습 시간에 이 웹프로그래밍 과목이 eCampus 수강 목록에 있는지 확인해보세요. 나타나지 않으면 수업 후 즉시 와서 말씀해주세요.

---

## Section 3 — AI Partner & Developer Tools / AI 파트너와 개발 도구 (25 min)

### [StackBlitz — Your Code Environment / StackBlitz — 실습 환경 — 6 min]

For the first half of this semester, from Weeks 1 through 8, you will write all of your HTML and CSS inside **StackBlitz**. StackBlitz is a cloud-based development environment that runs entirely inside your web browser. You do not need to install any software. You do not need to configure anything. You go to `stackblitz.com`, click "New Project," choose a template, and you have a working development environment in about ten seconds.

이번 학기 전반부, 1~8주차 동안 모든 HTML과 CSS를 **StackBlitz** 안에서 작성합니다. StackBlitz는 웹 브라우저 안에서 완전히 실행되는 클라우드 기반 개발 환경입니다. 어떤 소프트웨어도 설치할 필요 없습니다. 아무것도 설정할 필요 없습니다. `stackblitz.com`에 접속하고, "New Project"를 클릭하고, 템플릿을 선택하면 약 10초 안에 작동하는 개발 환경이 생깁니다.

The layout of StackBlitz is divided into three panels. On the left side is the file explorer — a list of all the files in your project. Initially you will see `index.html`, which is the main entry point for every web page. In the center is the code editor, where you type your HTML. On the right side is a live browser preview — every time you make a change to your HTML, the preview updates automatically in real time. You do not need to save your file and refresh the browser. The feedback is instant. This immediate feedback loop is one of the most valuable things about StackBlitz for learning HTML — you can see exactly what each change does the moment you make it.

StackBlitz의 레이아웃은 세 개의 패널로 나뉩니다. 왼쪽에는 파일 탐색기 — 프로젝트의 모든 파일 목록 — 가 있습니다. 처음에는 모든 웹 페이지의 주요 진입점인 `index.html`이 보입니다. 가운데에는 HTML을 타이핑하는 코드 에디터가 있습니다. 오른쪽에는 라이브 브라우저 미리보기가 있습니다 — HTML을 변경할 때마다 미리보기가 실시간으로 자동으로 업데이트됩니다. 파일을 저장하고 브라우저를 새로 고침할 필요가 없습니다. 피드백이 즉각적입니다. 이 즉각적인 피드백 루프가 HTML 학습에서 StackBlitz가 가장 가치 있는 것 중 하나입니다 — 변경을 하는 순간 각 변경이 무엇을 하는지 정확하게 볼 수 있습니다.

The one limitation of StackBlitz that you should be aware of is that each project gets a unique URL in the browser's address bar. That URL is your project's shareable link. If you log out and log back in, or if you access StackBlitz from a different browser, your project is associated with your account. This is why creating a StackBlitz account — even the free tier — is worth doing from the beginning. It ensures your work is saved and accessible from any device.

알아야 할 StackBlitz의 한 가지 제한 사항은 각 프로젝트가 브라우저 주소창에 고유한 URL을 얻는다는 것입니다. 그 URL이 프로젝트의 공유 가능한 링크입니다. 로그아웃하고 다시 로그인하거나, 다른 브라우저에서 StackBlitz에 접속하면, 프로젝트가 계정과 연결됩니다. 이것이 처음부터 StackBlitz 계정 — 무료 티어라도 — 을 만드는 것이 가치 있는 이유입니다. 작업이 저장되고 어떤 기기에서든 접근 가능하도록 보장합니다.

### [GitHub — Your Portfolio / GitHub — 포트폴리오 공간 — 5 min]

**GitHub** is a platform for storing, sharing, and tracking code. It is the most widely used version control platform in the software industry, and it will be your assignment submission system for this entire course.

**GitHub**는 코드를 저장, 공유, 추적하는 플랫폼입니다. 소프트웨어 업계에서 가장 널리 사용되는 버전 관리 플랫폼이며, 이 수업 전체의 과제 제출 시스템이 될 것입니다.

For this course, here is how assignment submission will work. You will create a single **private repository** on GitHub — think of it as a private folder in the cloud. Every week, you will create a new file in that repository. You will then paste the URL of that file into the eCampus submission box. Because you will invite me (`wonhyukc`) as a Collaborator, I have access to view and grade everything in your private repository.

이 수업에서 과제 제출은 이렇게 작동합니다. GitHub에 단일 **Private 저장소**를 만들 것입니다 — 클라우드의 개인 폴더라고 생각하세요. 매주 그 저장소에 새 파일을 만들 것입니다. 그런 다음 그 파일의 URL을 eCampus 제출함에 붙여넣습니다. 저(`wonhyukc`)를 Collaborator로 초대하기 때문에, 저는 여러분의 Private 저장소에 있는 모든 것을 보고 채점할 수 있습니다.

A critical point: if you do not invite me as a Collaborator, your private repository is completely inaccessible to me. I cannot grade what I cannot see. Any submission where the repository is not shared with my account will receive a zero. Please complete this step carefully during today's hands-on session.

중요한 사항: 저를 Collaborator로 초대하지 않으면, 여러분의 Private 저장소는 저에게 완전히 접근 불가능합니다. 볼 수 없는 것은 채점할 수 없습니다. 저장소가 제 계정과 공유되지 않은 제출은 0점을 받습니다. 오늘 실습 시간에 이 단계를 주의 깊게 완료해주세요.

Beyond this course, GitHub functions as a professional portfolio. Increasingly, employers and graduate school admissions reviewers look at GitHub profiles to understand what candidates can do. A GitHub profile with active projects, clear commit histories, and professional repository names communicates technical engagement even before an interview. You are building this habit now, in your first semester.

이 수업 이외에도, GitHub는 전문 포트폴리오 역할을 합니다. 고용주와 대학원 입학 심사관들이 점점 더 GitHub 프로필을 보고 지원자가 무엇을 할 수 있는지 파악합니다. 활성 프로젝트, 명확한 커밋 이력, 전문적인 저장소 이름이 있는 GitHub 프로필은 면접 전에도 기술적 참여도를 보여줍니다. 여러분은 지금 첫 학기에 이 습관을 만들고 있습니다.

### [AI Collaboration Tools / AI 협업 도구 — 5 min]

You are required to use an AI tool in this course. Not using AI is not a neutral choice — it is a disadvantage. Learning to work effectively with AI is itself a learning objective, just as learning HTML is a learning objective.

이 수업에서 AI 도구는 필수로 사용합니다. AI를 쓰지 않는 것은 중립적인 선택이 아닙니다 — 불이익입니다. AI와 효과적으로 협력하는 방법을 배우는 것이, HTML을 배우는 것과 마찬가지로 학습 목표 자체입니다.

The two primary options available to you are:

여러분이 이용할 수 있는 두 가지 주요 옵션은:

| | **ChatGPT** | **Google Gemini** |
|:---|:---|:---|
| Provider | OpenAI | Google |
| Free tier | Yes | Yes (login with Google account) |
| Recommended for | General coding Q&A, explanations | Quick lookups, Google ecosystem integration |

Both work well for the kinds of questions you will ask in this course. Pick one today, create a free account, and make sure you can log in and start a conversation. You may switch between them or use additional tools throughout the semester — Claude at `claude.ai` and Perplexity at `perplexity.ai` are also useful. The minimum requirement is that you have at least one AI tool ready to use by the end of today's class.

두 도구 모두 이 수업에서 묻게 될 종류의 질문에 잘 작동합니다. 오늘 하나를 선택하고, 무료 계정을 만들고, 로그인해서 대화를 시작할 수 있는지 확인하세요. 학기 내내 전환하거나 추가 도구를 사용할 수 있습니다 — `claude.ai`의 Claude와 `perplexity.ai`의 Perplexity도 유용합니다. 최소 요건은 오늘 수업 끝날 때까지 최소 하나의 AI 도구를 사용할 준비가 되어 있는 것입니다.

### [How to Use AI as a Partner / AI를 파트너로 사용하는 방법 — 6 min]

Let me show you two very different ways of using AI, and why they produce completely different outcomes.

AI를 사용하는 두 가지 매우 다른 방법과, 왜 그것이 완전히 다른 결과를 만드는지 보여드리겠습니다.

**The wrong approach**: Type a complete request. Get the output. Copy it. Submit it.

**잘못된 방법**: 완전한 요청을 입력합니다. 출력물을 받습니다. 복사합니다. 제출합니다.

Example: "Build me a webpage with a navigation bar at the top, a hero section with a title and subtitle, and a footer with copyright information."

예시: "상단에 내비게이션 바, 제목과 부제목이 있는 히어로 섹션, 저작권 정보가 있는 푸터가 있는 웹 페이지를 만들어줘."

The AI gives you complete, formatted code. You paste it into StackBlitz. It works. You submit it. What did you learn? Nothing. What can you do with a slightly different problem next week? Nothing. What happens on the exam when a similar structure has a bug? You cannot find the bug because you never understood the structure.

AI가 완전하고 형식화된 코드를 줍니다. StackBlitz에 붙여넣습니다. 작동합니다. 제출합니다. 무엇을 배웠나요? 아무것도 없습니다. 다음 주에 조금 다른 문제로 무엇을 할 수 있나요? 아무것도 없습니다. 시험에서 비슷한 구조에 버그가 있을 때 어떻게 되나요? 구조를 전혀 이해하지 못했기 때문에 버그를 찾을 수 없습니다.

**The right approach**: Use AI as a teacher who explains and demonstrates, not a machine that produces output for you to copy.

**올바른 방법**: AI를 여러분을 위한 출력물을 생산하는 기계가 아니라 설명하고 시범을 보여주는 선생님으로 사용합니다.

Better prompt: "I am a first-year university student learning HTML for the first time. I have seen the `<nav>` tag in HTML examples but I do not understand what it does. Can you explain what `<nav>` is for and how it differs from just using a `<div>`? Please explain why I would choose one over the other."

더 나은 프롬프트: "저는 처음으로 HTML을 배우는 대학교 1학년 학생입니다. HTML 예시에서 `<nav>` 태그를 봤는데 무엇을 하는지 이해하지 못합니다. `<nav>`가 무엇을 위한 것인지, 그냥 `<div>`를 사용하는 것과 어떻게 다른지 설명해줄 수 있나요? 왜 하나를 다른 것보다 선택하는지 설명해주세요."

Now you understand the tag. You can write it yourself next time. You can evaluate whether the AI's suggestion is appropriate for your specific context. You have gained something that belongs to you, not something you borrowed from a machine.

이제 태그를 이해했습니다. 다음에 직접 쓸 수 있습니다. AI의 제안이 특정 상황에 적합한지 평가할 수 있습니다. 기계에서 빌린 것이 아니라, 여러분에게 속하는 무언가를 얻었습니다.

The skill of writing clear, precise, well-structured questions to AI is called **prompting**. Prompting is not magic — it is communication. The same principles that make a good business email also make a good AI prompt. Be specific. State your context. Ask for what you actually need.

AI에게 명확하고 정확하며 잘 구조화된 질문을 작성하는 기술을 **프롬프팅**이라고 합니다. 프롬프팅은 마법이 아닙니다 — 소통입니다. 좋은 비즈니스 이메일을 만드는 원칙이 좋은 AI 프롬프트도 만듭니다. 구체적으로. 상황을 밝히세요. 실제로 필요한 것을 요청하세요.

You will practice prompting every week in the Micro-Assignment. Each week's assignment asks you to document the core question you posed to the AI, evaluate what the AI got right and wrong, and present the final version you verified and modified yourself. This three-part structure is what separates critical AI usage from passive AI consumption.

매주 마이크로 과제에서 프롬프팅을 연습할 것입니다. 매주 과제는 AI에게 던진 핵심 질문, AI가 맞고 틀린 것을 평가하기, 직접 검증하고 수정한 최종 버전을 문서화하도록 요청합니다. 이 세 부분 구조가 비판적 AI 사용과 수동적 AI 소비를 구분하는 것입니다.

### [AI Makes Mistakes / AI는 틀린다 — 4 min]

This is one of the most important things I will tell you all semester, so I want to say it very directly. **AI systems make mistakes with great confidence.** They do not signal uncertainty the way a human expert would. They deliver incorrect information in the same authoritative tone as correct information.

이것은 제가 이번 학기 내내 여러분에게 할 가장 중요한 말 중 하나입니다. 매우 직접적으로 말씀드리겠습니다. **AI 시스템은 매우 자신 있게 실수를 합니다.** 인간 전문가가 그러는 것처럼 불확실성을 신호하지 않습니다. 올바른 정보와 동일한 권위 있는 어조로 잘못된 정보를 전달합니다.

Here are specific examples of how AI fails with HTML and CSS:

HTML과 CSS에서 AI가 실패하는 구체적인 예입니다:

First, it invents attributes that do not exist in the HTML specification. If you ask for an unusual effect, it may generate an HTML attribute that looks plausible but is simply not real. When you paste that into StackBlitz, nothing happens — because the browser has no idea what that attribute means.

첫째, HTML 사양에 존재하지 않는 속성을 만들어냅니다. 특이한 효과를 요청하면 그럴듯해 보이지만 단순히 실재하지 않는 HTML 속성을 생성할 수 있습니다. StackBlitz에 붙여넣으면 아무 일도 일어나지 않습니다 — 브라우저가 그 속성이 무엇을 의미하는지 모르기 때문입니다.

Second, it recommends CSS that is not cross-browser compatible. Some CSS features work in Chrome but not in Firefox or Safari, or only in newer versions of those browsers. The AI will suggest these features without warning you about compatibility issues.

둘째, 크로스 브라우저 호환이 되지 않는 CSS를 권장합니다. 일부 CSS 기능은 Chrome에서는 작동하지만 Firefox나 Safari에서는 작동하지 않거나, 해당 브라우저의 최신 버전에서만 작동합니다. AI는 호환성 문제에 대해 경고하지 않고 이런 기능을 제안합니다.

Third, it describes deprecated approaches as if they are current. HTML4 had certain tags and attributes that were replaced in HTML5. AI training data includes both old and new documentation, and it does not always distinguish between them clearly.

셋째, 더 이상 사용되지 않는 방식을 현재 방식인 것처럼 설명합니다. HTML4에는 HTML5에서 교체된 특정 태그와 속성이 있었습니다. AI 학습 데이터에는 오래된 것과 새로운 것 모두 포함되어 있으며, 명확하게 구분하지 않는 경우가 많습니다.

This is why every piece of code that AI generates must be tested in a browser before you submit it. Copy the code, paste it into StackBlitz, and see what it actually does. Does the preview show what you expected? Does anything break? Are there any error messages in the console? The browser is the final authority on whether HTML is correct — not the AI.

이것이 AI가 생성한 모든 코드를 제출하기 전에 브라우저에서 반드시 테스트해야 하는 이유입니다. 코드를 복사하고, StackBlitz에 붙여넣고, 실제로 무엇을 하는지 보세요. 미리보기가 예상한 것을 보여주나요? 무언가 깨지나요? 콘솔에 오류 메시지가 있나요? 브라우저가 HTML이 올바른지에 대한 최종 권한입니다 — AI가 아니라.

The weekly Micro-Assignment includes an "AI Critique" section specifically because we want you to practice this critical evaluation every single week. Getting comfortable with "what did the AI get wrong?" is not cynicism — it is professional competence.

매주 마이크로 과제에 "AI Critique" 섹션이 포함되어 있는 이유가 이것입니다. 매주 이 비판적 평가를 연습하기를 원하기 때문입니다. "AI가 무엇을 틀렸는가?"에 익숙해지는 것은 냉소주의가 아닙니다 — 그것은 전문적 역량입니다.

### [Micro-Assignment Format / 마이크로 과제 형식 — 2 min]

Starting from Week 2, every Micro-Assignment you submit must use this fixed three-part format:

2주차부터 제출하는 모든 마이크로 과제는 이 고정된 세 부분 형식을 사용해야 합니다:

| Item / 항목 | Content / 내용 |
|:---|:---|
| **AI Prompt** | The core question you posed to the AI this week / 이번 주 AI에게 던진 핵심 질문 |
| **AI Critique** | One sentence: what the AI got right and what it got wrong or oversimplified / 한 문장: AI가 맞은 부분과 틀리거나 지나치게 단순화한 부분 |
| **Final Result** | The code or conclusion you verified and modified yourself / 직접 검증·수정한 최종 코드 또는 결론 |

Length target: approximately **0.5 pages of A4**. The goal is not quantity — it is genuine critical engagement with the AI interaction. One sentence for AI Critique, one block of tested code for Final Result, and a clear record of the prompt. That is the entire format.

분량 목표: **A4 0.5페이지** 내외. 목표는 분량이 아닙니다 — AI 상호작용과의 진정한 비판적 참여입니다. AI Critique에 한 문장, Final Result에 테스트된 코드 한 블록, 프롬프트의 명확한 기록. 전체 형식이 그것입니다.

Week 1 is an exception to this format. This week's tasks — the self-introduction email, the GitHub account verification file, and the web history impressions — do not follow the three-part structure. Starting Week 2, this format applies every week without exception for the entire semester.

1주차는 이 형식에서 예외입니다. 이번 주 과제 — 자기소개 이메일, GitHub 계정 인증 파일, 웹 역사 소감 — 는 세 부분 구조를 따르지 않습니다. 2주차부터 이 형식은 학기 내내 매주 예외 없이 적용됩니다.

### [Closing / 마무리 — 2 min]

Let me give you the five key things to take away from today's session.

오늘 세션에서 가져갈 다섯 가지 핵심을 정리하겠습니다.

One: The web is a client-server document system. Every webpage you have ever visited was an HTML file that a server sent to your browser in response to a request. HTML describes the structure, CSS describes the style, JavaScript adds the behavior. You will learn all three this semester.

하나. 웹은 클라이언트-서버 문서 시스템입니다. 여러분이 방문한 모든 웹 페이지는 서버가 요청에 응답해 브라우저로 보낸 HTML 파일이었습니다. HTML은 구조를, CSS는 스타일을, JavaScript는 동작을 추가합니다. 이번 학기에 이 세 가지를 모두 배웁니다.

Two: This course does not require memorizing code. It requires the ability to read, evaluate, and correct what AI produces. That judgment ability is what makes this skill set valuable for the next decade.

둘. 이 수업은 코드 암기가 필요하지 않습니다. AI가 생산하는 것을 읽고, 평가하고, 수정하는 능력이 필요합니다. 그 판단 능력이 이 기술 셋을 앞으로 10년간 가치 있게 만드는 것입니다.

Three: Business email principles and engineer-style questioning are the communication standards for every interaction in this course — with me, with teammates, and eventually with employers.

셋. 비즈니스 이메일 원칙과 엔지니어식 질문법은 이 수업의 모든 상호작용에서의 소통 기준입니다 — 강사와, 팀원과, 그리고 결국 고용주와의 상호작용에서도.

Four: Your development environment for the first eight weeks is StackBlitz. Your assignment submission system is GitHub. Your course communication platform is eCampus. Learn where each thing lives.

넷. 처음 여덟 주의 개발 환경은 StackBlitz입니다. 과제 제출 시스템은 GitHub입니다. 수업 소통 플랫폼은 eCampus입니다. 각각 무엇이 어디에 있는지 파악하세요.

Five: AI is a powerful tool that makes mistakes confidently. Test everything in a browser. Use AI to understand, not to copy.

다섯. AI는 자신 있게 실수하는 강력한 도구입니다. 모든 것을 브라우저에서 테스트하세요. AI를 복사하기 위해서가 아니라 이해하기 위해 사용하세요.

During the hands-on session that follows, you will open StackBlitz and type your first HTML tag, create your GitHub account and private repository, invite me as a Collaborator, verify your eCampus enrollment, and set up your AI account. All of this happens today.

이어지는 실습 세션에서 StackBlitz를 열고 첫 번째 HTML 태그를 입력하고, GitHub 계정과 Private 저장소를 만들고, 저를 Collaborator로 초대하고, eCampus 등록을 확인하고, AI 계정을 설정합니다. 이 모든 것이 오늘 이루어집니다.

Before next class, watch the **wb02 lecture video on eCampus**. Next week you will build the skeleton of an online business card using `<h1>`, `<p>`, and `<img>` tags.

다음 수업 전에 eCampus에서 **wb02 강의 영상**을 반드시 시청해 오세요. 다음 주에는 `<h1>`, `<p>`, `<img>` 태그를 사용해 온라인 명함 뼈대를 만들어봅니다.

Good work today.

수고하셨습니다.
