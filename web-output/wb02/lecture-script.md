# Week 2: HTML Basics - Building the Skeleton
# 2주차: HTML 기초 - 뼈대를 세우자

## [S1] The Skeleton of HTML and Text Tags 
## [S1] HTML의 뼈대 구조 및 텍스트 태그

*(Instructor Note: Start with a warm, welcoming tone, specifically acknowledging our international students joining from abroad due to visa issues. Use a clear, measured pace.)*
*(강사 참고: 비자 문제로 인해 해외에서 접속 중인 외국인 유학생들을 구체적으로 언급하며, 따뜻하고 환영하는 어조로 시작. 명확하고 일관된 속도로 말할 것.)*

Hello everyone, and welcome to week two of Web Programming! It is wonderful to see all your faces on the screen today. I know many of you are joining us from your home countries—India, Nepal, Bangladesh, Vietnam, and many others. I want to tell you how much I appreciate your dedication. Joining a live online class across different time zones is not easy, but you are all doing a fantastic job. How is the weather where you are? I hope you are all staying healthy and safe. Even though we are not physically in the same room, this digital space is our classroom, and I am here to support you every step of the way. If you ever have connection issues or something is unclear, please do not hesitate to raise your virtual hand or type in the chat. We are a team, and we will learn this together.
여러분 안녕하세요, 웹프로그래밍 2주차에 오신 것을 환영합니다! 오늘 화면으로 여러분의 얼굴을 보게 되어 정말 기쁩니다. 인도, 네팔, 방글라데시, 베트남 등 각자의 고국에서 접속하고 있는 학생들이 많다는 것을 알고 있습니다. 여러분의 열정에 얼마나 깊이 감사드리는지 꼭 전하고 싶었습니다. 시차가 있는 짐작하기 어려운 상황에서 실시간 온라인 수업에 참여하는 것이 결코 쉬운 일은 아니지만, 여러분 모두 정말 훌륭하게 해내고 계십니다. 여러분이 계신 곳의 날씨는 어떤가요? 모두 건강하고 안전하게 지내고 있기를 바랍니다. 비록 우리가 물리적으로 같은 방에 있지는 않지만, 이 디지털 공간이 바로 우리의 교실이며, 저는 여러분들의 모든 과정을 돕기 위해 이 자리에 있습니다. 접속에 문제가 생기거나 설명이 명확하지 않다면 언제든지 가상 손을 들거나 채팅창에 입력해 주세요. 우리는 하나의 팀이며, 이 모든 것을 함께 배워나갈 것입니다.

Last week, we talked about what it means to be a developer in the era of Artificial Intelligence. We discussed flipped learning, professional communication, and how to ask questions like an engineer. We also touched upon the very basic idea that learning to code is not about memorizing syntax, but rather about learning how to communicate with computers logically. Today, we are taking our very first concrete step into the world of web development. We are going to learn HTML.
지난주에 우리는 인공지능 시대에 개발자가 된다는 것이 어떤 의미인지에 대해 이야기했습니다. 플립 러닝, 프로페셔널한 커뮤니케이션, 그리고 엔지니어답게 질문하는 방법에 대해서도 논의했었죠. 또한 코딩을 배운다는 것은 단순한 문법 암기가 아니라, 컴퓨터와 논리적으로 소통하는 법을 배우는 것이라는 아주 기본적인 개념도 다루었습니다. 오늘, 우리는 웹 개발의 세계로 향하는 첫 번째 구체적인 발걸음을 내딛으려 합니다. 바로 HTML을 배울 것입니다.

*(Instructor Note: Pause, look directly into the camera, and smile.)*
*(강사 참고: 잠시 멈추고 카메라를 정면으로 응시하며 미소 짓기.)*

So, what exactly is HTML? It stands for HyperText Markup Language. But do not worry about memorizing that long name. Instead, I want you to think of HTML as the absolute core skeleton of every single website you have ever visited. Imagine building a house. Before you can paint the walls, before you can arrange the furniture, you must first build the foundation and the wooden or steel frame. You must erect the walls and the roof structure. HTML is that frame. It tells the browser—whether it is Chrome, Safari, or Edge—what things are. It says, "This is a title," "This is a paragraph," or "This is an image." It does not care about colors or beauty; it only cares about structure and meaning.
그렇다면 HTML이란 정확히 무엇일까요? HyperText Markup Language의 약자입니다. 하지만 이 긴 이름을 외우려고 걱정할 필요는 전혀 없습니다. 대신, HTML을 여러분이 지금까지 방문했던 모든 웹사이트의 '가장 핵심적인 뼈대(Skeleton)'라고 생각해 주었으면 합니다. 집을 짓는다고 상상해 보세요. 벽에 페인트를 칠하거나 가구를 배치하기 전에, 가장 먼저 기초를 다지고 나무나 철골로 뼈대를 세워야만 합니다. 벽을 세우고 지붕의 골격을 만들어야 하죠. HTML이 바로 그 뼈대입니다. 크롬이든, 사파리든, 엣지든 상관없이 웹 브라우저에게 '이것들이 무엇인지' 알려주는 역할을 합니다. 브라우저에게 "이건 제목이야", "이건 문단이야", 혹은 "이건 이미지야"라고 말해줍니다. HTML은 색상이나 아름다움에는 관심이 없습니다. 오로지 구조와 의미에만 집중합니다.

Today, we will be using StackBlitz. As I mentioned last week, you do not need to install complicated software on your computers right now. StackBlitz is a magical tool that lives entirely inside your web browser. Let's open it up together. 
오늘은 StackBlitz를 사용할 예정입니다. 지난주에 말씀드렸듯이, 당장 컴퓨터에 복잡한 소프트웨어를 설치할 필요가 없습니다. StackBlitz는 여러분의 웹 브라우저 안에서 완벽하게 구동되는 마법 같은 도구입니다. 다 같이 한 번 열어볼까요.

*(Instructor Note: Share your screen, showing the StackBlitz website. Slowly click on "HTML/JS/CSS" to create a new blank project.)*
*(강사 참고: 화면을 공유하여 StackBlitz 웹사이트를 보여줌. 천천히 "HTML/JS/CSS"를 클릭하여 비어 있는 새 프로젝트를 생성함.)*

Look at my screen. I am clicking on the 'HTML, JS, CSS' option. Instantly, we have a workspace. On the left side, we type our code. On the right side, we see the results immediately. It is like having a translation window. You speak to the computer on the left, and the computer shows you its understanding on the right. 
제 화면을 보세요. 저는 지금 'HTML, JS, CSS' 옵션을 클릭하고 있습니다. 순식간에 작업 공간이 생겨났죠. 왼쪽에는 코드를 입력하고, 오른쪽에는 그 결과가 즉시 나타납니다. 일종의 실시간 번역 창을 가진 것과 같습니다. 왼쪽에서 번역기에게 말을 걸면, 컴퓨터가 자신이 이해한 내용을 오른쪽 화면에 보여주는 것입니다.

Now, let us look at the fundamental architecture of an HTML document. I like to use the analogy of a human body, because it is something we all understand perfectly, regardless of our cultural background. Every proper HTML document has three main parts: The `<html>` tag, the `<head>` tag, and the `<body>` tag. Let me type them out for you, nice and slow.
이제, HTML 문서의 근본적인 구조(Architecture)를 살펴봅시다. 저는 이것을 인체에 비유하는 것을 좋아합니다. 왜냐하면 문화적 배경과 무관하게 우리 모두가 완벽하게 이해할 수 있는 비유이기 때문이죠. 제대로 된 HTML 문서라면 반드시 갖춰야 할 세 가지 핵심 부분이 있습니다. 바로 `<html>` 태그, `<head>` 태그, 그리고 `<body>` 태그입니다. 여러분을 위해 아주 천천히 타이핑해 보겠습니다.

*(Instructor Note: Delete all existing code in the StackBlitz editor to start from a completely blank slate. Type the basic HTML structure slowly.)*
*(강사 참고: 백지상태에서 시작하기 위해 StackBlitz 에디터의 기존 코드를 전부 지움. 기본적인 HTML 구조를 천천히 타이핑함.)*

```html
<html>
  <head>
  </head>
  <body>
  </body>
</html>
```

