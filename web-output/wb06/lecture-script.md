Created At: 2026-04-02T10:54:54Z

## [S1] 웹의 물리 법칙: CSS 박스 모델 이해하기 (약 15분)

First, let's talk about the Box Model, which is the most basic yet most difficult concept in CSS. Everything you see on a web page is actually made of rectangular 'boxes.' Images, text, and even buttons are all boxes. If you understand these boxes well, you've conquered 80% of web design.
먼저, CSS에서 가장 기초적이면서도 가장 어려운 개념인 '박스 모델'에 대해 이야기해 보겠습니다. 여러분이 웹페이지에서 보는 모든 것은 사실 직사각형의 '상자(Box)'로 이루어져 있습니다. 이미지도, 글자도, 버튼도 모두 상자입니다. 이 상자만 잘 이해하면 웹 디자인의 80%는 정복한 셈입니다.

Think of it this way: the Box Model is like the 'Package' or 'Courier Box' for the items we want to put on the web. This box consists of four layers. To help you understand, I'll explain it using the metaphor of a 'Delivery Package.'
이렇게 생각하면 쉽습니다. 박스 모델은 우리가 웹에 담고 싶은 물건을 감싸는 '패키지'나 '택배 상자'와 같습니다. 이 상자는 총 네 개의 겹으로 이루어져 있습니다. 여러분의 이해를 돕기 위해 '택배 상자' 비유를 들어 설명하겠습니다.

First is the **Content**. This is the **'Item'** you want to send. It's the core substance of the box, like a piece of clothing or an electronic device. In CSS, it's the actual content like text or an image.
첫 번째는 **내용물(Content)**입니 다. 이것은 여러분이 보내고 싶은 **'물건'** 그 자체입니다. 상자의 핵심 알맹이로, 옷 한 벌이나 전자 기기 같은 것이죠. CSS에서는 글자나 이미지 같은 실제 내용물에 해당합니다.

Second is the **Padding**. If you just put an item in a box, it might break during shipping, right? So we wrap the item in **'Bubble Wrap (Air Cap)'**. It's the inner space between the item and the box's paper. In CSS, padding means the **inner margin between the content and the border**. When you want to place text in the very center of a box or want to give it some breathing room so it doesn't look too cramped, you can wrap it thickly with this padding bubble wrap.
두 번째, **패딩(Padding)**입니다. 물건을 그냥 박스에 넣으면 배송 중에 깨질 수 있겠죠? 그래서 우리는 물건 주위에 **'뽁뽁이(에어캡)'**를 감쌉니다. 물건과 박스 종이 사이의 안쪽 공간이죠. CSS에서 패딩은 **내용물과 테두리 사이의 안쪽 여백**을 의미합니다. 내가 글자를 상자의 정중앙에 두고 싶거나, 상자 안에서 글자가 너무 답답해 보이지 않게 숨통을 틔워주고 싶을 때 이 패딩 뽁뽁이를 두껍게 감싸면 됩니다.

Third is the **Border**. This is the **'Cardboard Box'** itself that holds the item—its thickness and material. It's the reality of the box. You can make the border invisible or make it look like a very thick iron box. Only when this border exists do the boundaries of the box become clear.
세 번째, **테두리(Border)**입니다. 이것은 물건을 담고 있는 **'종이 상자'** 그 자체의 두께와 재질입니다. 상자의 실체죠. 테두리를 아예 안 보이게 할 수도 있고, 아주 두꺼운 철제 상자처럼 만들 수도 있습니다. 이 테두리가 있어야 비로소 상자의 경계가 명확해집니다.

Finally, the fourth is the **Margin**. This is the **'Social Distancing'** between my delivery box and the neighbor's delivery box. It's the margin on the outside of the box. If dozens of packages are stacked in front of your front door and the boxes are too close to each other, it'll be hard to pick them up, right? Leaving a proper distance so the boxes don't bump into each other is exactly what the margin does.
마지막 네 번째, **마진(Margin)**입니다. 이것은 내 택배 상자와 옆집 택배 상자 사이의 **'사회적 거리두기'**입니다. 상자 바깥쪽의 여백이죠. 우리 집 현관 앞에 택배가 수십 개 쌓여 있는데, 상자끼리 너무 딱 붙어 있으면 집어 올리기 힘들겠죠? 상자들끼리 서로 부딪히지 않게 적당한 거리를 띄워주는 것이 바로 마진입니다.

