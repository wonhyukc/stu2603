# wb07 주차 (E트랙 7주차) - 강사용 대본 (Instructor's Script)

## [S1] Flexbox 배치 원리 및 전반기 총정리 / Flexbox Principles & First Half Review (15분 / 15 min)

*(Instructor Note: 학생들을 환영하며 밝은 미소로 인사를 건넵니다. 화면에는 그동안 만들어온 결과물들의 캡처 화면들을 슬라이드로 띄워놓습니다.)*
*(Instructor Note: Welcome the students with a bright smile. Display a slide showing screenshots of the projects built so far.)*

안녕하십니까, 여러분! Wonhyuk William Chung입니다. 벌써 7주차 수업입니다. 시간이 정말 빠르죠?
Hello, everyone! I'm Wonhyuk William Chung. It's already our 7th week of class. Time flies, doesn't it?

우리는 지난 6주 동안 정말 많은 것을 함께 해왔습니다. 처음에는 HTML이 뭔지도 몰랐던 여러분이, 이제는 태그를 직접 쓰고, CSS로 색상을 입히고, 박스 모델로 여백까지 다루게 되었습니다. 1주차에 `<h1>Hello World</h1>`를 처음 쳤을 때의 그 설렘이 기억나시나요? 지금 여러분의 실력은 그때와 비교할 수 없을 만큼 성장했습니다.
We have accomplished so much together over the past six weeks. You started without knowing what HTML was, and now you are writing tags, adding colors with CSS, and managing margins with the Box Model. Do you remember the excitement of typing `<h1>Hello World</h1>` in the first week? Your skills have grown incomparably since then.

우리가 웹이라는 이름의 집을 짓기 시작했다면, 지금까지는 벽돌을 쌓고 페인트를 칠한 것과 같습니다. HTML이라는 뼈대를 만들고, CSS라는 옷을 입힌 뒤, 박스 모델을 통해 여백과 정렬을 조정했습니다. 그런데 혹시 여러분이 짠 코드를 보며 이런 답답함을 느낀 적 없으신가요? "아, 이 요소들을 옆으로 나란히 배치하고 싶은데 자꾸 아래로 떨어지네." "메뉴 바를 가로로 예쁘게 만들고 싶은데 왜 이렇게 마음대로 안 될까?" 네, 오늘 우리가 배울 핵심 마법 주문이 바로 그 문제를 해결해 줍니다. 바로 `display: flex`입니다. 우리는 이것을 보통 **Flexbox(플렉스박스)** 라고 부릅니다.
If we started building a house called the Web, so far we've been laying bricks and painting. We built the skeleton with HTML, clothed it with CSS, and adjusted spacing with the Box Model. But have you ever felt frustrated looking at your code, thinking, "Ah, I want to place these side by side, but they keep dropping to the next line," or "Why can't I make a horizontal menu bar exactly how I want it?" Well, today we'll learn the core magic spell to solve that exact problem. It's `display: flex`. We usually call this **Flexbox**.

Flexbox는 요소들을 여러분이 원하는 곳에 자유자재로 배치할 수 있게 해주는 아주 강력한 도구입니다. 상자들을 가로로 나란히 세울 수도 있고, 세로로 줄을 세울 수도 있습니다. 오른쪽 끝에 밀어 넣거나, 아니면 요소들 사이의 간격을 동일하게 띄워서 보기 좋게 정렬할 수도 있죠. 여러분, 마치 마트 진열대에 상품을 예쁘게 정돈하는 관리자가 된 것처럼, Flexbox를 사용하면 웹 브라우저라는 공간에 여러분의 요소들을 아주 깔끔하게 정리할 수 있습니다.
Flexbox is a very powerful tool that allows you to freely position elements exactly where you want them. You can align boxes horizontally in a row or vertically in a column. You can push them to the far right, or space them evenly to look nice. Everyone, just like a manager organizing products neatly on a supermarket shelf, using Flexbox allows you to perfectly organize your elements in the space of a web browser.

잠깐 비유를 하나 들어볼게요. 여러분이 방 안에 여러 개의 박스를 놓아야 하는 상황을 생각해 보세요. 일반적인 CSS 흐름, 즉 Flex를 쓰지 않은 상태는 마치 박스들이 서로 줄을 서는 기본 규칙에 따라 쌓이는 것과 같습니다. 무거운 박스는 아래에, 가벼운 박스는 위에. 그런데 우리가 원하는 건 박스들을 옆으로 나란히, 그리고 가운데로 딱 맞춰 세우고 싶을 때도 있잖아요? 그럴 때 Flexbox가 등장합니다. Flexbox는 마치 여러분이 박스들을 자유롭게 배치할 수 있는 특별한 '정렬 관리자'를 호출하는 것과 같습니다. 이 관리자에게 "가로로 나열해줘", "가운데 모아줘", "사이 간격을 똑같이 맞춰줘" 라고 명령을 내리면 그대로 실행해 줍니다.
Let me give you a brief analogy. Imagine you have to place several boxes in a room. The normal CSS flow, before using Flex, is like boxes stacking according to a basic waiting-in-line rule. Heavy boxes at the bottom, light ones on top. But sometimes we want to line them up side-by-side, perfectly centered, right? That's when Flexbox comes in. Flexbox is like summoning a special 'Alignment Manager' who can freely arrange your boxes. If you command this manager to "arrange horizontally," "gather in the center," or "make the spacing equal," it executes exactly that.