First, we have the `<html>` tag. Notice that it wraps around everything else. There is an opening `<html>` at the top, and a closing `</html>` at the very bottom. The closing tag always has that forward slash `/`. This is the skin of our human. It contains the entire person. The browser sees this and says, "Aha! Everything inside here is an HTML document."
가장 먼저 `<html>` 태그가 있습니다. 이 태그가 다른 모든 것을 감싸고 있다는 사실에 주목하세요. 맨 위에 여는 `<html>`이 있고, 맨 아래에 닫는 `</html>`이 있습니다. 닫는 태그에는 항상 슬래시 `/` 기호가 들어갑니다. 이것은 우리 인간의 '피부'와도 같습니다. 전체 사람을 감싸고 있죠. 브라우저는 이것을 보고 "아하! 이 안에 있는 모든 것이 하나의 HTML 문서구나."라고 인식합니다.

Next, inside the `<html>` tag, we have the `<head>`. Think of this as the human brain. The brain is incredibly important, right? It holds our memories, our identity, and our instructions for how our body should function. But, when you look at a person, you do not actually see their brain. You see their face, their hands, their clothes. The `<head>` tag is exactly like that. It contains metadata—which is data about data. It holds the title of the web page, links to stylesheets, and settings for search engines. But none of the content inside the `<head>` is actually displayed on the white canvas of the web page. It operates behind the scenes.
다음으로, `<html>` 태그 안에는 `<head>`가 있습니다. 이것을 인간의 '뇌'라고 생각해 보세요. 뇌는 엄청나게 중요하죠? 우리의 기억, 정체성, 그리고 몸이 어떻게 기능해야 하는지에 대한 지시 사항들을 담고 있습니다. 하지만, 우리가 어떤 사람을 바라볼 때 실제로 그 사람의 뇌를 보지는 못합니다. 얼굴과 손, 옷차림을 보죠. `<head>` 태그가 딱 그렇습니다. 여기에는 메타데이터(데이터에 대한 데이터)가 들어갑니다. 웹 페이지의 제목, 스타일시트 링크, 검색 엔진을 위한 설정 등을 담고 있죠. 하지만 `<head>` 안에 있는 어떤 내용도 웹 페이지의 하얀 캔버스 화면상에 실제로 나타나지는 않습니다. 철저하게 무대 뒤에서(Behind the scenes) 작동합니다.

Finally, we have the `<body>` tag. The body contains the meat and bones. It contains the text, the images, the videos, the buttons—everything that your users will actually see and interact with. If you want something to appear on the screen, it absolutely must go inside the `<body>` tags. If you put it outside, the browser will get very confused and angry.
마지막으로 `<body>` 태그가 있습니다. 바디(Body)에는 살과 뼈가 담겨 있습니다. 텍스트, 이미지, 비디오, 버튼 등 여러분의 사용자가 실제로 보고 상호작용하게 될 '모든 것'이 들어갑니다. 화면에 무언가 나타나게 하고 싶다면, 반드시 `<body>` 태그 안쪽에 작성해야만 합니다. 만약 바깥에 작성한다면 브라우저는 매우 혼란스럽고 화를 내게 될 것입니다.

Let's prove this. Let's write some text. I am going to introduce you to our first text tags: The `<h1>` tag and the `<p>` tag. The "h" stands for heading, and the "1" means it is the most important, biggest heading. Just like a newspaper has a massive headline at the top, our web page can have an `<h1>`. Let's type this inside the `<body>`.
이 사실을 한 번 증명해 봅시다. 글을 좀 써볼 텐데요. 첫 번째 텍스트 태그 부류인 `<h1>` 태그와 `<p>` 태그를 소개하겠습니다. "h"는 Heading(제목)을 의미하고, "1"은 가장 중요하고 가장 크다는 뜻입니다. 신문의 맨 위를 장식하는 커다란 헤드라인 기사 제목처럼, 우리의 웹 페이지도 `<h1>`을 가질 수 있죠. 이것을 `<body>` 안에 타이핑해 보겠습니다.

*(Instructor Note: Slowly type an `<h1>` heading inside the `<body>` tag. Let the students watch the output update live on the right screen.)*
*(강사 참고: `<body>` 태그 안에 `<h1>` 제목 태그를 천천히 타이핑. 오른쪽 화면에 결과가 실시간으로 업데이트되는 것을 학생들이 지켜보게 함.)*

```html
<body>
  <h1>Welcome to Wonhyuk's Profile</h1>
</body>
```

Look at the right side of the screen! The moment I type the closing `</h1>` tag, the text appears in huge, bold letters. The browser understood our command. It knew that because we wrapped our text in `<h1>` tags, we wanted it to be treated as a major title. That is the power of markup. We are 'marking up' the text with specific meaning.
화면 오른쪽을 보세요! 제가 닫는 `</h1>` 태그를 타이핑하는 순간, 거대한 굵은 글씨로 텍스트가 나타납니다. 브라우저가 우리의 명령을 완벽하게 이해했네요. 우리가 텍스트를 `<h1>` 태그로 감쌌기 때문에, 브라우저는 이것을 가장 중요한 메인 타이틀로 대우해야 한다는 것을 알게 된 것입니다. 이것이 바로 마크업(Markup)의 숨겨진 힘입니다. 우리는 특정한 의미를 부여하여 텍스트를 '마크업(표시)'하고 있는 것입니다.

Now, a title alone is not very informative. We need a paragraph. The tag for a paragraph is extremely simple: `<p>`. Let's add a short introduction right below the heading.
자, 그런데 제목만 덩그러니 있으면 많은 정보를 주지 못하죠. 우리는 문단이 필요합니다. 문단을 나타내는 태그는 극도로 단순합니다. 바로 `<p>`입니다. 제목 바로 아래에 짧은 소개글을 추가해 봅시다.

*(Instructor Note: Type a `<p>` tag below the `<h1>` with a few sentences.)*
*(강사 참고: `<h1>` 태그 아래에 몇 문장의 텍스트를 담은 `<p>` 태그를 타이핑함.)*

```html
<body>
  <h1>Welcome to Wonhyuk's Profile</h1>
  <p>Hello! My name is Wonhyuk William Chung. I am a university instructor. I love learning new things and helping students discover the magic of coding.</p>
</body>
```

Do you see the difference? The text inside the `<p>` tag is much smaller, normal-sized text. It is formatted as a block of text. This is how you structure a document. You use `<h1>` for the main title, maybe `<h2>` for a subtitle, and `<p>` for the actual reading content. Just like cooking a recipe, if you use the right ingredients in the right order, the final dish will turn out perfectly. 
차이점이 보이시나요? `<p>` 태그 안의 텍스트는 훨씬 작고 평범한 크기입니다. 하나의 텍스트 블록 형태로 딱 맞게 포맷팅되었죠. 이것이 바로 우리가 문서를 구조화하는 기본적인 방식입니다. 메인 제목에는 `<h1>`을 쓰고, 소제목이 필요하다면 `<h2>`를 쓰고, 실제 읽어야 할 본문에는 `<p>` 구문을 사용합니다. 요리 레시피를 따라 요리하는 것과 마찬가지입니다. 올바른 재료를 제 순서에 맞게 잘 활용한다면 최종 요리는 완벽하게 완성될 것입니다.

I want you guys to think about this logically. What if I forgot to put the closing `</h1>` tag? Does anyone want to guess what the browser would do? If I do not tell the browser where the massive heading stops, it will simply assume everything that follows is also part of that giant title. 
여러분이 이 사실을 다분히 논리적으로 생각해 보기를 바랍니다. 만약 제가 닫는 `</h1>` 태그를 넣는 것을 아예 깜빡했다면 어떻게 될까요? 브라우저가 어떤 행동을 취할지 짐작이 가시는 분 있나요? 만약 제가 브라우저에게 이 거대한 제목이 어디서 끝나는지 알려주지 않는다면, 브라우저는 그 뒤에 나오는 모든 텍스트 역시 그 거대한 타이틀의 일부라고 단순히 단정 지어 버릴 것입니다.

*(Instructor Note: Intentionally delete the `</h1>` closing tag to demonstrate the error.)*
*(강사 참고: 일부러 `</h1>` 닫는 태그를 지워서 화면에 발생하는 에러 현상을 그대로 보여줌.)*