Shall we summarize? **[Inner margin is Padding, the box itself is the Border, and the outer distance is the Margin.]** If you memorize these three names perfectly, half of today's class is over.
정리해 볼까요? **[안쪽 여백은 패딩, 상자 자체는 보더, 바깥쪽 거리는 마진]**입니다. 이 세 가지 이름만 완벽히 외우면 오늘 수업의 절반은 끝난 겁니다.

Now, let me show you directly how to manipulate these concepts with real code. Everyone, please pay attention to the StackBlitz screen. I've opened the precious 'Online Business Card' project exactly as we finished it together last week (Week 5). Your favorite colors and fonts are already applied, right? Currently, this entire business card is stuck too close to the corner of the screen.
이제 실전 코드로 이 개념들을 어떻게 조작하는지 직접 보여드리겠습니다. 다들 앞의 StackBlitz 화면을 주목해 주세요. 제가 지난주(5주차)에 여러분과 함께 완성했던 우리 소중한 '온라인 명함' 프로젝트를 StackBlitz에서 그대로 열었습니다. 이미 여러분이 좋아하는 색상과 폰트가 입혀져 있죠? 지금은 이 명함 전체가 화면 구석에 너무 딱 붙어 있습니다.

*(Instructor starts live coding)*
*(강사가 라이브로 코딩 시작)*

```css
.card {
  border: 5px solid blue;
}
```

Can you see it? By giving a blue border to the `.card` class that wraps the entire business card, the reality of the entire 'box' that this business card occupies has finally been revealed. However, the text and content are stuck too close to the border, which doesn't look good. It looks like the business card is trapped in a narrow prison. All right, let's deploy the **Bubble Wrap** here.
보이시나요? 명함 전체를 감싸는 `.card` 클래스에 파란색 테두리를 주었더니 드디어 이 명함이 차지하고 있는 전체 '상자'의 실체가 드러났습니다. 그런데 글자와 내용물이 테두리에 너무 바짝 붙어 있어서 보기가 안 좋네요. 마치 좁은 감옥에 명함이 갇힌 것 같습니다. 자, 여기서 **뽁뽁이**를 투입하겠습니다.

```css
.card {
  border: 5px solid blue;
  padding: 30px;
}
```

Wow! As soon as `padding` was added, the contents of the business card comfortably pushed toward the center inside the box, finding some breathing room. Does the business card box itself look bigger? That's right. Filling the inner margin also increases the total size of the box by that much.
와! `padding`을 주자마자 명함 내용물들이 상자 안쪽에서 편안하게 가운데로 밀려나며 여유를 찾았습니다. 명함 상자 자체가 커진 것처럼 보이시죠? 맞습니다. 안쪽 여백을 채우면 상자의 전체 크기도 그만큼 커집니다. 

So now, let's move this business card box toward the center of the screen a bit. Right now, it's too stuck in the left corner. Let's apply `margin`, which is the outer space, or **Social Distancing**.
그럼 이제 이 명함 상자를 화면 중앙 쪽으로 좀 치워보겠습니다. 지금은 화면 왼쪽 구석에 너무 붙어 있거든요. 상자 바깥쪽 공간, 즉 **사회적 거리두기**인 `margin`을 적용해 보죠.

```css
.card {
  border: 5px solid blue;
  padding: 30px;
  margin: 100px;
}
```

Yes, perfect! The business card box is now 100 pixels away from the corner of the screen and is beautifully positioned.
네, 완벽합니다! 명함 상자가 화면 구석에서 100픽셀만큼 멀어지며 멋지게 자리를 잡았습니다. 

Everyone, let me give you a very important tip here. Just like we wear a top, bottom, left sleeve, and right sleeve separately when we dress, we can also adjust the padding and margin for the top, bottom, left, and right individually. Like `margin-top`, `margin-bottom`, `margin-left`, and `margin-right`. If you want to slightly distance only the area below the title text in the business card you've made, you can just pick and give a value to `margin-bottom`.
여러분, 여기서 아주 중요한 팁 하나를 드릴게요. 우리가 옷을 입을 때 상의, 하의, 왼쪽 소매, 오른쪽 소매를 따로 입듯이 패딩과 마진도 상하좌우를 각각 따로 조절할 수 있습니다. `margin-top`, `margin-bottom`, `margin-left`, `margin-right`처럼 말이죠. 만약 여러분이 만든 명함에서 제목 글자 아래쪽만 살짝 띄우고 싶다면 `margin-bottom`만 콕 집어서 값을 주면 되는 겁니다.