가장 중요하게 알아야 할 세 가지 핵심 속성을 차례로 설명하겠습니다.
I will sequentially explain the three most important core properties you need to know.

첫째로 **`flex-direction`** 입니다. 정렬의 방향을 결정합니다. `row`라고 적으면 가로 방향, 즉 행에 따라 요소들이 배치됩니다. 메뉴 바를 만들 때 필수적이겠죠? `column`이라고 적으면 세로 방향, 즉 열을 따라 요소들이 배치됩니다. 이 두 가지만 알아도 요소들의 전체적인 흐름을 통제할 수 있습니다. 기본값은 `row`이기 때문에 사실 `flex-direction: row;`를 생략해도 가로 정렬이 됩니다만, 명시적으로 적어두는 것이 코드를 나중에 읽기 좋게 만들어 줍니다.
First is **`flex-direction`**. It determines the direction of alignment. If you write `row`, elements are arranged horizontally. Essential for making menu bars, right? If you write `column`, elements go vertically. Just knowing these two allows you to control the overall flow. Since the default is `row`, you can actually omit `flex-direction: row;` and it will still align horizontally, but explicitly writing it makes your code much more readable later.

둘째로 **`justify-content`** 입니다. 가로로 요소들을 나열했을 때 그 요소들을 어떻게 띄울 것인지를 결정합니다. 꽉 찬 교실에서 학생들을 벽 쪽으로 모두 밀어 붙일 것인가? 중간으로 옹기종기 모이게 할 것인가? 아니면 학생들 사이의 간격을 균일하게 띄워서 앉힐 것인가? `center`, `space-between`, `space-around`와 같은 속성 값들이 바로 이렇게 간격을 마법처럼 조절해 줍니다. 수동으로 픽셀을 일일이 계산해서 여백을 줄 필요가 없습니다. 컴퓨터가 알아서 가장 예쁜 간격을 찾아주죠! `space-between`은 첫 번째와 마지막 요소를 양쪽 끝에 딱 붙이고, 중간 요소들 사이의 간격을 균등하게 분배합니다. `space-around`는 모든 요소의 양쪽에 동일한 여백을 줍니다. 따라서 첫 번째와 마지막 요소의 바깥쪽 여백은 안쪽 간격의 절반이 됩니다. 어떤 것을 쓸지는 디자인에 따라 결정하시면 됩니다.
Second is **`justify-content`**. When elements are laid out horizontally, it decides how they are spaced. In a full classroom, do you push all students against the wall? Clump them in the middle? Or seat them with even spacing? Values like `center`, `space-between`, and `space-around` adjust spacing like magic. No need to manually calculate pixels for margins. The computer finds the most aesthetically pleasing spacing automatically! `space-between` sticks the first and last elements to the ends and distributes equal space between the middle elements. `space-around` gives equal space on both sides of every element. So the outer margins of the first and last elements are half the inner gaps. Which one to use depends entirely on your design.

셋째로 **`align-items`** 입니다. `justify-content`가 가로(주축) 방향 정렬이라면, `align-items`는 세로(교차축) 방향 정렬을 담당합니다. 예를 들어, 높이가 서로 다른 메뉴 버튼들을 수직으로 가운데에 딱 맞추고 싶을 때 `align-items: center`를 사용합니다. 이 세 가지 속성 조합만 제대로 이해해도, 웬만한 레이아웃 문제는 해결됩니다. 나중에 실무에서도 이 세 가지는 매일 쓰게 될 겁니다.
Third is **`align-items`**. If `justify-content` aligns along the main horizontal axis, `align-items` handles the cross vertical axis. For example, to perfectly vertically center menu buttons of differing heights, you use `align-items: center`. Mastering just the combination of these three properties solves most layout problems. You'll be using these three every single day in the real industry.

한 가지 더 덧붙이자면, Flexbox는 **부모-자식 관계**를 기반으로 동작합니다. `display: flex`는 항상 **부모 요소**에 선언합니다. 그러면 그 안에 있는 **자식 요소들**이 Flex 아이템이 되어 부모의 규칙을 따릅니다. 이 개념을 헷갈리면 "왜 Flex를 썼는데 안 되지?" 하는 상황이 생깁니다. 반드시 기억하세요. **`display: flex`는 정렬할 요소들의 엄마(부모 컨테이너)에게 씁니다.**
One more thing: Flexbox operates strictly on a **Parent-Child relationship**. `display: flex` is ALWAYS declared on the **parent element**. Then, the **child elements** inside become Flex items and follow the parent's rules. Confusing this concept leads to situations where you ask, "Why isn't Flex working?" Always remember: **`display: flex` goes on the mother (parent container) of the elements you want to align.**

마지막으로 Flexbox를 처음 쓸 때 자주 하는 실수를 짚어드리겠습니다. 가장 흔한 실수는 자식 요소에 `display: flex`를 선언하는 것입니다. 자식 요소에 Flex를 선언하면, 그 자식의 자식들이 정렬되는 것이지, 원래 의도했던 자식들이 정렬되지 않습니다. 두 번째 실수는 Flex 컨테이너에 고정된 `height`를 주는 것입니다. `align-items: center`가 제대로 동작하려면 컨테이너에 높이가 있어야 합니다. 높이가 없으면 세로 정렬을 할 공간 자체가 없어서 효과가 안 보이는 것처럼 느껴집니다.
Lastly, I'll point out common mistakes beginners make. The most frequent error is declaring `display: flex` on a child element. If you do that, the descendants of that child get aligned, not the children you originally intended. The second mistake is putting a fixed `height` on the Flex container. For `align-items: center` to work correctly, the container must have a clear height. Without height, there's no vertical space to align within, making it seem like the effect is broken.