Watch this. I delete the slash and the h1. Suddenly, my entire paragraph turns into giant, bold text. This is a very common mistake for beginners. Whenever your web page looks crazy, the first thing you should check is whether you properly closed all your tags! We are speaking a language of strict logic. Open the door, put something inside, close the door. Always close the door!
이 화면을 보세요. 제가 슬래시와 h1 태그를 지웠습니다. 갑자기 제 문단 전체가 거대하고 굵은 글씨체로 변해 버렸죠. 이것은 초보자들이 가장 흔하게 겪는 실수입니다. 여러분이 만든 웹 페이지의 모습이 뭔가 미쳐 날뛰는 것처럼 보일 때 가장 먼저 확인해야 할 일은, 바로 여러분이 모든 태그를 제대로 닫았는지를 점검하는 것입니다! 우리는 지금 대단히 엄격한 논리의 언어로 말하고 있는 셈입니다. 문을 열고, 그 안에 무언가를 넣고, 다시 문을 닫는다. 항상 문을 제대로 닫아 주셔야 합니다!


## [S2] Adding Media and Debugging Broken Images
## [S2] 이미지 태그 및 버그 수정 데모

*(Instructor Note: Take a quick sip of water. Transition smoothly from text tags to media tags. Display an engaging image of a famous landmark or a cute animal to grab their attention first.)*
*(강사 참고: 물을 한 모금 마시며 텍스트 태그에서 미디어 태그로 자연스럽게 전환. 시선을 사로잡을 수 있는 유명한 랜드마크나 귀여운 동물 사진 이미지를 가장 먼저 띄울 것.)*

Alright, we have successfully built our text skeleton. We have a solid `<h1>` heading and a descriptive `<p>` paragraph. But let's be honest, a website with only text is incredibly boring. It looks like a document from 1995! To make a web page truly come alive, we need media. Specifically, we need images. 
여러분, 이제 텍스트 뼈대를 세우는 데까지 완벽하게 성공했습니다. 확실한 `<h1>` 제목과 충분한 설명이 들어간 `<p>` 문단도 있죠. 하지만 솔직히 말해서 텍스트만 있는 웹사이트는 지루하기 짝이 없습니다. 1995년대 문서처럼 보이죠! 웹페이지를 '살아 숨 쉬게' 만들려면 우리는 미디어가 필요합니다. 구체적으로는 바로 '이미지'가 필요하죠.

The tag we use to add images is naturally `<img>`, short for image. However, the image tag is a very special exception in the world of HTML. Earlier, I told you that we must always "open the door and close the door." We opened `<h1>` and we closed `</h1>`. But the `<img>` tag is what we call an "empty tag" or a "self-closing tag." It has no closing tag whatsoever. Why? 
우리가 이미지를 추가하기 위해 필연적으로 사용하는 태그는 'image'의 줄임말인 `<img>` 태그입니다. 그런데 이 이미지 태그는 HTML의 세계에서 대단히 독특한 예외에 속합니다. 제가 아까 무조건 "문을 열고 나서 닫아야 한다"고 말씀드렸죠. `<h1>`을 열고 `</h1>`을 닫았던 것처럼 말입니다. 하지만 `<img>` 태그는 흔히 '빈 태그(empty tag)' 혹은 '셀프 클로징 태그(self-closing tag)'라고 부릅니다. 이 녀석에게는 닫는 태그가 아예 없습니다. 왜 그럴까요?

Think about it logically. With text, you put words *inside* the tags, between the opening and the closing points. But an image is not text. You cannot type a picture. You are simply instructing the browser to go grab an image file from somewhere and display it right at that spot. There is no "inside" content to wrap. The tag itself stands alone. Let me show you how it works.
이것도 논리적으로 한 번 생각해 보세요. 텍스트의 경우 열고 닫는 지점 그 '안쪽 공간'에 단어들을 집어넣습니다. 하지만 이미지는 텍스트가 아닙니다. 사진을 타자로 칠 수는 없으니까요. 여러분은 그 자리에 단순히 어딘가에서 이미지 파일을 끌어와 보여 달라고 브라우저에게 지시를 내리고 있을 뿐입니다. 즉, 감싸야 할 내부 콘텐츠 자체가 존재하지 않습니다. 태그 그 자체가 독립적으로 서 있는 셈이죠. 어떻게 작동하는지 바로 보여드리겠습니다.

*(Instructor Note: Back to the StackBlitz code. Type an empty `<img>` tag and explain attributes.)*
*(강사 참고: 다시 StackBlitz 코드로 전환. 비어 있는 `<img>` 태그를 타이핑하고 속성에 대해 설명함.)*

If I just type `<img >`, absolutely nothing happens on the right side. The browser knows I want to show an image, but it does not know *which* image to show. To tell the browser where the image lives, we need to introduce a new concept: Attributes. Attributes provide additional secret information inside a tag. They are like adjectives. For the image tag, the most critical attribute is `src`, which stands for source. 
만약 제가 단순히 `<img >`라고만 타이핑한다면, 화면 오른쪽에서는 아무런 일도 발생하지 않습니다. 브라우저는 제가 여기에 무언가 이미지를 보여주고 싶어 한다는 사실은 알았지만, '어떤' 이미지를 띄워야 할지 모르는 상태입니다. 브라우저에게 이 이미지가 대체 어디에 살고 있는지 알려주기 위해서, 우리는 여기서 '속성(Attribute)'이라는 새로운 개념을 도입해야만 합니다. 속성은 태그 안쪽에 또 다른 은밀한 추가 정보를 제공합니다. 마치 형용사와 같은 역할을 하죠. 이미지 태그에 있어 가장 결정적이고 치명적인 속성은 소스(Source)의 약자인 `src`입니다.

Before we write the source, we need to distinguish between two ways to link an image: an Absolute Path and a Relative Path. Let's use an easy analogy. An absolute path is like an international mailing address: "123 Seoul Street, South Korea, Planet Earth." It does not matter where you currently are in the world; if you follow that absolute address, you will find the building. In the web world, an absolute path is a full URL starting with `https://`. You are pointing to an image living on another server somewhere on the internet.
소스를 작성하기 전에, 우리는 이미지를 연결하는 두 가지 상반된 방식의 차이를 인지해야 합니다. 바로 절대경로(Absolute Path)와 상대경로(Relative Path)입니다. 쉬운 비유를 하나 들어볼게요. 절대경로는 국제 우편물의 주소와 같습니다. "대한민국 서울특별시 지구별 몇 번지" 전 세계 어디에 있든 상관없이 당신이 저 절대 우편 주소만 따라간다면 무조건 그 건물을 찾아낼 수 있겠죠. 웹 생태계 안에서의 절대경로란, `https://`로 시작하는 완전하고 독립적인 전체 URL 링크 본체를 뜻합니다. 즉 인터넷 어딘가의 다른 서버에 떡하니 살고 있는 이미지를 가리키고 있는 것이죠.

A relative path, on the other hand, is like giving someone directions relative to where you are currently standing: "Go out the door, take a left, and it is the second room on the right." It only makes sense if you know the starting point. In coding, a relative path is used when the image file is saved in the exact same folder as your HTML file. Today, to keep things simple, we will use an absolute path. Let's find a beautiful picture of a puppy on Google.
반면에 상대경로는 현재 당신이 발을 딛고 서 있는 위치를 기준으로 누군가에게 길을 안내해주는 것과 정확히 같습니다. "문 밖으로 나가서 왼쪽으로 꺾은 다음, 오른쪽에 있는 두 번째 방입니다." 이것은 안내를 시작하는 첫 출발점을 미리 알고 있어야만 말이 되는 개념이죠. 코딩에 있어서 언제 상대경로가 주로 쓰이냐면, 그 이미지 파일이 여러분의 HTML 문서와 아예 똑같은 폴더 속에 나란히 저장되어 있을 때 사용됩니다. 하지만 오늘은 복잡함을 덜기 위해 단순하게 절대경로만 활용하도록 하겠습니다. 구글에서 예쁜 강아지 사진을 하나 찾아볼게요.

*(Instructor Note: Search for a free stock image of a puppy. Right-click and select 'Copy Image Address'. Paste it into the `src` attribute.)*
*(강사 참고: 구글에서 무료 저작권의 귀여운 강아지 사진을 검색함. 마우스 우클릭을 누르고 '이미지 주소 복사'를 선택함. 그것을 `src` 속성에 붙여넣기 함.)*

```html
<img src="https://images.unsplash.com/photo-puppy.jpg">
```

