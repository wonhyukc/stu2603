# Week 3 강의 대본 (Lecture Script) / Week 3 Lecture Script

## [S1] 웹과 소통하기: 폼 태그의 구성 (25분) / [S1] Communicating with the Web: Form Tags Breakdown (25 min)

*(강사 참고: 학생들을 반갑게 환영하며, 온라인 대면 수업의 특성을 살려 카메라를 보고 활기차게 인사합니다. 특히 외국인 유학생들의 시차나 현지 날씨를 묻는 스몰토크로 시작합니다.)*
*(Instructor Note: Welcome the students warmly. Look at the camera and greet them energetically to emphasize the live online format. Start with small talk, especially asking international students about their time zones or local weather.)*

여러분, 안녕하세요! 새로운 한 주가 밝았습니다. 여러분이 계신 곳의 날씨는 어떤가요? 한국은 지금 날씨가 꽤 변덕스러워서 비가 오다가도 금세 해가 쨍하게 비추곤 합니다. 다들 건강 잘 챙기고 계시길 바랍니다. 지난주에 우리 모두가 각자의 개성을 담은 멋진 온라인 명함을 무사히 완성했습니다. 아주 잘하셨어요! 화면 너머로 여러분이 스스로 코드를 작성하며 신기해하던 표정들이 아직도 생생합니다.
Hello, everyone! A new week has dawned. How is the weather where you are? The weather in Korea is quite unpredictable right now; it rains and then suddenly the sun shines brightly. I hope you are all staying healthy. Last week, we all successfully completed our own awesome online business cards that capture our unique personalities. Great job! The looks of amazement on your faces as you wrote the code yourselves are still vivid in my mind.

자, 그런데 여러분. 지난주에 만든 명함을 다시 한 번 띄워보시겠어요? 예쁘고 멋지긴 하지만, 뭔가 좀 심심하지 않나요? 맞습니다. 바로 **'소통'**이 빠져 있기 때문입니다.
Now, everyone. Could you bring up the business card you made last week again? It's pretty and cool, but doesn't it feel a bit boring? That's right. It's because **'communication'** is missing.

우리가 만든 웹페이지는 현재 단방향입니다. 마치 텔레비전 뉴스처럼, 제가 여러분께 저의 정보(이름, 취미 등)를 일방적으로 보여주기만 할 뿐입니다. 만약 누군가가 여러분의 명함 웹사이트에 방문해서 "와, 취미가 저랑 똑같네요! 같이 대화해봐요!"라고 메세지를 남기고 싶다면 어떻게 해야 할까요? 지금 상태로는 불가능합니다.
The webpage we created is currently one-way. Like the television news, I am just unilaterally showing you my information (name, hobbies, etc.). What if someone visits your business card website and wants to leave a message saying, "Wow, we have the exact same hobbies! Let's talk!"? In its current state, that is impossible.

그래서 이번 3주차에는 여러분의 명함에 **쌍방향 소통 창구**를 만들어 줄 겁니다. 마치 식당에 가면 손님들이 메뉴를 고를 수 있게 체크하는 주문서가 있듯이, 웹페이지에도 방문자가 무언가를 적어서 우리에게 전달할 수 있는 주문서가 필요합니다. 이 주문서 역할을 하는 것이 바로 오늘 배울 핵심 주제, **폼(Form)**입니다.
So, in this 3rd week, we are going to create a **two-way communication channel** on your business cards. Just like a restaurant has an order form for customers to check the menu they want, a webpage also needs an order form where visitors can write something down and send it to us. The core topic we will learn today, which acts as this order form, is the **Form**.

자, 다들 눈을 크게 뜨고 화면을 집중해주세요. 제가 StackBlitz 화면을 공유하겠습니다. 화면에 깔끔한 빈 도화지를 준비했습니다.
Now, everyone, open your eyes wide and focus on the screen. I will share my StackBlitz screen. I have prepared a clean, blank canvas on the screen.

여러분, 일상 생활에서 관공서나 은행에 가면 가장 먼저 무엇을 주나요? 바로 서류 양식, 즉 폼(Form)을 주죠? 웹에서도 똑같습니다. 사용자가 글씨를 쓸 수 있는 공간을 마련하려면, 제일 먼저 "여기부터 여기까지가 사용자가 입력할 구역이야!"라고 브라우저에게 알려줘야 합니다. 이때 사용하는 태그가 바로 `<form>` 태그입니다.
Everyone, when you go to a public office or a bank in your daily life, what is the first thing they give you? They give you a document form, right? It's exactly the same on the web. To provide a space for users to write text, you first need to tell the browser, "From here to here is the area where the user will input data!" The tag used for this is the `<form>` tag.