So, that's the basics of the Box Model. If the slogan "Inner is Padding, Outer is Margin!" is stuck in your head, we now have powerful magic in our hands to freely place all elements of a web page in the positions we want.
자, 여기까지가 박스 모델의 기초입니다. "안쪽은 패딩, 바깥쪽은 마진!" 이 구호가 머릿속에 박혔다면 이제 우리는 웹페이지의 모든 요소들을 우리가 원하는 위치에 자유자재로 배치할 수 있는 강력한 마법을 손에 넣은 것입니다.

Before we move on to practice, I'll introduce the most important "Layout Solver" in CSS to wrap up session S2. It's a **magical line of code** that will reduce your layout stress by 90%.
수업 S2의 마지막으로, 레이아웃을 잡을 때 여러분의 스트레스를 90% 줄여줄 가장 중요한 "레이아웃 해결사(Layout Solver)"를 소개하며 넘어가겠습니다. 바로 **마법의 코드 한 줄**입니다.

First, let's talk about the problem. When you create a layout, if you set the width and then add `padding` or `border`, the actual box size gets bigger, overflowing to the right or dropping to the next line. This is because the initial width only counts the "content area," so the padding and border are added outwardly.
먼저, 박스가 자꾸 커지는 문제에 대해 이야기해 보겠습니다. 레이아웃을 잡을 때 너비(`width`)를 지정하고 `padding`이나 `border`를 추가하면 실제 박스 크기가 자꾸 커져서 오른쪽으로 삐져나가거나 아랫줄로 툭 떨어지는 현상이 생깁니다. 기본적으로 너비는 "콘텐츠(내용물) 영역"만을 의미하므로, 패딩과 단단한 테두리가 바깥쪽으로 덧붙기 때문입니다.

To solve this, we use the property `box-sizing: border-box;`. This "forces" both the padding and the border to be included inside the width you defined. No matter how thick your padding or border is, the external width of the box stays fixed, and only the internal space for the content shrinks.
이를 해결하는 구원 투수가 바로 `box-sizing: border-box;` 속성입니다. 이 속성은 패딩과 테두리를 여러분이 지정한 너비 안에 "강제로" 포함되도록 만듭니다. 즉, 패딩이나 테두리를 아무리 두껍게 주어도 상자의 전체 외부 너비는 고정되고 내부 콘텐츠가 들어갈 공간만 줄어들게 됩니다.

*(Instructor action: Scroll down to the newly added 'Box Model Lab' section in the bottom of index.html and demonstrate the visual difference between content-box and border-box)*
Now, please look at the 'Box Model Lab' area I added below in your index.html. Both boxes are set to 300px width. But watch what happens when we add bold padding. The upper box, which uses the default setting, grew way beyond its container! However, the lower solver box safely maintained its exact width.
*(강사 액션: index.html 하단에 새로 추가한 'Box Model Lab' 영역으로 스크롤하여, 화면에서 직접 content-box와 border-box의 시각적 차이를 시연)*
자, 이제 여러분의 index.html 하단에 제가 추가해 둔 'Box Model Lab' 영역을 보세요. 두 박스 모두 똑같이 300픽셀 너비를 주었습니다. 그런데 두꺼운 패딩과 테두리를 추가했더니 어떻게 되었나요? 기본 설정인 위쪽 박스는 뚱뚱해져서 삐져나갔지만, 아래쪽 해결사 박스는 원래 지정한 너비를 안전하게 유지하고 있습니다.

*(Instructor action: Demonstrate applying the property to the `*` selector at the top of the code to fix everything)*
Because this setting makes layout calculations extremely intuitive, it has become an essential declaration for almost all modern web developers. When starting a project, they apply `* { box-sizing: border-box; }` to everything first. 
*(강사 액션: 코드 최상단 `*` 선택자에 해당 속성을 적용하는 시연)*
레이아웃 수치 계산을 아주 직관적으로 만들어주기 때문에, 현대의 모든 웹 개발자들에게 이것은 "필수 선언"이나 다름없습니다. 프로젝트를 시작할 때 모든 요소(`*`)에 `box-sizing: border-box;`를 가장 먼저 적용하고 출발하는 것이 정석입니다.