I right-click the image, select "Copy Image Address", and now I paste that long, absolute URL inside the quotation marks of my `src` attribute. Boom! The moment I close the quote, the beautiful puppy appears on our web page. This is the magic of linking. Our HTML file is incredibly small because it does not actually contain the picture. It merely points an invisible arrow to the picture's location.
제가 사진을 향해 우클릭을 하고, "이미지 주소 복사"를 누른 다음, 제 `src` 속성의 따옴표 안쪽에 길고 긴 절대경로 URL을 비로소 붙여넣었습니다. 짠! 따옴표를 닫은 그 순간, 아름다운 강아지가 우리의 웹 페이지에 등장했습니다. 이것이 바로 링크의 기적 같은 마법입니다. 여러분의 HTML 파일 자체의 용량은 믿을 수 없을 만큼 턱없이 작습니다. 왜냐하면 실제로 그 사진을 파일 안에 포함하지 않고 있기 때문이죠. 우리의 코드는 단지 그 사진의 위치를 향해 안 보이는 투명한 화살표를 세게 가리키고 있을 뿐입니다.

But wait, what happens if we make a mistake? What if I accidentally delete just one letter from this URL?
그런데 잠깐, 만약 우리가 실수를 한다면 어떤 끔찍한 일이 벌어질까요? 제가 무실수로 이 URL 주소에서 단 한 글자라도 쏙 빼먹고 지워버린다면?

*(Instructor Note: Intentionally delete a single character from the URL string to break the link. The image will vanish, replaced by a broken image icon.)*
*(강사 참고: 의도적으로 URL 문자열 가운데서 한 글자만 지워서 연결을 파괴함. 이미지 사진이 증발하면서 엑스박스(깨진 이미지) 아이콘으로 교체됨.)*

Oh no! Where did the puppy go? We now have an ugly, broken image icon. This is famously called a "dead link" or the "X-box error". As a beginner, seeing this can be terrifying. You might think you broke the entire internet. However, as an engineer, when you see an error like this, you should not panic. You should smile.
오 안돼! 이 강아지가 대체 어디로 도망간 걸까요! 이제 우리 눈앞에는 끔찍하게 안 예쁜 '깨진 이미지 아이콘'만 남아버렸네요. 이것은 흔히 말하는 '데드 링크(죽어버린 링크)'라 불리거나 소위 '엑스박스 에러 현상'입니다. 코딩 초보자 입장에서는 이걸 목격하면 섬찟하고 겁이 덜컥 날 수도 있습니다. 인터넷 전체를 망가뜨렸다고 생각할지도 모르죠. 하지만 진정한 엔지니어의 입장에서는, 이렇게 치명적인 에러를 보게 되었을 때 절대 당황해서는 안 됩니다. 오히려 씩 하고 미소를 지어야 합니다.

Why? Because the browser is talking to you. It is saying, "Master, I followed the exact address you gave me, but nobody was home!" An error is simply a piece of data. It points you directly to the problem. If an image is broken, you know with 100% certainty that the issue is inside your `src` attribute. It is a typo. Let's look closely at the path... Ah, I deleted the 'h' in 'photo'. I will type it back in...
대체 왜죠? 왜냐하면 브라우저가 당신에게 분명하게 말을 걸고 있기 때문입니다. "주인님, 방금 저한테 건네주신 주소 그대로 따라가 봤는데 집에 찾아보니 아무도 없었어요!"라고 말입니다. 에러 표시는 단지 일종의 데이터에 불과합니다. 그것은 곧장 문제의 원인을 다이렉트로 가리키고 있는 지표이기도 하죠. 만약 이미지가 깨져 있다는 것은, 여러분의 100% 확신을 가지고 `src` 속성 내부를 다시 살펴봐야 한다는 뜻이 됩니다. 이것은 단순한 오타입니다. 경로 주소를 눈 크게 뜨고 다시 자세히 봅시다... 아하! 제가 'photo'라는 단어의 'h' 하나를 지워버렸었군요. 다시 h를 타이핑해서 되돌리면...

*(Instructor Note: Type the missing letter back. The image reappears instantly.)*
*(강사 참고: 빠뜨린 글자를 다시 기입함. 이미지가 다시금 팝업처럼 짠 하고 나타남.)*

And we are back! Debugging is an enormous part of programming. It is like being a detective. You look for clues, you form a hypothesis ("maybe there is a typo"), and you test it. Never be afraid of making mistakes. The more errors you encounter and fix today, the faster you will become an expert tomorrow.
그리고 다시 살아 돌아왔군요! 디버깅(Debugging), 즉 벌레 잡는 과정은 프로그래밍의 엄청나게 방대한 비중을 차지하는 여정입니다. 마치 탐정이나 명탐정 코난이 되는 것과 똑같습니다. 단서를 찾고, "혹시 오타가 난 거 아닐까?" 하는 가설을 세운 후 직접 테스트해 보는 무한 반복이죠. 결코 실수하는 것을 꺼리거나 두려워하지 마세요. 오늘 여러분이 더 무수히 많은 에러를 마주하고 해결해 볼수록, 내일의 당신은 훨씬 더 빠르고 눈부신 웹 전문가로 거듭나 있을 테니까요.


## [S3] Building Your Digital Business Card & AI Debugging
## [S3] 포트폴리오 명함 조립 및 AI 비평 훈련

*(Instructor Note: Now, bring everything together. Open a deliberately broken HTML template for a digital business card. The template should be missing a `<p>` tag and an `<img>` tag.)*
*(강사 참고: 자, 이제 배운 모든 것을 하나로 모을 차례입니다. 고의적으로 망가뜨려 둔 디지털 명함용 HTML 템플릿 코드를 엽니다. 이 템플릿에는 핵심 `<p>` 태그와 `<img>` 태그가 누락되어 있어야 합니다.)*

For our final section today, we are going to combine all the basic tags we just learned—`<html>`, `<head>`, `<body>`, `<h1>`, `<p>`, and `<img>`—to actually build something useful. We are going to build the skeleton of an online digital business card. Think of this as the very first draft of your personal portfolio website, which we will continue to expand over the next 14 weeks. 
오늘의 마지막 섹션에서는 기왕 배운 `<html>`, `<head>`, `<body>`, `<h1>`, `<p>`, 그리고 `<img>` 등의 기본 태그들을 몽땅 결합해서 '실제 쓸모 있는 무언가'를 만들어 볼 참입니다. 우리는 온라인 디지털 명함의 뼈대를 조립할 것입니다. 앞으로 다가올 14주 동안 계속해서 확장하고 살을 붙여나갈 여러분만의 '포트폴리오 웹사이트 초안'이라고 생각해 주시면 되겠습니다.

I have prepared a template line of code for a handsome, basic business card. However... it is currently broken. I have deliberately deleted some incredibly crucial tags. My challenge to you, as junior engineers, is to look at the screen and visually debug the issue alongside me right now. Let me run this template in StackBlitz.
자, 제가 여러분을 위해 기본적이면서 꽤 근사한 명함 템플릿 한 토막을 미리 준비해왔습니다. 그런데... 이게 지금 엉망으로 고장 나 있습니다. 제가 아주 의도적이고 악랄하게 핵심적인 태그 몇 개를 쏙 빼버렸거든요. 주니어 엔지니어인 여러분에게 던지는 저의 도전 과제입니다. 지금 당장 저와 함께 이 화면을 시각적으로 디버깅하고 문제를 찾아내 보세요. 이 템플릿 코드를 StackBlitz 안에서 실행시켜 보겠습니다.

*(Instructor Note: Paste the broken business card HTML code that renders awkwardly on the screen. Let the students look at the horrible layout for a few seconds.)*
*(강사 참고: 화면에 상당히 이상하게 구동되는, 박살 난 명함 HTML 코드를 붙여넣습니다. 학생들이 그 끔찍한 레이아웃을 몇 초간 조용히 지켜볼 시간을 줍니다.)*

The title says "CEO of Nothing," which is a great start. But look below it. There is just a giant wall of messy text. "Contact me at... My favorite things are..." It is all crammed into one continuous line. And where is the profile picture? There is no face at all to this business card. A business card without a picture and nicely separated text is not professional; it is just a ransom note!
타이틀에 "CEO of Nothing (아무것도 아닌 것의 대표)"라고 훌륭하게 적혀 있네요. 시작은 참 좋습니다만 그 아래를 주목해 보시죠. 그저 거대한 텍스트의 벽이 지저분하게 늘어서 있습니다. "연락처는... 내가 좋아하는 것들은..." 이 모든 것들이 숨 막히게 한 줄로 다닥다닥 욱여넣어져 있죠? 게다가 프로필 사진은 대체 어디 간 건가요? 명함인데 얼굴이 하나도 없네요. 사진도 없고 텍스트가 예쁘게 분리되지도 않은 명함은 전문적이지 못한 것을 넘어서, 그냥 유괴범의 협박 편지처럼 보입니다!