*(강사 참고: StackBlitz 화면에 `<form>` 태그를 라이브 코딩합니다.)*
*(Instructor Note: Live code the `<form>` tag on the StackBlitz screen.)*

```html
<form>
</form>
```

하지만 `<form>` 태그만 덜렁 써놓으면 화면에는 아무것도 나타나지 않습니다. 왜냐고요? 이것은 그저 "서류 뭉치를 담는 빈 폴더"와 같기 때문입니다. 폴더 안을 채우려면 실제 펜으로 글씨를 적을 수 있는 **입력 칸**을 만들어야 합니다. 이 입력 칸을 만드는 마법의 태그가 바로 `<input>`입니다. '입력하다'라는 뜻의 영어 단어 그대로죠.
However, if you just leave the `<form>` tag hanging there, nothing will appear on the screen. Why? Because this is just like an "empty folder for holding a stack of papers." To fill the folder, you need to create an **input field** where you can actually write with a pen. The magical tag that creates this input field is `<input>`. It literally means "to input."

자, 한번 적어볼게요.
Let's type it out.

```html
<form>
  <input>
</form>
```

오! 보셨나요? 우측 렌더링 화면에 글씨를 타이핑할 수 있는 하얀 네모 상자가 뿅 하고 나타났습니다. 여기에 여러분의 이름을 적어볼 수도 있죠. 이 작은 상자 하나가 바로 여러분의 웹사이트를 '정적'인 문서에서 '동적'인 소통의 장으로 바꿔주는 첫걸음입니다.
Oh! Did you see that? A white rectangular box where you can type text suddenly popped up on the right rendering screen. You can even try typing your name here. This single small box is the first step in transforming your website from a 'static' document into a 'dynamic' place of communication.

그런데 `<input>` 태그에는 아주 놀라운 비밀 무기가 하나 있습니다. 바로 **`type` 속성**입니다.
우리가 옷을 입을 때, 운동할 때는 운동복을, 잠잘 때는 잠옷을 입듯, `<input>`도 목적에 따라 옷을 갈아입을 수 있습니다.
By the way, the `<input>` tag has a very amazing secret weapon. It is the **`type` attribute**.
Just like we wear sportswear when exercising and pajamas when sleeping, the `<input>` tag can also change clothes depending on its purpose.

한번 볼까요? 제가 속성으로 `type="text"`를 줘보겠습니다.
Let's take a look. I'll give it the attribute `type="text"`.

```html
<input type="text">
```

이건 기본 텍스트, 즉 일반적인 글씨를 적는 상자입니다. 이번에는 비밀번호를 입력받고 싶어요. 남들이 보면 안 되니까요. 이럴 때는 `type`을 어떻게 해야 할까요?
This is basic text, a regular box for writing normal letters. This time, I want to receive a password. Since others shouldn't see it. In this case, what should the `type` be?

```html
<input type="password">
```

이렇게 적어주면... 자! 제가 키보드를 막 쳐보겠습니다. 어떻게 되나요? 깜장색 동그라미(혹은 별표)로 변해서 제가 무슨 글씨를 치는지 숨겨주죠! 이것이 바로 타입의 힘입니다.
If you type it like this... Now! I'll randomly hit the keyboard. What happens? It turns into black circles (or asterisks) and hides what I'm typing! This is the power of the type attribute.

더 재미있는 것도 있습니다. 만약 달력을 띄워서 날짜를 선택하게 하고 싶다면요? 어려운 코드를 짤 필요가 전혀 없습니다.
There are even more fun things. What if you want to pop up a calendar and let the user select a date? There is absolutely no need to write difficult code.

```html
<input type="date">
```

우와! 방금 보셨나요? 브라우저에 달력 아이콘이 생겼습니다. 클릭하니 달력이 튀어나오죠! 예전에는 이런 달력 하나 만들려면 몇 날 며칠을 밤새 코드와 씨름해야 했지만, 이제는 이 `type="date"` 하나로 마법처럼 해결됩니다.
Wow! Did you just see that? A calendar icon appeared in the browser. When I click it, a calendar pops out! In the past, you had to struggle with code for days and nights just to make one calendar like this, but now, it's magically solved with just this `type="date"`.