자, Flexbox는 이따가 2번째 세션에서 우리가 직접 실습해 보면서 몸으로 익혀볼 것입니다. 정말 신기할 정도로 한 줄의 코드가 화면을 확 바꿔버리는 것을 경험하실 수 있을 겁니다.
Now, we will experience Flexbox firsthand in our second session through direct practice. You will get to experience how just one line of code completely revamps the screen like magic.

## [S2] Flexbox Lab 실시간 데모 / Flexbox Lab Live Demo (15분 / 15 min)

*(Instructor Note:
[강사 사전 준비 및 데모 진행 순서]
1. `lecture-demo/index.html` 파일을 브라우저에 띄워 'Flexbox Lab' 화면을 학생들에게 보여줍니다.
2. 윗부분의 고정된 미리보기 영역과 아랫부분의 컨트롤러 영역을 안내합니다.
3. JavaScript 파일(`script.js`)이나 복잡한 HTML 구조는 무시하고, 상단의 CSS 대시보드와 버튼 간의 관계에만 집중하도록 유도합니다.
)*
*(Instructor Note:
[Instructor Prep & Demo Sequence]
1. Open `lecture-demo/index.html` in the browser to show students the 'Flexbox Lab'.
2. Explain the fixed preview area at the top and the controller area at the bottom.
3. Instruct them to ignore `script.js` or complex HTML, and focus entirely on the relationship between the top CSS dashboard and the bottom buttons.
)*

자, 드디어 2번째 세션입니다. 실제로 Flexbox라는 마법을 눈으로 확인해보겠습니다.
화면을 보세요. 제가 여러분을 위해 'Flexbox Lab'이라는 실시간 레이아웃 시뮬레이터를 준비했습니다. 파일 탐색기에서 `lecture-demo/index.html`을 열어보시면 똑같은 화면을 보실 수 있습니다.
Alright, finally our 2nd session. Let's see the magic of Flexbox with our own eyes. 
Look at the screen. I have prepared a real-time layout simulator called 'Flexbox Lab' for you. You can see the exact same screen by opening `lecture-demo/index.html` in your file explorer.

"어? 선생님, 갑자기 코드가 너무 길어지고 `script.js` 같은 모르는 파일도 생겼는데요?" 하시는 분들 계실 겁니다. **여기서 복잡해진 나머지 파일들이나 코드는 신경 쓰지 마세요. 지금은 오직 CSS에만 초점을 맞추겠습니다. 자바스크립트(script)는 나중에 배울 테니 지금은 완전히 무시하셔도 좋습니다.** 우리가 봐야 할 것은 오직 화면에 보이는 시각적 변화와, 그 변화를 만들어내는 4가지 핵심 CSS 속성뿐입니다. 
Some of you might say, "Teacher, the code suddenly got so long and there are unknown files like `script.js`!" **Do not worry about the rest of these complex files or codes. Right now, we will focus solely on CSS. We will learn JavaScript later, so you can completely ignore it for now.** All we need to look at is the visual change on the screen and the 4 core CSS properties driving those changes.

화면을 위아래로 나누어 봅시다. 위쪽 프레임은 우리의 실험실입니다. 8개의 크기와 모양이 다른 상자들이 들어 있죠? 그리고 바로 아래쪽 하단 프레임에는 이 상자들을 마음대로 조종할 수 있는 조이스틱, 바로 컨트롤 버튼들이 있습니다. 버튼을 클릭하기 위해 스크롤을 내려도 위의 실험실 화면은 고정되어 있으니 아주 편하게 결과를 확인할 수 있어요.
Let's divide the screen top and bottom. The top frame is our laboratory. It contains 8 boxes of different sizes and shapes, right? And directly below in the bottom frame, we have joysticks—control buttons—to manipulate these boxes. The laboratory screen above remains fixed even when you scroll down to click buttons, making it super easy to see the results.

자, 첫 번째 조이스틱인 **`flex-direction`**부터 만져보겠습니다. `row` (가로) 상태에서 `column` 버튼을 눌러볼까요?
*(Instructor Note: `column` 버튼 클릭)*
*(Instructor Note: Click the `column` button)*
Now, let's play with our first joystick, **`flex-direction`**. Let's press the `column` button from the `row` state.

순식간에 8개의 상자가 세로로 탑을 쌓았습니다! 메뉴바를 만들 땐 `row`, 모바일 화면 전체를 구성할 땐 통상 `column`을 쓴다고 이해하시면 됩니다. 
In a flash, the 8 boxes stacked up vertically into a tower! Just understand that we use `row` for making menu bars, and typically `column` when structuring entire mobile screens.

다시 `row`로 돌려놓고, 이번엔 두 번째 조이스틱인 **`justify-content`**를 보겠습니다. 
*(Instructor Note: `space-between`과 `space-around` 클릭을 번갈아가며 시연)*
*(Instructor Note: Demonstrate by clicking `space-between` and `space-around` alternately)*
Let's switch it back to `row`, and this time check out the second joystick, **`justify-content`**.