Let's read the code from the top to bottom. It is a fundamental skill for an engineer to trace the execution step by step. We have the `<html>` open. Good. We have the `<head>`. Good. The `<body>` is open. We see the `<h1>CEO of Nothing</h1>`. That looks perfect on the right side. But then we have lines and lines of raw text, floating alone in the body without any tags wrapping them. The browser has no idea how to format them.
코드를 맨 위에서부터 아래로 차근차근 읽어 내려가 보겠습니다. 실행의 흐름을 한 단계씩 추적해 나가는 것은 엔지니어의 가장 근본적인 핵심 기술입니다. `<html>` 문이 열렸고요. 좋네요. `<head>`도 정상. `<body>` 문도 열려 있습니다. 그 뒤로 `<h1>CEO of Nothing</h1>`가 보입니다. 이건 아까 화면 오른쪽에서 봤듯 완벽하게 구동되었죠. 하지만 그 아래로는 그 어떤 태그도 감싸지 않은 생원시(raw) 텍스트들이 바디 안에서 외롭게 둥둥 떠다니고만 있습니다. 브라우저로서는 저걸 어떻게 문단으로 쪼개서 포맷팅해야 할지 도무지 알 턱이 없는 겁니다.

Who can tell me what tag we are missing to fix this massive wall of text? Yes! We need the paragraph tag, the `<p>` tag. 
자, 이 거대하고 두꺼운 텍스트의 장벽을 부수고 원래대로 고치려면 도대체 어떤 태그가 빠진 것인지 누가 저한테 말해 주실 분 있나요? 네, 맞습니다! 우리에게는 바로 문단을 나누는 태그, `<p>` 태그가 절실히 필요합니다.

*(Instructor Note: Wrap the raw text strings with `<p>` and `</p>` tags one by one. The text will magically separate into nicely formatted blocks on the output side.)*
*(강사 참고: 아무렇게나 버려진 텍스트 문자열의 앞뒤를 `<p>`와 `</p>` 태그로 하나씩 하나씩 감싸 줍니다. 오른쪽 렌더링 화면에서 마법처럼 텍스트가 깔끔하게 분리된 예쁜 블록으로 정렬될 것입니다.)*

Look at how beautifully it separates! Just inserting `<p>` and `</p>` tells the browser that this chunk of text is a complete thought, and it deserves its own space. Now, what about the missing picture? We need an image of ourselves. I will use the `<img src="...">` tag we just mastered. I will put this right above the `<h1>` title so the picture is the very first thing people see.
얼마나 눈부실 만큼 아름답게 문단이 분리되는지 감상해 보시죠! 단지 `<p>`와 `</p>`를 삽입한 것만으로도 브라우저에게 "이 덩어리의 텍스트는 온전하게 독립된 하나의 생각의 뭉치니까 고유한 공간을 할당해 줘야 해"라고 말해준 셈입니다. 자, 그렇다면 우리의 실종된 프로필 사진은 어떻게 해야 할까요? 우리 자신의 이미지가 필요합니다. 방금 우리가 완벽하게 마스터했던 `<img src="...">` 태그를 사용할 겁니다. 사람들이 이 명함에 접속했을 때 가장 먼저 사진부터 볼 수 있게끔, 이것을 제일 위쪽인 `<h1>` 타이틀 바로 상단에 배치해 보겠습니다.

*(Instructor Note: Add the `<img>` tag and grab another image URL to place in the `src` attribute. Emphasize that adding content is like assembling Lego blocks.)*
*(강사 참고: `<img>` 태그를 새롭게 추가하고, `src` 속성에 넣을 또 다른 이미지 URL을 가져옵니다. 코드를 추가하는 행위가 마치 레고 블록을 하나둘씩 조립하는 것과 정확히 같다는 점을 한껏 부각합니다.)*

This is exactly like putting Lego blocks together. You take an `<h1>` Lego piece, a `<p>` Lego piece, and an `<img>` Lego piece, and you snap them together inside the `<body>` container. 
이 과정은 레고 블록 조각들을 차곡차곡 끼워 맞추는 일과 정확히 일치합니다. `<h1>` 모양 레고 조각을 집어 들고, `<p>` 모양 레고를 쥐고, 또 `<img>` 모양 레고 조각을 하나 빼내서 `<body>`라는 널찍한 장난감 통 안쪽에다가 모두 '딸깍' 소리가 나게 끼워 맞추고 있는 것이죠.

For this week's Micro-Assignment, we are going to use the magic of Artificial Intelligence to accelerate this process. We are not going to type every single tedious letter from scratch like it's 1999. Instead, your assignment is to open your favorite AI—whether it is ChatGPT, Gemini, or Claude—and ask it to generate the skeleton of your digital business card for you. 
자, 이번 주차에 여러분이 수행해야 할 '마이크로 과제(Micro-Assignment)'에서는 방금 보여드린 이런 조립 과정을 맹렬한 속도로 가속화하기 위해 인공지능(AI)의 마법을 십분 활용할 계획입니다. 마치 응답하라 1999 시절로 돌아간 것처럼 처음부터 모든 길고 지루한 글자를 타이핑하고 앉아 있지는 않겠다는 말입니다. 대신 여러분의 과제는, 본인이 애용하는 AI(ChatGPT, 제미나이, 클로드 등 무엇이든)를 켠 다음 "나를 위해 근사한 디지털 명함 뼈대를 생성해 줘"라고 무모하리만치 과감하게 요구하는 것입니다.

But here is the catch. The AI will probably give you a lot of complex tags we haven't even talked about yet. It might add `<div>`, or `<span>`, or crazy styling attributes that make your head spin. You must not blindly copy and paste it! An engineer never copies code they do not understand.
하지만 여기에 중요한 함정이 아주 깊게 파여 있습니다. AI는 아마도 우리가 아직 다루지도 않은 수백 가지의 복잡하고 진절머리 나는 태그들을 마구잡이로 던져 줄 겁니다. `<div>`나 `<span>`을 욱여넣기도 하고, 여러분의 머리가 빙빙 돌게 만들 미친 듯한 스타일링 속성을 잔뜩 끼워 넣을지도 모릅니다. 여러분은 이 결과물을 '눈을 감고 맹목적으로 복사'해서는 절대 안 됩니다! 진정한 엔지니어라면 자신이 한 줄 한 줄 이해하지 못한 코드를 함부로 남의 데서 복사하지 않는 법입니다.

Your assignment has three specific sections: First, the "AI Prompt"—show me exactly what sentence you typed to command the AI. Second, the "AI Critique"—in one sentence, tell me what you think of the AI's result. Was it too complicated? Was it exactly what you wanted? Look at the HTML it generated and evaluate it critically. Third, the "Final Result"—I want you to delete or modify at least ONE annoying or mysterious tag from the AI's code, replace it with your own simple tag (like a beautiful `<img>` of your own), and give me a screenshot of your personal version running in StackBlitz. 
여러분이 제출할 과제물은 앞서 공지한 세 가지 명확한 섹션으로 나뉘어야 합니다. 첫째, "AI Prompt (AI 질문표)" — 이 거대한 녀석에게 명령을 내리기 위해 여러분이 정확히 무슨 문장을 입력했는지 보여주세요. 둘째, "AI Critique (AI 답변 비평)" — 인공지능이 뱉어낸 결과물에 대한 여러분의 솔직한 평가를 단 한 줄의 문장으로 서술해 주세요. 너무 난해했나요? 여러분이 정확히 의도했던 대로 나왔나요? 생성된 HTML 뼈대를 눈으로 훑어보고 아주 날카롭고 비판적으로 바라보세요. 셋째, "Final Result (최종 결과 방어)" — AI가 짜준 코드의 바다에서 짜증을 유발하거나 도무지 정체를 알 수 없는 모호한 태그를 최소 '단 1개'라도 직접 스스로 골라 '삭제 혹은 수정'하시길 바랍니다. 그리고 그것을 여러분만의 고유한 단순한 태그(예를 들어 예쁜 프로필 사진이 담긴 독창적인 `<img>` 따위)로 교체한 뒤, StackBlitz에서 당당하게 돌아가는 여러분만의 개인화 버전 화면을 캡처해서 제출하면 됩니다.