이 외에도 체크박스(`type="checkbox"`), 동그란 라디오 버튼(`type="radio"`) 등 무궁무진합니다. 여러분은 그저 "어떤 목적의 데이터를 받을 것인가"만 결정하면 됩니다.
Besides this, there are endless options like checkboxes (`type="checkbox"`), round radio buttons (`type="radio"`), etc. You just need to decide "what kind of data purpose you are going to receive."

자, 입력은 다 마쳤습니다. 그런데 열심히 적기만 하면 무슨 소용인가요? 은행 직원에게 종이를 건네주어야 서류 제출이 끝나겠죠? 웹에서는 그 건네주는 역할을 **버튼(Button)**이 합니다.
Alright, we're done with input. But what is the use of just writing diligently? You have to hand the paper to the bank teller to finish submitting the document, right? On the web, the **Button** plays the role of handing that over.

```html
<button>제출하기 / Submit</button>
```

보이시나요? 폼 태그 제일 밑에 `<button>`을 만들고 그 안에 '제출하기'라고 썼습니다. 아주 예쁜 클릭 가능한 버튼이 완성되었습니다.
Do you see it? I created a `<button>` at the very bottom of the form tag and wrote 'Submit' inside it. A very pretty clickable button is complete.

정말 간단하죠? 요약하자면 오늘 배운 폼의 기본 구조는 **1. `<form>`이라는 큰 틀 안에 2. `<input>`으로 입력 공간을 만들고 3. `<button>`으로 제출한다!** 이 3단계만 기억하시면 됩니다.
It's really simple, isn't it? To summarize, the basic structure of the form we learned today is: **1. Inside the big framework called `<form>`, 2. create an input space with `<input>`, and 3. submit with `<button>`!** You only need to remember these three steps.

아, 그런데 잠깐 여기서 중요한 질문이 하나 들어올 수 있겠네요. "교수님, `<input>` 안에 기본으로 희미하게 적혀있는 글씨 말고, 아예 처음부터 값이 들어가 있게 할 수는 없나요?" 아주 훌륭한 질문입니다!
Oh, but wait, an important question might arise here. "Professor, instead of faintly written text as a placeholder inside the `<input>`, isn't it possible to have a value already filled in from the very beginning?" That is an excellent question!

우리가 관공서 서류를 뗄 때 이름란에 제 이름이 미리 인쇄되어 있으면 참 편하죠? 웹에서도 마찬가지입니다. `<input>` 태그에는 `value`라는 속성이 있습니다.
When we get documents from a public office, it's really convenient if my name is pre-printed in the name field, right? It's the same on the web. The `<input>` tag has an attribute called `value`.

```html
<input type="text" value="Hong Gildong">
```

이렇게 적어주면 처음부터 저 칸 안에 'Hong Gildong'이라는 글자가 떡하니 들어가 있습니다. 사용자가 직접 지우고 다른 걸 쓸 수도 있고요. 기본값을 세팅해줄 때 아주 유용하겠죠? 예를 들어 국가를 선택하는 칸이 있다면 기본값으로 "대한민국"을 넣어둘 수 있는 겁니다.
If you write it like this, the word 'Hong Gildong' is sitting right there in the box from the beginning. The user can also manually erase it and write something else. It would be very useful when setting a default value, right? For example, if there is a field to select a country, you could put "South Korea" as the default value.

그리고 또 하나 더! "비밀번호 칸인데, 너무 짧게 쓰면 반려하고 싶어요. 어떻게 하나요?"라는 질문도 나올 수 있습니다.
And one more thing! The question might arise: "It's a password field, and I want to reject it if they write it too short. What should I do?"

HTML은 참으로 배려심이 깊습니다. `minlength`와 `maxlength`라는 속성을 제공합니다.
HTML is truly very considerate. It provides the `minlength` and `maxlength` attributes.

```html
<input type="password" minlength="8" maxlength="20">
```

이 속성들을 붙여주면, 사용자가 비밀번호를 8글자보다 짧게 쓰거나 20글자보다 길게 쓸 때 알아서 차단해 줍니다.
과거에는 이런 걸 모두 복잡한 자바스크립트 수백 줄로 짜야 했어요. 하지만 지금은 시대가 좋아져서 HTML 태그 하나로 다 처리할 수 있게 된 거죠. 여러분은 복잡한 논리나 문법을 달달 외울 필요가 없습니다. 그저 "이런 기능이 있구나" 정도만 기억해 두시고, 나중에 필요할 때 검색하시거나 AI에게 "HTML로 글자 수 제한 어떻게 해?"라고 물어보시면 됩니다.
If you attach these attributes, it automatically blocks the user if they write a password shorter than 8 characters or longer than 20 characters.
In the past, you had to code all of this with hundreds of lines of complex JavaScript. But times are so good now that you can handle it all with a single HTML tag. You do not need to memorize complex logic or grammar by heart. Just remember "this kind of feature exists," and later when you need it, you can search or ask an AI, "How do I limit character length in HTML?"