The moment you write this one line, you will be liberated from the mathematical hell of box size calculation. Please make sure to remember this magic spell.
이 한 줄을 적는 순간, 여러분은 박스 크기 계산이라는 수학적 지옥에서 해방될 것입니다. 이 마법의 주문을 꼭 기억해 두세요.

Now, let's apply these skills we just learned to our 'Personal Business Card' project that we've been upgrading since last week. You've all made things like 'Guestbook' or 'Send Email' buttons at the bottom, right? But how are those buttons looking right now? They're sticking too close to each other, like they're joined at the hip. They're so close that you might click the wrong one. Let's do some **'Live Debugging'** together using the box model and developer tools we just learned to give these buttons some breathing room.
자, 방금 배운 이 기술들을 우리가 지난주부터 업그레이드해 오고 있는 '나만의 명함' 프로젝트에 바로 써먹어 봅시다. 다들 아래쪽에 '방명록'이나 '이메일 보내기' 버튼 같은 걸 만들어 두었죠? 그런데 지금 그 버튼들이 어떤가요? 서로 의리 있게(?) 딱딱 어깨를 나란히 하고 붙어 있습니다. 너무 붙어 있어서 잘못 누를 것 같네요. 방금 배운 박스 모델과 개발자 도구를 활용해서 버튼 사이에 숨통을 틔워주는 **'라이브 디버깅'**을 함께 해보겠습니다.

*(Instructor Action: Demonstrate live coding by adding margin to button elements to align them)*
Let's add a line of `margin-right: 15px;` to the button class. Ta-da! Now the buttons are keeping a polite distance and are nicely separated. This is how web design is completed—through the persistence of handling margins at the pixel level.
*(강사 액션: 버튼 요소에 마진을 주어 정렬하는 라이브 코딩 시연)*
버튼 클래스에 `margin-right: 15px;`를 한 줄 넣어보겠습니다. 짠! 이제 버튼들이 서로 예의를 지키며 기분 좋게 떨어졌습니다. 이렇게 웹 디자인은 픽셀 단위의 여백을 다루는 집요함에서 완성됩니다.

---

## [S3] Information Hunter: Advanced Googling and Data Structuring (Approx. 25 min)
## [S3] 정보 사냥꾼: 고급 구글링 및 데이터 구조화 (약 25분)

*(Instructor Note: S3 consists of Google search operators and Google Sheets practice. Please prepare a blank Google Sheets window in advance.)*
*(강사 참고: S3는 구글 검색 연산자와 구글 시트 실습으로 구성됩니다. 빈 구글 시트 창을 미리 준비하세요.)*

Now, we will begin the 'Information Hunter' special lecture, the highlight of today's class, which will upgrade your digital survival skills by one level. Just as important as coding skills is the **"ability to find accurate information as quickly as possible and make it your own."**
자, 이제 오늘 수업의 하이라이트이자, 여러분의 디지털 생존 능력을 한 단계 업그레이드해 줄 '정보 사냥꾼' 특강을 시작합니다. 코딩 실력만큼이나 중요한 것이 바로 **"정확한 정보를 가장 빠르게 찾아내서 내 것으로 만드는 능력"**입니다.

Everyone, when you don't know something, you ask Google, right? But even with the same question, some friends find the perfect solution in one second, while others spend an hour searching and end up on pages full of advertisements. This is because search is not **luck**, but a **skill**.
여러분, 모르는 게 생기면 구글에게 물어보시죠? 하지만 똑같은 질문을 해도 어떤 친구는 1초 만에 완벽한 해결책을 찾아오고, 어떤 친구는 한 시간 내내 검색해도 광고성 글만 가득한 페이지에서 헤맵니다. 이건 검색이 **운**이 아니라 **기술**이기 때문입니다.