Do not be intimidated. Remember, you control the computer. The tags do what you tell them to do. Let's make some awesome, although very basic, digital business cards this week. Have a fantastic week, everyone, and I will see you exactly at this time next week!
미리 지레 겁먹고 위축될 필요는 추호도 없습니다. 여러분 자신이 이 거대한 컴퓨터를 완벽하게 쥐락펴락 통제하고 있다는 사실만을 항상 기억하세요. 저 보잘것없는 태그들은 여러분이 시키는 대로만 움직이는 복종적인 존재들입니다. 자, 비록 가장 기초적인 뼈대 수준에 불과하겠지만 꽤나 근사하고 멋들어진 디지털 명함들을 이번 주에 한 번 만들어 봅시다. 그럼 학생 여러분 모두 환상적이고 역동적인 한 주를 보내시길 바라며, 정확히 다음 주 이 시간에 변함없는 모습으로 다시 뵙겠습니다!


## [Extended Session] Common Student Questions & Deep Dive
## [심화 세션] 흔한 학생 질문 및 딥 다이브

*(Instructor Note: This extended block is to be used as a buffer if the class progresses faster than expected, or to provide additional rich context to curious students. It dives deeper into the philosophy of the web and common beginner pitfalls.)*
*(강사 참고: 이 심화 블록은 수업이 예상보다 빠르게 진행될 경우를 대비한 버퍼로 사용하거나, 호기심 많은 학생들에게 풍성한 추가 배경지식을 제공하기 위함입니다. 웹의 철학과 초보자들이 흔히 겪는 함정들을 깊이 파고듭니다.)*

Many of you have sent me questions beforehand regarding exactly how much you need to memorize. When you look at the `<html>`, `<head>`, `<body>`, `<h1>`, and `<p>` tags, it might feel like you are learning a massive dictionary of new vocabulary. I want to address this explicitly. Do you need to memorize every single HTML tag that has ever been created? The absolute, undeniable answer is no. Memorization is the enemy of a modern software engineer.
여러분이 사전에 제게 가장 많이 보내주신 질문 중 하나는 "도대체 얼마나 많은 것을 외워야 합니까?"였습니다. `<html>`, `<head>`, `<body>`, `<h1>`, `<p>` 같은 태그들을 마주하면, 마치 수십만 단어가 수록된 방대한 새로운 언어 사전 전체를 암기하려 드는 기분이 들지도 모릅니다. 이 점에 대해 제가 아주 명확히 답변을 드리고 싶습니다. 지금까지 세상에 창조된 모든 HTML 태그를 여러분의 머릿속에 구겨 넣듯 통째로 외워야만 할까요? 그 질문에 대한 가장 절대적이고 부인할 수 없는 답변은 '아니오'입니다. 무작정 외우는 행위야말로 현대 소프트웨어 엔지니어들이 가장 경계해야 할 최악의 적입니다.

Think about how you use a search engine or an AI. You do not hold the entire encyclopedia in your brain. You merely hold the 'index' or the 'map' of where to find the knowledge. In Web Programming, you only need to understand the fundamental logic. For example, if you know that the `<body>` tag holds visible content, and you want to create a hyperlinked button, you just need to search for "HTML button tag" or ask your AI, "How do I make a clickable link inside the body?" The syntax will be provided to you instantly. Your job as an engineer is to take that syntax, evaluate if it is logical, and connect it to the rest of yours.
자, 여러분이 평소에 검색 엔진 상단 창이나 AI를 어떻게 활용하고 있는지 가만히 떠올려 보세요. 여러분은 백과사전 전체의 모든 텍스트를 머릿속 뇌세포에 모조리 저장해 두고 다니지 않습니다. 여러분은 오직 그 지식을 '어디에서 어떻게 찾아야 할지'를 알려주는 '색인(Index)'이나 '지도(Map)'만을 온전히 쥐고 있을 뿐입니다. 웹 프로그래밍이라는 수업에서도 진리는 동일합니다. 여러분은 그저 가장 근본적인 핵심 논리만을 이해하면 그만입니다. 예를 들어, `<body>` 태그가 시각적으로 노출되는 모든 콘텐츠를 품는다는 대전제를 알고 있고, 이제 화면에 클릭 가능한 하이퍼링크 버튼을 하나 만들고 싶다고 해봅시다. 그렇다면 여러분이 해야 할 일은 그저 "HTML 버튼 태그"라고 구글에 검색하거나, AI에게 "body 안쪽에 어떻게 클릭 가능한 링크를 만들 수 있어?"라고 똑똑하게 질문하는 것뿐입니다. 정확한 문법 규칙은 단 1초 만에 여러분의 눈앞에 대령될 것입니다. 엔지니어로서 진정 여러분이 해야 할 중대한 역할은, 그렇게 눈앞에 나타난 문법 구조를 조심스럽게 가져다가 그것이 현재 내 코드의 흐름상 논리적으로 타당한지 날카롭게 평가하고, 내가 기존에 짜놓은 다른 뼈대들과 자연스럽게 스며들도록 '연결(Connect)'해 내는 것뿐입니다.

Let us discuss another very common issue you will undoubtedly face. It is called the 'Whitespace' mystery. Suppose you type a paragraph in your code, and you press the spacebar on your keyboard fifty times between two words. You might expect the browser to display a massive, gaping gap between those words. Let's try it right now in our StackBlitz editor.
여러분이 필연적으로 직면하게 될 또 다른 아주 흔하고 진저리 나는 문제에 대해 한 번 심도 있게 토론해 보겠습니다. 이른바 '공백(Whitespace)'의 미스터리라고 부르는 현상입니다. 여러분이 코드 에디터 안에 문단 하나를 타이핑하고 있다고 가정합시다. 그리고 두 단어 사이에 스페이스바(Spacebar)를 미친 듯이 연타해서 50번쯤 띄어쓰기를 넣었다고 쳐 보죠. 여러분의 상식선에서는 브라우저가 당연히 그 두 단어 사이에 거대하고 뻥 뚫린 태평양 같은 공백을 그대로 보여주리라 기대할 것입니다. 우리의 StackBlitz 에디터에서 지금 당장 그 실험을 해볼까요.

*(Instructor Note: Type `<p>Hello                   World</p>` with many spaces. The output shows only one space.)*
*(강사 참고: `<p>Hello                   World</p>` 처럼 중간에 엄청난 공백을 넣어 타이핑함. 결과 화면에는 단 하나의 띄어쓰기만 적용되어 나타남.)*

Look at the result. I pressed the spacebar so many times my thumb hurts. But the browser completely ignored all of those extra spaces! It squashed them down into a single, tiny space. Why did it do that? Did my code break?
결과 창을 똑똑히 살펴보시죠. 제 엄지손가락에 쥐가 날 정도로 스페이스바를 미친 듯이 연타했는데도 불구하고 말입니다. 브라우저는 제가 피땀 흘려 추가한 그 수많은 여분의 공백들을 완전히 깔아뭉개고 철저하게 무시해 버렸습니다! 그 긴 공간을 찌부러뜨려 단 하나의 조그만 띄어쓰기로 퉁쳐버렸네요. 대체 웹 브라우저 녀석은 왜 이런 건방진 짓을 한 걸까요? 제 코드가 어딘가 박살이 나버린 걸까요?