자, 폼 태그의 구성에 대해 여기까지 이해가 되셨나요? 고개를 끄덕이시는 분들이 많네요. 좋습니다.
우리가 이제 뼈대를 다 배웠으니, 이 뼈대를 가지고 실제로 살아 움직이는 '방명록'을 조립해 볼 차례입니다. 다음 섹션에서 본격적으로 여러분의 명함에 소통 창구를 달아보겠습니다. 잠시 스트레칭 한 번 하시고, 기지개 활짝 켜신 다음 두 번째 섹션으로 넘어가겠습니다!
Now, do you understand the breakdown of the form tags up to this point? I see many people nodding their heads. Good.
Now that we have learned all the skeletons, it is time to assemble an actually living, moving 'Guestbook' with these skeletons. In the next section, we will begin in earnest to attach a communication window to your business card. Take a moment to stretch, spread your arms wide, and then we will move on to the second section!

---

## [S2] 방명록 폼 만들기 및 폼의 원리 (25분) / [S2] Building the Guestbook Form & Form Principles (25 min)

*(강사 참고: 지난 주에 배운 내용을 복습하며 점진적으로 새로운 내용을 덧붙이는 Build-up 방식으로 접근합니다. 자연스럽고 대화하는 듯한 톤을 유지하세요.)*
*(Instructor Note: Approach this with a Build-up method, reviewing last week's material and gradually adding new content. Maintain a natural, conversational tone.)*

자, 여러분! 첫 번째 섹션에서 우리는 폼의 아주 기본적인 동작 방식을 살펴봤습니다. 이제 진짜 재미있는 시간을 가져봅시다. 바로 여러분이 지난주에 정성껏 만든 **온라인 명함**에 **'방명록'**을 직접 달아주는 시간입니다!
Alright, everyone! In the first section, we looked at the very basic operation of forms. Now let's have some real fun. It's time to personally attach a **'Guestbook'** to the **online business card** you carefully created last week!

여러분 모두 각자의 명함 파일을 열어주시겠어요? 사진도 있고 이름도 있고, 각자의 고향인 네팔, 인도, 베트남 등의 자기소개가 멋지게 적혀 있을 겁니다.
Could everyone please open your respective business card files? There should be your photo, your name, and a cool self-introduction about your hometowns in Nepal, India, Vietnam, etc.

자, 제 화면을 보세요. 저도 제 명함을 띄웠습니다. 명함의 제일 아랫부분에 방명록을 달아보겠습니다. 우선 방명록이라는 것을 알려주기 위해, 구분을 지어야겠죠. 구분선 태그인 `<hr>`을 그어주겠습니다. 그리고 제목도 하나 달아볼까요?
Now, look at my screen. I have also brought up my business card. Let's attach a guestbook to the very bottom part of the business card. First, to indicate that it is a guestbook, we should make a division. I will draw a horizontal rule tag, `<hr>`. And shall we add a title too?

```html
<hr>
<h2>Leave a Message</h2>
```

아주 근사하게 선이 그어지고 제목이 생겼네요.
A line has been drawn and a title has been created quite wonderfully.

이제 방명록에 필요한 정보가 무엇인지 생각해봅시다. 누군가 글을 남겼는데, 누군지도 모르고 이메일 주소도 모르면 제가 답장을 해줄 수가 없겠죠? 그래서 1) 작성자의 이름, 2) 작성자의 이메일 주소, 그리고 3) 남기고 싶은 메세지를 받을 수 있는 3개의 칸을 만들 겁니다.
Now let's think about what information is needed for a guestbook. If someone leaves a message, but I don't know who they are or their email address, I can't reply back to them, right? So, we are going to create 3 boxes to receive: 1) the writer's name, 2) the writer's email address, and 3) the message they want to leave.

이전 섹션에서 배웠던 폼의 규칙 1단계! 네, 바로 빈 폴더를 꺼내야 하죠. `<form>` 태그를 시작합니다.
Rule step 1 of the forms we learned in the previous section! Yes, exactly, we need to bring out the empty folder. We start with the `<form>` tag.

```html
<form>
</form>
```