`space-between`을 누르면 상자들이 양쪽 끝 벽에 찰싹 붙고 가운데가 벌어지죠? 반면에 `space-around`를 누르면 양 끝에도 여백이 생깁니다. 아까 이론 시간에 배운 '정렬 관리자'가 빈 공간을 어떻게 나눠줄지 명령하는 곳입니다. 직접 눌러보시면서 이 직관적인 느낌을 손에 익히세요.
When you click `space-between`, the boxes stick flat against the side walls and the middle opens up, right? Conversely, `space-around` adds margins to both extreme ends as well. This is where you command our 'Alignment Manager' from theory time on how to divide empty space. Please click them yourself and get a hands-on feel for this intuitive difference.

세 번째는 **`align-items`**입니다. 가로로 아이템이 늘어서 있을 때, 수직으로 어떻게 맞출지 결정합니다. 
*(Instructor Note: `flex-start`와 `baseline` 클릭 시연)*
*(Instructor Note: Demonstrate clicking `flex-start` and `baseline`)*
Third is **`align-items`**. While items are stretched out horizontally, this decides how they align vertically.

화면을 잘 보세요. 상자들의 크기가 제각각이죠? `flex-start`를 누르면 상자들의 '천장(위쪽 테두리)'이 일직선으로 맞습니다. 그런데 제가 아까 타이포그래피에서 아주 중요하다고 했던 `baseline` 버튼을 눌러보겠습니다. 짠! 상자 모양은 삐뚤빼뚤해 보이지만, 안쪽에 적힌 숫자 '1, 2, 3, 4'의 바닥 라인이 자를 댄 것처럼 완벽하게 일렬로 맞춰집니다. 메뉴나 텍스트를 나란히 배치할 때 이 `baseline`을 꼭 기억해두세요.
Watch the screen closely. The boxes are all different sizes, right? If you click `flex-start`, the 'ceilings' (top borders) of the boxes align perfectly straight. Now, let's click the `baseline` button, which I emphasized as very important in typography earlier. Ta-da! The outer box shapes look jagged, but the bottom lines of the text numbers '1, 2, 3, 4' align perfectly straight as if drawn with a ruler. Always remember this `baseline` when placing menus or text side-by-side.

마지막 조이스틱, **`flex-wrap`**입니다. 상자들이 화면의 좁은 공간에 갇혔을 때, 어떻게 할 것인가를 결정하죠.
*(Instructor Note: `wrap`과 `wrap-reverse` 시연)*
*(Instructor Note: Demonstrate `wrap` and `wrap-reverse`)*
Our final joystick is **`flex-wrap`**. It decides what happens when the boxes are trapped in a narrow screen space.

`nowrap` 상태에서는 제가 브라우저 크기를 아무리 줄여도 상자들이 한 줄에 찌그러져서라도 버티려고 합니다. 하지만 `wrap`을 누르면 어떻게 되죠? 무리하지 않고 자연스럽게 다음 줄로 밀려납니다. 마치 글씨를 쓸 때 다음 줄로 넘어가듯 말이죠. 이 속성 덕분에 스마트폰의 좁은 화면에서도 레이아웃이 깨지지 않는 반응형 웹을 만들 수 있습니다.
In the `nowrap` state, no matter how small I shrink the browser, the boxes try to survive on a single line, even if they have to squash themselves. But what happens if you press `wrap`? They naturally get pushed to the next line without forcing it. Just like wrapping text to a new line when writing. Because of this property, we can create responsive websites where layouts never break, even on small smartphone screens.

**여러분, 이 4줄의 코드가 사실 전부입니다.** 이걸 달달 외우실 필요는 없습니다. "가로로 나열하고 싶다? Flex 쓰면 된다." 그리고 "이 4가지 버튼이 각각 어떤 느낌이었지?" 하는 직관만 남기시면 충분합니다. 나머지는 구글링하거나 AI에게 물어보면 바로 코드를 뱉어주니까요. 이 시뮬레이터를 수업이 끝나고도 마음껏 가지고 놀면서 감각을 익혀보시기 바랍니다.
**Everyone, these 4 lines of code are actually everything.** You don't need to memorize them by heart. Just keep the intuition: "Want to arrange horizontally? Use Flex." and "What did each of those 4 buttons feel like?". That's enough. You can always just Google it or ask AI, and it will spit out the code instantly. I hope you play around with this simulator to your heart's content even after class to master the feel for it.

## [S3] 레이아웃 리팩터링 / Layout Refactoring (15분 / 15 min)