No, your code did not break. This behavior is called 'Whitespace Collapse'. From the very beginning of the World Wide Web, the creators decided that raw text spacing inside an HTML document should not control the actual layout. If developers wanted strict control over spacing, layout, margins, and padding, they would have to use CSS—Cascading Style Sheets—which is exactly what we will conquer together in the upcoming weeks. HTML is the bones; it does not dictate how fat or thin the person is. CSS is the meat and the clothing. So, the browser purposefully ignores extra spaces to keep the raw text structure clean and to force you to rely on CSS for the visual design.
아닙니다. 여러분의 코드는 절대 고장 나지 않았습니다. 브라우저의 이러한 독특한 습성을 가리켜 '공백 축소(Whitespace Collapse) 현상'이라고 부릅니다. 아주 오래전 월드 와이드 웹(World Wide Web)이 처음 탄생하던 그 태초의 시기부터, 이 시스템의 창시자들은 HTML 문서 내부에 타이핑된 원시적인 띄어쓰기 텍스트 공백 따위가 웹페이지의 실제 레이아웃을 마음대로 통제해서는 안 된다고 굳게 마음먹고 결정했습니다. 만약 개발자들이 화면 상의 띄어쓰기, 레이아웃, 마진, 패딩과 같은 것들을 아주 엄격하고 정교하게 통제하고 싶다면, 그들은 반드시 CSS — Cascading Style Sheets — 라는 별도의 언어를 활용해야만 하도록 규칙을 설계했던 것이죠. 그 CSS가 바로 우리가 다가오는 몇 주 동안 함께 정복해 나갈 핵심 무기입니다. HTML은 어디까지나 뼈대일 뿐입니다. 그 뼈대 주변을 감싸고 있는 사람의 체형이 뚱뚱한지 홀쭉한지를 결정하지는 않는다는 뜻이죠. CSS야말로 뼈대 위에 붙는 살점이자 아름다운 옷차림입니다. 그렇기에 브라우저는 여러분이 HTML 문서에 입력한 쓸데없는 추가 공백들을 아주 고의적으로 못 본 척 무시함으로써, 원시 텍스트의 구조를 깨끗하게 보존하고, 시각적인 디자인에 관해서는 여러분이 철저하게 CSS에 의존하도록 강제하는 것입니다.

Speaking of tags, let us review the `<img>` tag and the terrifying "Dead link". Many beginner developers ask: "If the image breaks because I made a typo in the URL, can I just upload the image file directly to my HTML code?" This is a brilliant question. It reveals a deep engineering curiosity.
내친김에 태그에 대한 이야기를 조금 더 이어나가 봅시다. 우리가 아까 다뤘던 `<img>` 태그와 그 두려운 "죽은 링크(Dead link)" 엑스박스 사태를 다시 한번 떠올려 볼까요. 초보 개발자들이 수없이 던지는 질문 중 하나는 바로 이것입니다. "제가 URL 주소에 오타를 냈다는 그 사소한 이유 하나만으로 전체 이미지가 깨져버린다면, 애초에 그 이미지 파일 자체를 내 HTML 코드 안쪽에다가 통째로 업로드해서 욱여넣어 버리면 안 되는 건가요?" 와, 이것은 정말이지 눈부시게 훌륭한 질문입니다. 한 명의 예비 엔지니어로서 지녀야 할 매우 깊고 본질적인 호기심이 그대로 드러나는 질문이죠.

Can you insert an image directly into the text? Actually, yes, using something called Base64 encoding. You can translate a visual picture into a gigantic string of letters and numbers and paste it into your HTML. But... if you do that, your tiny 1-kilobyte HTML file suddenly turns into a massive 5-megabyte monster. It becomes impossible to read, extremely slow to load, and a nightmare to manage. Therefore, the architectural best practice is to separate the content (HTML) from the massive media files (Images). Your HTML remains extremely light and fast, acting solely as a roadmap that points to where the heavy media files are stored on a server.
눈에 보이는 이미지를 텍스트 데이터 내부로 다이렉트하게 삽입할 수 있을까요? 사실, 네, 가능합니다. 이른바 'Base64 인코딩'이라는 마법 같은 기법을 사용하면 말이죠. 여러분은 특정한 시각적 사진 한 장을 수만 개의 알파벳과 숫자가 뒤섞인 징그러울 만큼 거대한 텍스트 문자열로 모조리 번역해 낸 다음, 그것을 여러분의 HTML 코드 한복판에 통째로 복사해서 붙여넣을 수 있습니다. 하지만... 만약 여러분이 실제로 그런 미친 짓을 감행한다면 어떤 일이 벌어질까요? 고작 1킬로바이트(KB)도 채 안 되던 깃털처럼 가볍고 작았던 여러분의 HTML 파일은, 눈 깜짝할 사이에 5메가바이트(MB)에 육박하는 거대하고 끔찍한 괴물 덩어리로 변모하고 말 것입니다. 코드가 너무 길어져서 사람이 두 눈으로 읽는 것 자체가 완벽하게 불가능해질뿐더러, 브라우저가 그 페이지를 로딩하는 속도는 미치도록 느려지고, 훗날 파일을 관리하고 수정하는 일은 그야말로 지옥 같은 악몽이 되어버리겠죠. 그렇기 때문에 소프트웨어 아키텍처 관점에서의 가장 현명하고 완벽한 모범 답안(Best Practice)은, 구조를 담당하는 콘텐츠(HTML)와 무겁고 거대한 덩치를 자랑하는 미디어 파일(이미지)을 철저하게 분리해 내는 것입니다. 여러분의 HTML 문서는 오로지 그 무거운 미디어 파일들이 저 멀리 인터넷 서버 위 어느 구석에 저장되어 있는지를 친절하게 가리켜주는 가볍고 날렵한 '지도(Roadmap)' 역할만을 수행함으로써, 궁극적으로는 극단적인 가벼움과 눈부신 속도를 영원히 유지할 수 있게 되는 것입니다.


## [Extended Session 2] Introduction to Web Accessibility and HTML Standards
## [심화 세션 2] 웹 접근성(Web Accessibility)과 HTML 표준에 대한 입문

*(Instructor Note: This final deep-dive acts as an advanced primer on why HTML semantics matter so much in the real world, pushing students to think beyond just making things visible on the screen.)*
*(강사 참고: 이 마지막 심화 세션은 실제 현업에서 HTML 시맨틱(의미론)이 왜 그토록 중요한지에 대한 고급 입문 역할을 하며, 단순히 화면에 무언가를 시각적으로 띄우는 것 너머를 고민하도록 학생들을 자극합니다.)*

As we wrap up our incredibly productive second week, I want to plant a very important seed in your minds. It is a concept that separates the amateur coders from the true, professional software engineers. That concept is called 'Web Accessibility', often abbreviated as a11y. Have you ever wondered how a person who is entirely blind navigates the internet? Or how someone who cannot use a computer mouse interacts with a complex website? 
엄청나게 생산적이었던 우리의 두 번째 주간을 마무리하면서, 저는 여러분의 머릿속에 아주 중요하고 거대한 씨앗 하나를 심어두고 싶습니다. 그것은 바로 '아마추어 코더'와 진정한 '프로페셔널 소프트웨어 엔지니어'를 가르는 결정적인 개념입니다. 이 개념은 흔히 '웹 접근성(Web Accessibility)', 줄여서 a11y라고 부릅니다. 여러분은 앞을 전혀 보지 못하는 시각장애인이 어떻게 인터넷을 탐색하는지 궁금해본 적이 있나요? 혹은 마우스를 사용할 수 없는 신체적 제약을 가진 사람이 어떻게 이토록 복잡한 웹사이트들과 상호작용할 수 있는지 상상해 보신 적이 있습니까?

They do it using a specialized piece of software called a 'Screen Reader'. A screen reader literally reads the raw HTML code of your website out loud to the user. Now, if your HTML is just a giant, messy wall of text with no tags, the screen reader has absolutely no idea what to do. It will just start reading a massive block of confusing words without pausing or changing tone. But, if you use your tags correctly—if you use an `<h1>` for the main title, and a `<p>` for a paragraph—the screen reader understands the structure. It will announce, "Heading level 1: CEO of Nothing," and then it will pause respectfully before reading the paragraph. 
그분들은 '스크린 리더(Screen Reader)'라고 불리는 특수하고 정밀한 소프트웨어를 활용하여 웹을 탐색합니다. 스크린 리더는 말 그대로 여러분이 작성한 웹사이트의 원시 HTML 코드를 사용자에게 직접 소리 내어 읽어주는 역할을 합니다. 자, 만약 여러분의 HTML이 태그 하나 없이 그저 거대하고 지저분한 텍스트의 장벽에 불과하다면, 스크린 리더는 도대체 이것을 어떻게 처리해야 할지 전혀 갈피를 잡지 못하게 됩니다. 어디서 쉬어야 할지, 톤을 어떻게 바꿔야 할지 모른 채 무지막지하게 혼란스러운 단어의 덩어리들을 기계적으로 읽어대기 시작하겠죠. 하지만 만약 여러분이 오늘 배운 태그들을 구조에 맞게 올바르게 사용했다면 어떨까요? 메인 타이틀에는 `<h1>`을 적용하고, 문단에는 `<p>`를 시의적절하게 둘렀다면, 스크린 리더는 그 골격을 완벽하게 이해하게 됩니다. 시각장애인 사용자에게 "제목 레벨 1: CEO of Nothing"이라고 명확하게 선언한 뒤, 본문 문단을 소리 내어 읽기 전에 아주 정중하게 한 템포를 쉬어갈 수 있게 되는 것입니다.