자, 먼저 이름을 받아보겠습니다.
이게 방금 배운 `<input type="text">`를 쓰면 딱이겠네요. 그런데 이 네모칸이 이름을 적는 칸이라는 걸 방문자가 어떻게 알까요? 칸 옆에 "이름을 적어주세요!"라는 이름표를 달아주는 것이 친절하겠죠. 이때는 `<label>`이라는 태그를 씁니다. 라벨지에 이름을 써서 붙여주는 것과 똑같아요.
Now, let's receive the name first.
It would be perfect to use the `<input type="text">` we just learned for this. But how would the visitor know that this rectangular box is the box for their name? It would be kind to attach a name tag next to the box that says "Please write your name!" In this case, we use a tag called `<label>`. It's exactly the same as writing a name on a sticky label and attaching it.

```html
<label>Name:</label>
<input type="text" placeholder="Your Name">
```

참, 여기서 처음 보는 `placeholder`라는 속성이 보일 텐데요, 여러분! 칸 안에 옅은 회색으로 "Your Name"이라고 안내 문구가 들어간 것 보이시죠? 백화점 가이드라인처럼 방문자에게 예시를 보여주는 훌륭한 속성입니다.
By the way, you might see an attribute called `placeholder` here for the first time, everyone! Do you see the guiding phrase "Your Name" inside the box in faint gray? It is a wonderful attribute that shows visitors an example, like a department store guideline.

다음은 이메일을 받아야 합니다. 줄바꿈을 위해 `<br><br>`을 써줍니다.
Next, we need to receive the email. We will use `<br><br>` for line breaks.

```html
<br><br>
<label>Email:</label>
<input type="email" placeholder="you@domain.com">
```

여기서는 `type="email"`을 썼습니다! 이것이 얼마나 똑똑한지는 조금 이따가 직접 보여드리겠습니다.
Here, we used `type="email"`! I will personally show you just how smart this is in a little while.

마지막으로 긴 메시지를 남겨야 하는데요. 제가 여러분께 편지를 쓰는데 아주아주 작은 한 줄짜리 네모칸에 다 써야 한다면 얼마나 답답할까요? 그래서 여러 줄을 넉넉하게 쓸 수 있는 커다란 텍스트 박스가 필요합니다. 그건 `<input>` 대신에 `<textarea>`를 사용합니다. 이름부터 "넓은 텍스트 영역"이죠?
Lastly, they need to leave a long message. If I were writing a letter to you, how frustrating would it be if I had to write everything entirely in a very, very small one-line rectangular box? So, we need a large text box where you can generously write multiple lines. For that, we use `<textarea>` instead of `<input>`. The name itself means "large text area," right?

```html
<br><br>
<label>Message:</label><br>
<textarea rows="4" cols="30" placeholder="Say hello!"></textarea><br><br>
```

`rows`와 `cols`는 가로 세로 칸 수를 의미해요. 넓게 넓게 펼쳐져서 속이 시원해졌습니다.
`rows` and `cols` mean the horizontal and vertical number of spaces, respectively. It has spread out wide, making us feel refreshed.

그리고 방명록의 대미를 장식할 전송 버튼이죠!
And the submit button that will decorate the finale of the guestbook!

```html
<button type="submit">Send Message</button>
```

자, 짠! 오른쪽에 방명록이 완성되었습니다! 여러분 놀랍지 않나요? 우리가 조금씩 코드를 덧붙였을 뿐인데 이렇게 훌륭한 인터넷 방명록 레이아웃이 나왔습니다. 여러분 모두 꼭 스스로 실습해보시고 완성된 모습을 만끽해보세요.
Now, Ta-da! The guestbook has been completed on the right side! Isn't it amazing, everyone? We just added code little by little, and such a wonderful internet guestbook layout came out. Everyone, please make sure to practice this yourself and fully enjoy the completed appearance.

자, 그런데 여기서 아주아주 재밌고 엄청나게 중요한 사실을 하나 알려드리겠습니다. 다들 화면에 집중해주세요.
Now, however, I will tell you one very, very fun and incredibly important fact right here. Everyone, focus on the screen.

제가 방금 만든 폼에 제 이름과 이메일을 적을 텐데, 이메일 칸에 제 이름인 'wonhyuk'이라고 대충 글씨를 쳐버렸습니다. 그리고 당당하게 [Send Message] 버튼을 딱 누르면 어떻게 될까요?
I am going to write my name and email in the form I just made, but I carelessly typed my name 'wonhyuk' in the email box. And what happens when I confidently press the [Send Message] button?