*(Instructor Note:
[강사 사전 준비 및 디버깅 시연 순서]
1. 앞서 학생들이 실습 중인 `lab/index.html` 파일을 브라우저에 띄웁니다. 하단(38번째 줄 주변)의 프로필 이미지(`<img class="profile-img-buggy">`)가 부모 컨테이너 밖으로 심하게 튀어나가 있는 상황을 보여줍니다.
2. 학생들에게 브라우저 개발자 도구(F12)를 열어 엘리먼트 탭(Elements)에서 해당 이미지가 `width: 1000px;`로 고정되어 부모 박스의 유연성을 무시하고 있음을 짚어줍니다.
3. 개발자 도구의 스타일 탭에서 직접 아래와 같이 코드를 수정하며 튀어나간 이미지가 카드로 쏙 들어가는 것을 시연합니다.

```css
.profile-img-buggy {
    /* 원흉인 width: 1000px; 를 체크 해제(삭제)합니다. */
    
    /* 아래 코드를 입력하여 이미지가 부모 크기를 넘지 못하게 합니다. */
    max-width: 100%;
    height: auto;
}
```
)*
*(Instructor Note:
[Instructor Prep & Demo Sequence]
1. Open the `lab/index.html` file students were practicing with in the browser. Show the situation where the profile image (`<img class="profile-img-buggy">`) at the bottom (around line 38) is severely overflowing outside its parent container.
2. Tell students to open the browser Developer Tools (F12) and point out in the Elements tab that the image is fixed at `width: 1000px;`, ignoring the flexibility of the parent box.
3. In the Styles tab of Developer Tools, directly modify the code as shown below to demonstrate the overflowing image sliding perfectly back into the card.
(Keep the CSS block exactly as is)
)*

이제 마지막 3번째 세션입니다. 여러분, 코딩을 하다 보면 우리가 입력하는 코드가 항상 내 마음처럼 움직여 주진 않죠. 화면을 보세요. 이 사이트는 아주 심각한 문제를 겪고 있습니다. 밑에 있는 사진이 본문 영역을 뚫고 밖으로 심하게 튀어나가 버려서 레이아웃이 아주 엉망진창이죠.
Now for our final 3rd session. Everyone, when coding, the code we type doesn't always behave the way we want it to, right? Look at the screen. This site is suffering from a very serious problem. The photo at the bottom has severely pierced through the main content area and popped out, making the layout a total mess.

우리는 코드를 처음 작성하는 능력만큼이나 에러가 나거나 꼬여있는 기존의 코드를 고치고 개선하는, 즉 **리팩터링(Refactoring)** 하는 능력을 길러야 합니다. 리팩터링이라는 단어가 처음에는 어렵게 느껴질 수 있지만, 간단하게 말하면 "작동은 하되, 더 나은 방식으로 코드를 다시 정리하는 것"입니다. 실제 현업에서 개발자들이 하는 일의 상당 부분은 새 코드를 작성하는 것이 아니라, 이미 짜여진 코드를 읽고 고치는 일입니다. 그래서 리팩터링 능력은 어쩌면 처음 코드를 짜는 능력보다 더 중요할 수 있어요.
We must develop the ability to fix and improve existing code that has errors or is tangled up—in other words, **Refactoring**—just as much as we develop the ability to write code from scratch. The word refactoring might sound difficult at first, but simply put, it means "restructuring the code in a better way, while keeping it functional." A significant portion of what developers actually do in the industry isn't writing new code, but reading and fixing already written code. Therefore, refactoring skills can arguably be even more important than the ability to write code for the first time.

이 버그를 잡으려면 무작정 코드를 지웠다 썼다 하면 안 됩니다. 문제를 진단할 청진기가 필요합니다. 브라우저에서 `F12` 키를 누르면 나오는 **개발자 도구(Developer Tools)** 가 바로 의사들의 청진기입니다.
To catch this bug, you shouldn't just blindly delete and rewrite code. You need a stethoscope to diagnose the problem. Pressing the `F12` key in your browser opens the **Developer Tools**, which is exactly that doctor's stethoscope.

*(Instructor Note: 브라우저에서 F12를 눌러 개발자 도구를 열어 보여줍니다.)*
*(Instructor Note: Press F12 in the browser to open and show the Developer Tools.)*

개발자 도구의 왼쪽 패널에는 HTML 구조가 나무처럼 펼쳐져 있습니다. 이것을 **DOM 트리**라고 부릅니다. 오른쪽에는 선택한 요소에 적용된 CSS 스타일이 나옵니다. 이 두 패널을 함께 보면, 어떤 요소가 어떤 스타일을 받고 있는지 실시간으로 확인할 수 있습니다.
In the left panel of Developer Tools, the HTML structure is spread out like a tree. We call this the **DOM Tree**. On the right, the CSS styles applied to the selected element appear. By looking at these two panels together, you can see in real-time which element is receiving which styles.

화면의 개발자 도구를 켜서 이 튀어나간 요소 위에 마우스를 올려보겠습니다. 좌측 상단의 마우스 커서 모양 아이콘(Inspector 도구)을 클릭하고, 튀어나간 이미지 위에 마우스를 갖다 대면 해당 요소가 DOM 트리에서 하이라이트됩니다. 아, 보니까 이 자식 요소가 부모 상자의 크기 제한인 width 값 100%를 무시하고 픽셀값으로 강제로 고정되어 버렸네요. 부모 상자는 고무줄처럼 변하는데, 이 자식 이미지가 굳건한 쇳덩이처럼 본인의 픽셀 크기를 주장하다 보니 화면이 좁아질 때 밖으로 튀어나가는 현상(**Overflow**)이 발생한 것입니다.
Let's turn on the Developer Tools on screen and hover the mouse over this overflowing element. Let's click the mouse cursor icon (Inspector Tool) in the top left and point at the overflowing image; notice how that element highlights in the DOM tree. Ah, looking here, this child element has ignored the parent box's size limit of width 100% and has been forcibly fixed to a pixel value. The parent box changes elastically like a rubber band, but because this child image stands firm like a piece of iron asserting its own pixel size, an **Overflow** phenomenon occurs where it pops out when the screen narrows.