I will introduce the 'Google operator' weapons that I will pass on to you today.
First is the **source specifying operator (`site:`)**. When we're studying the CSS box model and want to see only content from official sites like 'MDN' or 'W3Schools' instead of various explanations from countless other blogs, type `box-sizing site:developer.mozilla.org` into the Google search bar. Google will search for information only within that specific domain among the hundreds of millions of sites in the world and present it to you. 
오늘 제가 여러분께 전수할 '구글 연산자' 무기들을 소개합니다. 
가장 먼저 **출처 지정 연산자 (`site:`)**입니다. 우리가 CSS 박스 모델에 대해 공부하다가, 다른 수많은 블로그의 잡다한 설명 말고 'MDN'이나 'W3Schools' 같은 공식 사이트의 내용만 딱 보고 싶을 때가 있죠? 그럴 땐 구글 검색창에 `box-sizing site:developer.mozilla.org`라고 치세요. 구글은 전 세계 수억 개의 사이트 중 오직 해당 영역 안에서만 정보를 뒤져서 여러분께 바칩니다. 

Next is the **word exclusion operator (`-`)**. If you want to search for 'Apple' but keep getting iPhone ads, try writing `-iphone` after your search term. Then Google will automatically throw the junk information into the trash for you. 
다음은 **단어 제외 연산자 (`-`)**입니다. '애플'에 대해 찾고 싶은데 자꾸 아이폰 광고만 나온다면? 검색어 뒤에 `-iphone`이라고 적어보세요. 그러면 구글이 알아서 쓰레기 정보들을 쓰레기통에 버려줍니다. 

Finally, there's the **file specifying operator (`filetype:pdf`)**. When writing a university report, you need official reports or papers rather than blog posts, right? If you attach this operator after your search term, you can directly open only official PDF documents. 
마지막으로 **파일 지정 연산자 (`filetype:pdf`)**입니다. 대학 리포트를 쓸 때 블로그 글보다는 공식 리포트나 논문이 필요하죠? 검색어 뒤에 이 연산자를 붙이면 바로 공식 PDF 문서만 열어볼 수 있습니다. 

Now, once you've hunted for information, you need to put those fragments neatly into your own container. That container is **'Google Sheets.'**
자, 이제 정보를 사냥했다면 그 파편들을 내 그릇에 예쁘게 담아야 합니다. 그 그릇이 바로 **'구글 스프레드시트'**입니다. 

*(Instructor Note: Display a blank Google Sheet on the screen. Demonstrate importing table data from the web.)*
*(강사 참고: 빈 구글 시트를 화면에 띄웁니다. 웹의 표 데이터를 가져오는 시연을 합니다.)*

Suppose you've found a table full of useful data on a website (like a list of famous restaurants or celebrity info). If you just copy and paste it, the table will break. In this case, press `Ctrl + Shift + V`. This is a professional technique to discard messy formatting and bring in only the pure data plainly.
웹사이트에서 유용한 데이터(맛집 리스트나 연예인 정보 등)가 가득한 표를 발견했다고 칩시다. 그냥 복사해서 붙여넣으면 표가 다 깨집니다. 이때는 `Ctrl + Shift + V`를 누르세요. 지저분한 서식은 버리고 순수한 데이터만 담백하게 가져오는 전문가의 기술입니다.

Once you've poured the data into the sheet, you need to establish three pillars.
First is **Frame Freezing**. When there's a lot of data and you scroll down, the title row disappears, right? Click [View] - [Freeze] - [1 Row]. Now the title will always be fixed at the top. 
시트에 데이터를 부었다면 이제 세 가지 뼈대를 잡아야 합니다.
첫째, **틀 고정**입니다. 데이터가 많아서 내리다 보면 제목 줄이 안 보이죠? [보기] - [틀 고정] - [행 1개]를 누르세요. 이제 제목은 항상 위에 고정됩니다. 

Second is **Sorting**. Want to create a ranking table from randomly mixed numbers? Click the column and select 'Sort Sheet.' With one click of 'Sort Z-A,' the entire sheet will be rearranged from largest to smallest numbers. 
둘째, **정렬(Sort)**입니다. 무작위로 섞인 숫자들 사이에서 순위표를 만들고 싶다면? 열을 클릭하고 '시트 정렬'을 누르세요. '내림차순(Z-A)' 한 번이면 큰 숫자부터 작은 숫자 순으로 시트 전체가 촤르륵 재배치됩니다. 