This is exactly why I told you earlier that HTML does not care about colors or beauty. HTML only cares about 'meaning'. When you write HTML, you are not just painting a pretty picture for people with perfect eyesight. You are building a deeply structured logical document that can be read by computers, search engines, and assistive technologies. Imagine you have an image of your cute puppy. A blind person cannot see the puppy. How do we describe it to them? The `<img>` tag has another secret attribute called `alt`, which stands for alternative text. It looks like this: `<img src="..." alt="A fluffy golden retriever puppy smiling">`. 
이것이 바로 제가 수업 초반에 "HTML은 색상이나 미적인 아름다움에는 철저하게 무관심하다"고 거듭 강조했던 명확한 이유입니다. HTML은 오로지 '의미(Meaning)' 하나에만 집착합니다. 여러분이 HTML 코드를 타이핑할 때, 여러분은 단순히 시력이 온전하고 완벽한 사람들만을 위한 예쁜 그림을 캔버스에 그리고 있는 것이 아닙니다. 여러분은 컴퓨터와 구글 검색 엔진, 그리고 세상의 수많은 보조 공학 기기들이 완벽하게 읽고 해석할 수 있는 '깊고 단단하게 구조화된 논리적 문서'를 세우고 있는 중입니다. 여러분이 웹페이지에 띄운 그 귀여운 강아지 사진을 다시 상상해 보세요. 시각장애인은 그 귀여운 강아지를 두 눈으로 볼 수 없습니다. 우리는 그것을 그분들에게 어떻게 설명해 주어야 할까요? 놀랍게도 `<img>` 태그에는 '대체 텍스트(Alternative text)'의 약자인 `alt`라는 또 다른 비밀스러운 속성이 숨겨져 있습니다. 대략 이렇게 생겼죠: `<img src="..." alt="환하게 미소 짓고 있는 복슬복슬한 골든 리트리버 강아지">`.

If the image loads successfully and the user can see it, the browser keeps the `alt` text hidden. But if the user is employing a screen reader, the software will smoothly announce, "Image: A fluffy golden retriever puppy smiling." Furthermore, remember our nightmare scenario with the typo and the broken Dead Link? If the image breaks because of a server error or a bad internet connection, the browser will gracefully display that `alt` text on the screen instead of just an ugly broken icon. This is the hallmark of robust, fault-tolerant engineering. You anticipate failure, and you gracefully handle it.
만약 놀라운 화질의 사진이 성공적으로 로딩되고 일반 사용자가 그 이미지를 볼 수 있다면, 브라우저는 저 `alt` 대체 텍스트를 조용히 숨겨놓습니다. 하지만 만약 접속자가 스크린 리더를 사용하고 있다면, 소프트웨어는 부드러운 목소리로 "이미지: 환하게 미소 짓고 있는 복슬복슬한 골든 리트리버 강아지"라고 친절하게 읽어줄 것입니다. 뿐만 아니라, 아까 우리가 경험했던 오타로 인한 엑스박스와 데드 링크의 끔찍한 악몽 시나리오를 기억하시나요? 만약 서버에 치명적인 에러가 발생하거나 인터넷 연결이 불안정해서 이미지가 처참하게 깨져버린 경우, 브라우저는 단순히 흉측한 엑스박스 아이콘만 남겨두는 대신 저 `alt` 텍스트를 화면에 우아하게 대신 띄워주게 됩니다. 이것이야말로 진정으로 견고하고 결함 내성(fault-tolerant)이 뛰어난 위대한 엔지니어링의 상징이자 특권입니다. 실패할 가능성을 겸허히 예측하고, 그것을 우아하게 대비하여 처리하는 것이야말로 개발자의 미덕이죠.

Therefore, when you use Artificial Intelligence to complete your Micro-Assignments, do not just stare at the visual output on the right side of the StackBlitz screen. I strongly encourage you to deeply study the tags the AI generated on the left side. Notice how it structures the document. Does it use the correct HTML5 semantic tags? Does it provide `alt` text for images? An outstanding engineer questions everything, including the output of an advanced AI. 
따라서 여러분이 이번 주 과제인 마이크로 어사인먼트를 수행하기 위해 인공지능의 힘을 빌릴 때, 부디 StackBlitz 화면 오른쪽에 나타나는 시각적인 결과물에만 넋을 잃고 쳐다보지 마시기를 바랍니다. 저는 여러분이 언제나 왼쪽 패널에 등장하는 AI가 뱉어낸 그 뼈대 태그들을 집요하게, 그리고 대단히 깊이 있게 연구하고 분석할 것을 강력하게 권고합니다. AI가 이 문서를 대체 어떤 식으로 구조화했는지 날카롭게 관찰하세요. 그것이 최신 HTML5의 시맨틱(의미론적) 태그들을 올바르게 배치했나요? 사진을 띄웠다면 친절하게도 `alt` 텍스트 속성까지 챙겨서 넣어두었습니까? 뛰어난 역량을 갖춘 훌륭한 엔지니어는, 설령 전지전능해 보이는 진보한 AI의 결과물 앞에서도 언제나 끝없이 의심하고 모든 것에 질문을 던지는 사람입니다. 

When we meet next week, we will introduce HTML forms and buttons, giving you the power to actually communicate backward with your users. The web will evolve from a boring, static newspaper into an interactive, dynamic dialogue. Until then, remember: close your tags, watch for typos in your absolute paths, and never be afraid of debugging. Have a wonderful weekend!
우리가 다음 주 3주 차에 다시 만나게 될 때, 우리는 비로소 HTML 폼(Forms)과 버튼(Buttons)의 세계를 새롭게 도입할 것입니다. 이는 여러분들에게 단순히 정보를 보여주는 것을 넘어, 현장에 있는 방문자들과 본격적으로 데이터를 주고받고 맞소통할 수 있는 거대한 권력을 쥐여주게 될 것입니다. 바야흐로 지루하고 정적인 신문지에 불과했던 여러분의 웹페이지가, 놀랍도록 상호작용적이고 역동적인 대화의 플랫폼으로 진화하는 순간이죠. 그날이 올 때까지 부디 세 가지만 확실하게 기억해 주십시오. 여러분의 태그 문을 확실히 닫을 것, 절대경로를 타이핑할 때 눈을 크게 뜨고 오타를 경계할 것, 그리고 영원히 디버깅을 두려워하지 말 것! 그럼 모두 아름답고 경이로운 주말 보내시기를 바랍니다!


*(Instructor Note: Remind them one last time about the assignment deadline. Emphasize that reading the AI's tags carefully is the key to mastering this week's material. Remind them to submit everything via email (`wonhyuk@stu.ac.kr`) on time, with the exact title format `과제0.1 학번`.)*
*(강사 참고: 마지막으로 한 번 더 과제 마감 기한을 확실히 상기시킵니다. 인공지능이 생성해 낸 태그들을 주의 깊게 읽어보는 것만이 이번 주차의 핵심 내용을 완벽히 내 것으로 만드는 비결임을 힘주어 강조하세요. 제출은 반드시 기한 내에 이메일(`wonhyuk@stu.ac.kr`)로, 제목은 `과제0.1 학번` 형식을 지켜 제출하도록 당부합니다.)*

One absolute final reminder before we close: Please ensure you submit your Micro-Assignment with the Prompt, the Critique, and your Final Result. Submitting just the HTML file will result in a zero. We want to see your analytical thought process above all else. See you all soon!
수업을 마치기 전 마지막 필수 공지사항입니다. 마이크로 과제를 제출하실 때 반드시 여러분이 작성한 인공지능 프롬프트(질문)와 그에 대한 비평, 그리고 직접 수정한 최종 결과물 캡처 이 세 가지를 모두 포함했는지 점검해 주세요. 달랑 뼈대 HTML 파일만 띡하고 제출하는 행위는 0점 처리될 것입니다. 우리가 가장 보고 싶은 것은 그 무엇보다도 여러분의 날카롭고 분석적인 사고 과정 자체입니다. 그럼 모두 곧 다시 뵙겠습니다!