이를 픽셀 고정이 아닌 `%` 비율이나 `max-width: 100%`로 유연하게 수용할 수 있게 코드를 바꾸도록 하겠습니다. 개발자 도구 오른쪽 스타일 패널에서 `width: 1000px;` 옆에 있는 체크박스를 클릭해서 해제해 봅시다. 그리고 새 규칙으로 `max-width: 100%;`와 `height: auto;`를 입력합니다.
Let's change the code to flexibly accommodate this with `%` ratios or `max-width: 100%` instead of fixing pixels. Let's uncheck the box next to `width: 1000px;` in the style panel on the right side of Developer Tools. Then, let's type in a new rule: `max-width: 100%;` and `height: auto;`.

자, 어떻습니까. 개발자 도구에서 코드를 바로 수정해서 쳐보니까 이제 이미지 파일이 예쁘게 부모 사이즈 안으로 쏙 들어와서 창이 줄어들면 같이 맞춰서 줄어들죠? 여러분이 만약 도구 사용법을 몰랐다면 저 이미지가 삐져나온 원인을 찾지 못해 하루하루 밤을 설쳤을 겁니다. 이렇게 디버깅은 도구를 써서 문제의 '원인'을 정밀 타격하는 과정입니다.
Well, how is it? Since we immediately modified and typed the code in the Developer Tools, the image file now slides beautifully into the parent size, shrinking along nicely when the window shrinks, right? If you hadn't known how to use the tools, you wouldn't have been able to find the cause of that protruding image and would have tossed and turned at night. In this way, debugging is the process of using tools to perform a precision strike on the 'cause' of the problem.

중요한 원칙 하나를 더 짚고 가겠습니다. **개발자 도구에서 수정한 내용은 임시 수정입니다.** 브라우저를 새로고침하면 원래대로 돌아갑니다. 따라서 개발자 도구는 "이 스타일을 적용하면 어떻게 보일까?" 를 빠르게 테스트하는 용도로 쓰고, 마음에 들면 그 코드를 실제 CSS 파일에 옮겨 저장해야 합니다. 이 순서를 꼭 기억하세요. 도구에서 확인 → 파일에 적용 → 저장.
Let me point out one more important principle. **Modifications made in Developer Tools are temporary.** If you refresh the browser, they revert to the original state. Therefore, Developer Tools is used for quickly testing "how would it look if I applied this style?". If you like the result, you must move that code into your actual CSS file and save it. Remember this sequence: Check in Tools → Apply to File → Save.

이번 세션에서 여러분이 가져가야 할 핵심 메시지는 두 가지입니다. 첫째, 문제가 생겼을 때 무작정 코드를 지우고 다시 쓰지 마세요. 개발자 도구라는 진단 도구를 먼저 여세요. 둘째, `width`에 고정 픽셀값을 줄 때는 항상 부모 컨테이너의 크기와 비교하세요. 부모보다 자식이 크면, 자식이 밖으로 튀어나옵니다. 이 두 가지 원칙만 지켜도 레이아웃 관련 버그의 절반 이상은 쉽게 해결할 수 있습니다.
There are two core messages you should take away from this session. First, when a problem occurs, don't just blindly delete and rewrite code. Open your diagnostic tool—the Developer Tools—first. Second, whenever you give a fixed pixel value to `width`, always compare it to the size of the parent container. If the child is bigger than the parent, the child will overflow. Just adhering to these two principles alone will easily resolve more than half of layout-related bugs.

여러분! 오늘 배운 Flexbox 레이아웃과 리팩터링은 웹 페이지를 구조적으로 배치하는 핵심 무기입니다. 오늘 배운 내용을 여러분의 포트폴리오 사이트에 꼭 반영해 보시기 바랍니다.
Everyone! The Flexbox layout and Refactoring we learned today are core weapons for structurally aligning web pages. Please make sure to reflect what you've learned today onto your own portfolio sites.

## [S4] [특강] 컴퓨터 활용도 (30분)

*(Instructor Note: 화면에 바탕화면이 지저분한 예제 상태(파일들이 무질서하게 널려 있는 화면)를 미리 준비해 띄워놓습니다. 컴퓨터 활용도 특강은 딱딱한 기술 강의가 아니라, 학생들이 "아, 나 이거 몰랐는데!" 하는 재미있는 발견의 시간이 될 수 있도록 가볍고 유머 있게 진행합니다.)*

자, 여기서부터는 잠깐 HTML과 CSS를 내려놓고, 우리가 매일 쓰는 컴퓨터 자체를 얼마나 잘 활용하고 있는지 점검해 보는 시간입니다. 이 특강 시간은 여러분이 앞으로 공부하고, 취업하고, 일하는 모든 환경에서 실질적으로 쓸 수 있는 내용입니다.

여기 제 화면을 한번 보세요. 바탕화면에 파일들이 정말 어지럽게 흩어져 있죠? 이게 여러분 컴퓨터 모습과 혹시 비슷하지 않나요? 웃음이 나오시죠? 이 상태에서 "아, 지난주에 작업했던 그 파일 어디 있지?" 하고 찾으려면 시간이 얼마나 걸릴까요?