*(강사 참고: StackBlitz 화면에서 `<input type="email">` 안에 잘못된 이메일 양식을 넣고 제출을 클릭합니다. 브라우저의 기본 팝업인 "이메일 주소에 @를 포함해 주세요"가 뜨는 것을 보여줍니다.)*
*(Instructor Note: On the StackBlitz screen, enter an incorrect email format into the `<input type="email">` and click submit. Show that the browser's default popup "Please include an '@' in the email address" appears.)*

오마이갓! 보이시나요? 브라우저가 화를 내며 제멋대로 경고 메시지를 띄웠습니다! "이메일 주소 형식에 맞게 '@' 문자를 포함해서 작성해주세요!"라고 빨간 글씨를 보여주네요.
우리는 저런 안내문을 띄우라는 코드를 단 한 줄도 짠 적이 없는데 말이죠!
Oh my god! Do you see that? The browser got angry and threw up a warning message on its own! It's showing red text saying "Please include the '@' character in the email address format!"
Even though we never wrote a single line of code telling it to display such a notice!

이것이 바로 브라우저의 엄청난 능력입니다. 우리가 `type="email"`이라고 지정해준 순간, 브라우저는 "앗! 여기엔 반드시 이메일 규칙이 들어가야 해"라고 똑똑하게 **유효성 검사**를 해주는 것입니다. 이런 사소한 것들이 방문자의 실수를 막아주고 프로페셔널한 사이트로 만들어줍니다.
This is exactly the enormous power of the browser. The moment we designated it as `type="email"`, the browser intelligently performs **validation**, thinking, "Ah! An email rule must absolutely go in here." These trivial things prevent visitor mistakes and make it into a professional site.

그리고 버튼을 누르고 조건을 만족했을 때 어떤가요? 방금 화면이 눈을 깜빡이듯 '새로고침'되면서 제가 입력한 내용이 싹 날아가버렸죠!
초보자분들은 "악! 내가 다 적은 게 날아갔어! 버그가 생겼나 봐!" 하고 당황하시는데요, 절대 아닙니다.
And what happens when you press the button and the conditions are met? Just now, the screen 'refreshed' as if blinking an eye, and everything I inputted completely flew away!
Beginners often panic, thinking, "Ack! Everything I wrote is gone! Must be a bug!" But it absolutely is not.

이것은 브라우저의 **가장 기본적이고 정상적인 폼 전송 방식**입니다. 여러분이 우체국에서 편지를 부칠 때, 편지가 여러분의 손을 떠나 우체통 안으로 사라지는 것과 똑같아요. 브라우저가 저 서류 뭉치를 품에 안고 어디론가 전송하려고 페이지를 다시 리로드하는 겁니다.
This is the browser's **most basic and normal form submission method**. It is exactly the same as when you mail a letter at the post office; the letter leaves your hands and disappears into the mailbox. The browser embraces that stack of documents and reloads the page to transmit it somewhere.

다만, 지금은 데이터를 받아줄 백엔드(창구 직원)가 없기 때문에 일단 전송만 하고 제자리로 돌아오는 거죠. 방명록의 내용이 지금은 저장되지 않지만, 그것은 여러분이 잘못 코딩해서가 아니니 안심하셔도 됩니다! 나중에 데이터베이스를 배우게 되면 그 편지가 데이터베이스라는 든든한 금고에 안전하게 저장될 겁니다.
However, because there is no backend (teller) to receive the data right now, it simply transmits it and returns to its original place. The contents of the guestbook are not currently saved, but you don't have to worry because that's not due to you coding it incorrectly! Later, when you learn about databases, that letter will be safely stored in the solid vault known as the database.

---

## [S3] 오작동 디버깅과 AI의 활약 (25분) / [S3] Malfunction Debugging & The Role of AI (25 min)

*(강사 참고: 학생들의 주의를 집중시키고, 실수를 두려워하지 않도록 격려하는 것이 핵심입니다. AI를 적극적으로 활용하는 방법을 보여줍니다.)*
*(Instructor Note: The key is to gather the students' attention and encourage them not to fear making mistakes. Demonstrate how to actively utilize AI.)*

벌써 마지막 섹션입니다! 여러분, 우리 엔지니어들에게 코드를 예쁘게 짤 줄 아는 것만큼이나 중요한 능력이 있습니다. 그것이 무엇일까요? 바로 **문제를 해결하는 능력**, 전문 용어로는 **디버깅(Debugging)**입니다.
It is already the final section! Everyone, there is a skill just as important to us engineers as knowing how to write beautiful code. What is it? That is exactly the **ability to solve problems**, or in technical terms, **Debugging**.

현실 세계에서 물건이 고장나면 왜 고장 났는지 찬찬히 원인을 찾아 고치죠? 웹 개발도 똑같습니다. 우리의 코드는 숨쉬듯이 고장 날 것이고, 우리는 숨쉬듯이 고칠 겁니다. 여러분이 그 과정을 두려워하지 않기를 바랍니다.
In the real world, when an object breaks down, we carefully find the cause of why it broke and fix it, right? Web development is the same. Our code will break constantly like breathing, and we will fix it constantly like breathing. I hope you do not fear that process.

자, 제가 제 화면을 하나 공유하겠습니다. 개발자들이 정말 흔히 저지르는 끔찍한 실수 중 하나를 보여드리겠습니다. 화면 밑에 조그마하게 제가 "오류 디버깅 예제"라는 걸 만들어 두었는데요.
Now, I will share one of my screens. I will show you one of the terrible mistakes that developers make really commonly. At the bottom of the screen, I purposely made a small thing called the "Error Debugging Example".

한번 보세요. 제가 폼을 열고 라벨이랑 버튼을 달았는데 뭔가 이상합니다.
Take a look. I opened the form and attached labels and buttons, but something is weird.

```html
<!-- The form below is intentionally left unclosed to break layout -->
<form>
    <label>Newsletter Signup:</label>
    <input type="email" placeholder="Subscribe">
    <button type="submit">Subscribe

<h3>This header might be broken because of unclosed tags!</h3>
```

혹시 무언가 허전한 걸 눈치채셨나요? 맞습니다. 버튼 태그도 닫지 않았고, 시작했던 `<form>` 태그에 대한 닫는 `</form>` 태그가 눈을 씻고 찾아봐도 없습니다!
Did you happen to notice something missing? That's right. The button tag was not closed, and there is absolutely no closing `</form>` tag for the started `<form>` tag anywhere in sight!

우리가 밥을 먹었으면 그릇을 치워야 하고, 문을 열었으면 닫고 나가야 합니다. 태그를 열었으면 반드시 `/` 기호를 써서 닫아주어야 하죠. 안 그러면 어떻게 되느냐? 브라우저가 너무나 혼란스러워합니다. "어? 폼이 여기서 끝난 거야 만 거야?" 하고 헷갈려서 그 밑에 있는 아주 멀쩡한 제목 텍스트(`<h3>` 태그)조차 폼 속에 갇혀버리거나 화면의 디자인 구조를 무너뜨리게 됩니다.
If we eat a meal, we have to clear the dishes, and if we open a door, we must close it when leaving. If you open a tag, you must absolutely close it using the `/` symbol. If you don't, what happens? The browser gets extremely confused. It gets tangled up wondering, "Huh? Did the form end here or not?" and even the perfectly fine title text (`<h3>` tag) located below it inevitably gets trapped inside the form or causes the screen's design structure to collapse.

이런 상황에서 당황하지 마세요! 이런 문을 닫지 않은 오류는 아주 흔합니다. 코드를 짤 때 항상 "열린 괄호가 있으면 닫힌 괄호가 있는지 눈으로 확인하는 습관"을 들이면 됩니다.
Don't panic in this situation! This kind of error of not closing the door is very common. When writing code, you just need to develop the habit of always "visually checking if there is a closed bracket when there is an open bracket".

그런데 제가 여러분께 훌륭한 파트너가 한 명 있다고 말씀드렸죠? 바로 우리의 친구 **생성형 AI (ChatGPT, Gemini)**입니다.
By the way, didn't I tell you that you have one excellent partner? It is our friend, **Generative AI (ChatGPT, Gemini)**.

자, 실습을 좀 더 고도화해 볼까요?
우리가 만든 방명록은 아주 간단한데, 제가 만약 꽃꽂이 모임을 운영하고 있어서 "회원 가입 폼" 같은 복잡한 걸 만들고 싶다고 해볼게요. 하나하나 구글에서 검색하며 짜려면 시간이 굉장히 오래 걸릴 겁니다.
Now, shall we step up the practice a bit more?
The guestbook we made is very simple, but let's say I run a flower arrangement gathering and I want to make something complex like a "Membership Signup Form". If I try to code it by searching Google one by one, it will take a very long time.

이때 AI의 힘을 빌리는 겁니다! 제가 ChatGPT 창을 켜고 이렇게 질문해보겠습니다.
> **"나만의 꽃꽂이 클래스 참석 예약 폼을 HTML로 아주 간단하게 짜줘. 이메일도 꼭 들어가야 해."**

This is when we borrow the power of AI! I will turn on the ChatGPT window and ask this question:
> **"Create a very simple class attendance reservation form for my own flower arrangement gathering in HTML. It must include an email field too."**

자, 답변이 나오는 것을 볼까요? AI가 10초도 안 되어서 꽤 훌륭한 `<form>` 구조를 뱉어냈습니다!
`name`, `email`, 심지어 참석할 날짜를 고르는 `type="date"`까지 알아서 넣어주었네요.
Now, shall we watch the response come out? The AI spat out a pretty excellent `<form>` structure in less than 10 seconds!
It spontaneously took care to insert `name`, `email`, and even `type="date"` for selecting the attendance date.

이 코드를 복사해서 제 StackBlitz에 싹 붙여넣어 보겠습니다. 우와! 아주 예쁜 꽃꽂이 클래스 참석 예약 칸이 나왔습니다.
I will casually copy this code and paste it right into my StackBlitz. Wow! A very pretty flower arrangement class reservation section is generated.

하지만 여기서 **매우 주의할 점**이 있습니다! AI가 준 것을 그저 'Ctrl+C, Ctrl+V' 하고 끝낸다면 다 된 걸까요? 절대 아닙니다. AI는 훌륭한 조수지만 가끔가다 아주 엉뚱한 실수를 저지릅니다. 만약 `<input type="email">`을 줘야 하는데, AI가 깜빡하고 `<input type="text">`로만 대충 던져주었다고 가정해 볼까요?
However, there is a **very important thing to be careful about** here! Is everything completely finished if we just do "Ctrl+C, Ctrl+V" with what the AI gave us? Absolutely not. While AI is an excellent assistant, it occasionally makes very absurd mistakes. What if it had to provide an `<input type="email">`, but the AI forgot and just carelessly tossed over an `<input type="text">` instead?

제가 한번 AI 코드를 일부러 그렇게 수정해서 이메일 칸에 한글로 '꽃꽂이' 라고 치면 다 통과되어버릴 겁니다. 그러면 정작 저에게 나중에 참석자 명단이 날아왔을 때 답장을 줄 수 없어서 클래스가 엉망이 되겠죠.
If I purposely modify the AI code like that and type the Korean word 'flower arrangement' in the email box, it will just pass right through. Then, when the attendee list is finally sent to me later, I won't be able to reply, and the class operation will become a mess.

그래서 여러분은 반드시 AI가 만들어준 결과물을 **여러분만의 비평적인 시각으로 점검**해야 합니다.
이것이 이번 3주차 마이크로 과제의 핵심이기도 합니다.
That is exactly why you must absolutely **inspect the results created by the AI with your own critical eye**.
This is also the core element of the week 3 micro-assignment.

여러분이 가장 좋아하는 취미(축구 동호회, 영화 감상 등)를 주제로 폼을 하나 AI에게 짜달라고 해보세요. 그리고 AI가 짜준 코드를 가져와 복사해본 다음, **이메일 칸에 글자를 입력하고 확인을 눌러서 에러가 제대로 뜨는지, 타입이 제대로 되어 있는지 실험**해 보십시오.
Try asking the AI to code a single form regarding the hobby you like best (a soccer club, watching movies, etc.) as the subject. And after you bring in and copy the code the AI drafted to try out, **experiment by typing letters into the email box and clicking confirm to see if the error appropriately appears and if the type is properly configured**.

여러분이 스스로 의심하고, 수정하고, 디버깅할 때 여러분의 실력은 눈부시게 폭발적으로 성장할 것입니다.
When you personally doubt, modify, and debug it for yourself, your capabilities will explosively grow in a dazzling manner.

오늘 수업은 여기서 마무리하겠습니다. 방명록을 만드느라 수고 많으셨고, 여러분의 홈페이지가 마침내 여러분의 목소리를 담고 사람들의 이야기를 들을 준비가 되었습니다! 이 멋진 첫 소통의 단추를 잘 간직하시길 바랍니다. 이메일 과제와 eCampus 동료평가 제출 꼭 잊지 마시고요. 다음 주에 훨씬 더 매력적인 기술을 가지고 돌아오겠습니다. 여러분 안녕!
I will wrap up today's class here. You did a great job making the guestbook, and your homepage is finally prepared to contain your voice and listen to people's stories! I hope you carefully cherish this wonderful first step of communication. Please do not forget your email assignment and submitting the eCampus peer evaluation. I will return next week with far more attractive and fascinating technologies. Goodbye, everyone!