Third is **Conditional Formatting**. When you want to see large and small numbers at a glance among many, apply [Format] - [Conditional Formatting] - [Color Scale]. In an instant, your black-and-white table transforms into a color map that shows hot and cold data like a thermal camera. 
셋째, **조건부 서식**입니다. 수많은 숫자 중에서 큰 것과 작은 것을 한눈에 보고 싶을 때, [서식] - [조건부 서식] - [색상 스케일]을 적용해 보세요. 흑백의 표가 순식간에 열화상 카메라처럼 뜨거운 데이터와 차가운 데이터를 보여주는 색상 지도로 변합니다. 

Finally, the king of data analysis: **Pivot Tables**. This feature lets you summarize massive amounts of data in just a few seconds. Clicking [Insert] - [Pivot Table] opens a new sheet, where you can find averages or sums with just a few clicks, without needing complex functions. Today, you'll learn how to cross-analyze multi-dimensional data, such as browser market share or sales by gender.
마지막으로 데이터 분석의 끝판왕, **피벗 테이블(Pivot Table)**입니다. 거대한 데이터의 요약을 단 몇 초 만에 끝내는 기능입니다. [삽입] - [피벗 테이블]을 누르면 새로운 시트가 열리고, 여러분은 복잡한 함수 없이도 클릭 몇 번으로 평균값이나 총합을 구할 수 있습니다. 브라우저별 점유율이나 성별 매출 같은 다차원 데이터를 교차 분석하는 법을 오늘 익히게 될 것입니다.

And here’s one more magical feature! **Smart Auto-Fill (Flash Fill)**. When you want to extract just dates or names from a cluster of complex text, try typing them manually two or three times in the adjacent column. Google Sheets will recognize the pattern and automatically fill in the remaining thousands of cells. When the gray preview appears, just hit **'Enter'** and you're done! 
여기에 마법 같은 기능 하나 더! **스마트 자동 채우기(Flash Fill)**입니다. 복잡한 텍스트 뭉치에서 날짜나 이름만 따로 쏙 뽑아내고 싶을 때, 옆 칸에 직접 두세 번만 적어보세요. 구글 시트가 패턴을 파악해서 나머지 수천 칸을 자동으로 채워줍니다. 회색으로 미리보기가 뜰 때 **'엔터'**만 치면 끝입니다! 

Let's wrap up today's class. We learned the physical structure of the web called the **Box Model**, and we learned how to catch the culprit using **Developer Tools** when we get lost in that structure. And finally, we mastered **advanced search and data analysis techniques** to hunt for and structure information when we encounter something we don't know. 
오늘 수업을 마무리하겠습니다. 우리는 **박스 모델**이라는 웹의 물리적 구조를 배웠고, 그 구조 속에서 길을 잃었을 때 **개발자 도구**로 범인을 잡는 법을 배웠습니다. 그리고 마지막으로 우리가 모르는 것이 생겼을 때 정보를 사냥하고 구조화하는 **고급 검색과 데이터 분석 기술**까지 익혔습니다. 

Everyone, coding is not just a study of memorization. It's a skill for handling tools and an attitude toward solving problems. With the 'beauty of margins' and 'data techniques' you learned today, I hope you'll make your business card sites much more relaxed and abundant. 
여러분, 코딩은 단순히 암기하는 공부가 아닙니다. 도구를 다루는 기술이고, 문제를 해결하는 태도입니다. 오늘 배운 '여백의 미'와 '데이터의 기술'을 가지고, 여러분의 명함 사이트를 훨씬 더 여유롭고 풍성하게 가꾸어 보시기 바랍니다. 

You all did a great job today. Oh, and you know, right? The data map you found with your search skills and organized with Sheets today must be captured and sent along in the body of your email for this week's **Micro-Assignment**. Don't forget that the submission deadline is Sunday at 9 PM!
오늘 정말 고생 많으셨습니다. 아, 아시죠? 여러분이 오늘 검색 기술로 찾아내고 시트로 정돈한 데이터 지도는 반드시 이번 주 **마이크로 과제**인 이메일 본문에 캡처해서 함께 보내주셔야 합니다. 제출 기한은 일요일 밤 9시까지인 거 잊지 마시고요!

Well then, everyone pack your bags and get home safely, and we'll meet again next week with more fun 'Layout and Flexbox' magic. That concludes the class! Great job, everyone!
자, 그럼 다들 짐 챙겨서 조심해서 돌아가시고, 우리는 다음 주에 더 재미있는 '레이아웃과 플렉스 박스'의 마법으로 다시 만나겠습니다. 이상 수업 마치겠습니다! 수고하셨습니다!