### 컴퓨터 활용 팁 1: Search, Don't Sort (정리하지 말고 검색하세요)

많은 분들이 폴더를 만들고, 폴더 안에 또 폴더를 만들고, 그 안에 또 폴더를 만들어 파일을 정리하려고 합니다. "학교 > 2026 > 1학기 > 웹기초 > 7주차 > 실습" 같은 구조가 대표적입니다. 그런데 이렇게 하면 문제가 생깁니다. 다음 주가 되면 "이 파일이 7주차 폴더에 있나, 아니면 8주차에 있나?" 하고 헷갈리거든요. 폴더 구조 복잡해질수록 파일을 찾는 시간은 오히려 늘어납니다.

그 대신, 파일 이름을 잘 짓는 것이 훨씬 강력합니다. 예를 들어 `20261015_Portfolio_John_v1.html`처럼 날짜, 내용, 버전이 파일명에 들어 있으면, 탐색기에서 `Win + F`나 탐색기 검색창에 "Portfolio John"을 치는 것만으로 바로 찾을 수 있습니다. 폴더 구조에 기대지 말고, 검색 기능을 믿으세요. **Search, Don't Sort** — 이 네 단어가 파일 관리의 핵심입니다.

그리고 한 가지 더. 파일 탐색기에서 **파일 확장자 표시** 옵션을 반드시 켜두세요. 기본 설정으로는 `.exe`, `.jpg`, `.pdf` 같은 확장자가 숨겨져 있습니다. 이 상태에서는 "이 파일이 실행 파일인지, 그림 파일인지, 문서 파일인지"를 구분할 수 없어서 악성 파일에 속아 실행하는 사고가 생깁니다. 실제로 바이러스 감염 사례 중 많은 수가 "PDF 같아 보이는 .exe 파일"을 열면서 시작됩니다. 탐색기 > 보기 > 파일 이름 확장명 표시 체크. 지금 당장 켜두세요.

### 컴퓨터 활용 팁 2: Win + V — 클립보드 히스토리

*(Instructor Note: 텍스트를 두 개 이상 복사한 뒤 Win + V를 눌러 클립보드 목록이 뜨는 것을 실시간으로 시연합니다.)*

여러분, 복사(`Ctrl + C`)와 붙여넣기(`Ctrl + V`)는 매일 쓰시죠? 그런데 이런 경험 없으셨나요? 링크를 복사했는데, 그 사이에 다른 걸 복사해서 원래 링크가 사라져 버린 경험. 다시 찾으러 가야 하는 그 귀찮음. 여러 곳에서 정보를 모아 붙여넣어야 하는데 한 번에 한 개씩밖에 못해서 왔다갔다 반복했던 기억.

**Win + V** 를 누르면 복사 기록이 목록으로 나타납니다. 내가 오늘 복사한 텍스트, 링크, 이미지 등을 모두 골라서 붙여넣을 수 있습니다. 처음 쓸 때 "클립보드 기록 켜기"를 활성화해야 하는데, 한 번만 설정하면 됩니다. 이 기능 하나로 여러분의 복사-붙여넣기 효율이 눈에 띄게 올라갑니다. 특히 여러 자료에서 내용을 모아서 정리할 때 아주 편리합니다.

### 컴퓨터 활용 팁 3: Win + Shift + S — 화면 캡처 마스터

*(Instructor Note: 전체화면 캡처와 영역 캡처의 차이를 직접 보여줍니다. 특히 캡처 후 바로 문서나 카카오톡에 Ctrl + V로 붙여넣는 과정을 시연합니다.)*

화면을 캡처할 때 Print Screen 키를 눌러서 전체 화면을 찍고, 그림판에 붙여넣어서 저장하고, 다시 잘라내는 과정을 거치고 계신가요? 이건 정말 비효율적인 방법입니다. 전체 화면을 다 캡처하면 파일 크기도 크고, 필요한 부분만 전달하기 위해 또 편집해야 하죠.

**Win + Shift + S** 를 누르면 화면이 어두워지면서 원하는 영역만 드래그해서 선택할 수 있습니다. 선택이 끝나는 순간, 그 영역이 클립보드에 복사됩니다. 바로 `Ctrl + V`로 카카오톡, 이메일, 워드, 모든 곳에 붙여넣을 수 있습니다. 그림판에 거쳐서 저장할 필요가 없습니다. 오늘 이 수업에서 가장 많이 "아 이걸 몰랐다!" 하실 팁이라고 생각합니다.

실제로 이 기능을 쓰면 화면에 표시된 에러 메시지를 캡처해서 AI나 선생님에게 바로 보낼 수 있습니다. "에러가 났어요" 대신 캡처된 에러 화면을 보내면 훨씬 빠르게 도움을 받을 수 있겠죠? 오늘 과제에서도 패스키 로그인 화면을 캡처할 때 이 방법을 쓰게 될 겁니다.

### 컴퓨터 활용 팁 4: Win + 방향키, Win + Tab — 화면 분할과 가상 데스크톱

*(Instructor Note: 실제로 창을 두 개 띄운 뒤, Win + 왼쪽 화살표로 절반 고정, Win + 오른쪽 화살표로 나머지 절반을 다른 창으로 채우는 것을 시연합니다. 이어서 Win + Tab을 눌러 가상 데스크톱을 추가하는 것도 보여줍니다.)*

노트북 화면 하나에서 StackBlitz와 핸드아웃을 동시에 봐야 할 때, 창 크기를 수동 조절하고 계신가요? 마우스로 창의 가장자리를 잡고 늘렸다 줄였다 하는 그 번거로운 작업을 매번 반복하고 계신 건 아닌가요?

**Win + 방향키** 를 쓰면 현재 활성화된 창이 화면의 절반을 차지하도록 딱 붙어버립니다. Win + 왼쪽 화살표 누르면 왼쪽 절반. Win + 오른쪽 화살표 누르면 오른쪽 절반. 그러면 자동으로 나머지 공간에 다른 창을 선택해서 붙이겠냐고 물어봅니다. 이걸 쓰면 마우스로 창 크기를 조절하는 시간이 완전히 사라집니다.

한발 더 나아가서, **Win + Tab** 을 누르면 **가상 데스크톱(Virtual Desktop)** 기능이 나타납니다. 데스크톱을 새로 만들면, 마치 두 번째 모니터가 생긴 것처럼 완전히 새로운 작업 공간이 생깁니다. 데스크톱 1에는 수업 자료, 데스크톱 2에는 개인 작업물처럼 공간을 분리해서 쓸 수 있습니다. 모니터 한 대로도 여러 대 모니터를 쓰는 것과 비슷한 효과를 낼 수 있습니다. 취업 후 회사에서도 이 기능을 쓰면 업무와 사적인 창을 섞지 않고 깔끔하게 분리할 수 있습니다.

### 컴퓨터 활용 팁 5: Ctrl + Shift + Esc — 작업 관리자와 강제 종료

*(Instructor Note: 일부러 응답 없는 프로그램 상황(또는 여러 탭을 열어 CPU 점유율이 높은 상황)을 만들어서 작업 관리자가 어떻게 보이는지 실시간으로 보여줍니다.)*

컴퓨터를 쓰다 보면 프로그램이 갑자기 멈추거나 "응답 없음"이 뜨는 경험, 다들 해보셨죠? 이럴 때 대부분의 사람들이 전원 버튼을 길게 누르거나, 그냥 기다립니다. 둘 다 좋은 방법이 아닙니다. 전원을 강제로 끄면 저장하지 않은 작업이 날아가고, 심한 경우 운영체제 파일이 손상될 수도 있습니다.

**Ctrl + Shift + Esc** 를 누르면 작업 관리자가 바로 열립니다. 여기서 응답 없는 프로그램을 찾아 클릭하고, "작업 끝내기"를 누르면 그 프로그램만 깔끔하게 종료됩니다. 나머지 프로그램들은 아무런 영향을 받지 않습니다. 작업 관리자는 또한 현재 CPU와 메모리를 얼마나 쓰고 있는지도 볼 수 있어서, "왜 내 컴퓨터가 이렇게 느리지?"를 진단하는 데도 씁니다. 메모리를 많이 잡아먹는 프로그램을 찾아서 닫으면 컴퓨터가 눈에 띄게 빨라지는 경험을 하실 수 있을 거예요.

### 보너스 팁: 압축 파일(Zip)을 제대로 해제하는 법

압축 파일 관련 실수도 많이 합니다. `something.zip` 파일을 받아서 열면, 압축 프로그램이 파일 목록을 보여줍니다. 이 상태에서 안에 있는 프로그램을 그냥 실행하면, 경로가 임시 폴더를 가리키고 있어서 파일을 찾지 못하거나 실행이 안 되는 오류가 납니다. 반드시 **압축 파일 위에서 오른쪽 클릭 > "압축 풀기"** 를 해서 파일을 실제 폴더에 꺼낸 다음 실행해야 합니다. 아주 간단하지만, 이걸 몰라서 "왜 안 되지?" 하고 고생하는 경우가 정말 많습니다. 특히 학교 과제물이나 강의 자료를 내려받았을 때 이 문제가 자주 발생합니다. 파일을 받으면 항상 "먼저 압축 해제부터"를 습관화하세요.

---

*(Instructor Note: 마무리 안내)*

오늘 배운 내용을 정리하면: Flexbox로 레이아웃을 자유자재로 배치하는 법, 개발자 도구로 버그를 진단하고 고치는 법, 그리고 컴퓨터 활용도 5가지 팁입니다. 오늘의 팁들은 지금 당장 오늘 쓸 수 있는 것들입니다. 수업 끝나고 바로 써보세요.

숙제 안내드립니다. 오늘은 보안과 편리함이라는 현대 웹 개발의 중요 트렌드를 반영하여 Passkey 이메일 Microassignment가 있습니다. 과제 0.7 이메일 꼭 기억하시고, Handout을 참고하세요.

다음 주(8주차)에는 지금까지 배운 내용을 바탕으로 중간고사와 대체 평가(타임어택 종합장)가 예정되어 있습니다. 너무 긴장하지 마세요. 지금까지 꾸준히 따라오셨다면 충분히 잘 하실 수 있습니다. 마지막으로 지금까지 7주 동안 열심히 함께해주신 여러분께 진심으로 수고했다고 전하고 싶습니다.

수고하셨습니다. 우리는 다음 주에 또 다른 세상의 비밀을 푸는 코딩 이야기로 다시 만나겠습니다!
*(Instructor Note: 학생들에게 따뜻하게 인사하고 강의를 마무리합니다.)*
