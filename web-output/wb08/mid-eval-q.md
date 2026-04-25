[Question name] Q01-A (wb07) [Medium] - Multiple Choice

## Flexbox Layout Halucination Check ##

[Question type] multiple choice

[Question text]

An AI generated the following CSS to center an item both vertically and horizontally.

<pre style="background-color: #f4f4f4; padding: 15px; border: 1px solid #ccc; border-radius: 4px; white-space: pre-wrap; font-family: 'Courier New', Courier, monospace;"><code>
.container {
  display: flexbox;
  align-content: center;
  justify-items: center;
  width: 100vw;
  height: 100vh;
}
</code></pre>

Test this code in a browser. Which of the following pairs of properties used in the code above contains invalid or hallucinated CSS values for a Flexbox container?

[General feedback]

The correct value for display is `flex`, not `flexbox`. In CSS Flexbox, horizontal alignment is controlled by `justify-content`, not `justify-items` (which belongs to CSS Grid). `align-content` is valid but only applies to multi-line flex containers.

[Choice 1 (정답 100%)]

display: flexbox; AND justify-items: center;

[Choice 2]

align-content: center; AND width: 100vw;

[Choice 3]

display: flexbox; AND height: 100vh;

[Choice 4]

justify-items: center; AND align-content: center;

[Korean]
AI가 항목을 수직 및 수평으로 중앙 정렬하기 위해 다음 CSS를 생성했습니다. (코드 생략) 위 코드에서 사용된 속성 쌍 중 Flexbox 컨테이너에 대해 유효하지 않거나 할루시네이션(환각)된 CSS 값을 포함하고 있는 것은 무엇입니까?

---

[Question name] Q01-B (wb07) [Medium] - Matching

## Flexbox Layout Validity Check ##

[Question type] matching

[Question text]

An AI generated the following CSS to center an item. 

<pre style="background-color: #f4f4f4; padding: 15px; border: 1px solid #ccc; border-radius: 4px; white-space: pre-wrap; font-family: 'Courier New', Courier, monospace;"><code>
.container {
  display: flexbox;
  align-content: center;
  justify-items: center;
  width: 100vw;
}
</code></pre>

Match the CSS declarations from the AI's code with their correct validity status in CSS Flexbox.

[General feedback]

`display: flexbox` is completely invalid. `justify-items` is a valid CSS Grid property but ignored in Flexbox. `align-content` is valid in Flexbox but only applies to multi-line containers. `width: 100vw` is standard and valid.

[Match 1]
display: flexbox;
[Answer 1]
Invalid (Should be 'display: flex;')

[Match 2]
justify-items: center;
[Answer 2]
Invalid (Belongs to CSS Grid, not Flexbox)

[Match 3]
align-content: center;
[Answer 3]
Valid (But only applies to multi-line flex containers)

[Match 4]
width: 100vw;
[Answer 4]
Valid (Standard CSS property)

[Korean]
AI가 항목을 중앙 정렬하기 위해 다음 CSS를 생성했습니다. (코드 생략) AI 코드의 각 CSS 선언을 CSS Flexbox에서의 정확한 유효성 상태와 짝지으세요.

---

[Question name] Q01-C (wb07) [Medium] - Short Answer

## Flexbox Display Property Check ##

[Question type] short answer

[Question text]

An AI generated the following CSS to create a flex container:

<pre style="background-color: #f4f4f4; padding: 15px; border: 1px solid #ccc; border-radius: 4px; white-space: pre-wrap; font-family: 'Courier New', Courier, monospace;"><code>
.container {
  display: flexbox;
  justify-items: center;
}
</code></pre>

The value `flexbox` for the display property is completely invalid and hallucinated. What is the correct, exact value you must assign to the `display` property to establish a flex container? (Type just the single word).

[General feedback]

The correct value is `flex`. Browsers do not recognize `flexbox` as a valid display property value.

[Answer]

정답 1:
flex (100%)

정답 2:
flex; (100%)

[Korean]
AI가 플렉스 컨테이너를 만들기 위해 다음 CSS를 생성했습니다. (코드 생략) display 속성의 `flexbox` 값은 유효하지 않은 환각(Hallucination)입니다. 플렉스 컨테이너를 생성하기 위해 `display` 속성에 할당해야 하는 정확하고 올바른 값은 무엇입니까? (단어 하나만 입력하세요)

---

[Question name] Q01-D (wb07) [Medium] - True / False

## Flexbox Horizontal Alignment ##

[Question type] true/false

[Question text]

An AI generated the following CSS to align items horizontally in a Flexbox container.

<pre style="background-color: #f4f4f4; padding: 15px; border: 1px solid #ccc; border-radius: 4px; white-space: pre-wrap; font-family: 'Courier New', Courier, monospace;"><code>
.container {
  display: flex;
  justify-items: center;
}
</code></pre>

True or False: The property `justify-items: center;` is the correct CSS Flexbox property to align items horizontally along the main axis.

[General feedback]

False. `justify-items` belongs to the CSS Grid specification and has no effect on flex items. To align items along the main axis in Flexbox, you must use `justify-content: center;`.

[Answer]

False

[Korean]
AI가 Flexbox 컨테이너 내의 항목을 수평으로 정렬하기 위해 다음 CSS를 생성했습니다. (코드 생략) 참/거짓: `justify-items: center;`는 플렉스 컨테이너의 메인 축을 따라 수평으로 항목을 정렬하는 올바른 CSS Flexbox 속성입니다.

---




[Question name] Q04 (wb03) [Easy]

## Form Submission Button Default ##

[Question type] multiple choice

[Question text]

You have the following form:

<pre style="background-color: #f4f4f4; padding: 15px; border: 1px solid #ccc; border-radius: 4px; white-space: pre-wrap; font-family: 'Courier New', Courier, monospace;"><code>
&lt;form action=&quot;https://example.com/submit&quot; method=&quot;GET&quot;&gt;
  &lt;input type=&quot;text&quot; name=&quot;username&quot;&gt;
  &lt;button&gt;Send Data&lt;/button&gt;
&lt;/form&gt;
</code></pre>

When a user types "testuser" and clicks the "Send Data" button, what is the exact URL the browser attempts to navigate to?

[General feedback]

Any `<button>` inside a `<form>` defaults to `type="submit"` unless specified otherwise. When a GET method form is submitted, the browser automatically appends the input's name and value to the URL as a query string (e.g., `?username=testuser`).

[Choice 1 (정답 100%)]

https://example.com/submit?username=testuser

[Choice 2]

https://example.com/submit

[Choice 3]

It does not navigate anywhere because the button lacks type="submit"

[Choice 4]

https://example.com/submit/testuser

[Korean]
다음과 같은 폼(form)이 있습니다: (코드 생략) 사용자가 "testuser"를 입력하고 "Send Data" 버튼을 클릭할 때, 브라우저가 이동하려고 시도하는 정확한 URL은 무엇입니까?



---




[Question name] Q05 (wb01) [Easy]

## StackBlitz Console Output ##

[Question type] multiple choice

[Question text]

When you open a new HTML/JS project in StackBlitz, you can view the Console. If you add `<script>console.log('Test');</script>` inside the `<head>` tag, where exactly will this output appear?

[General feedback]

StackBlitz captures console output and displays it in the Developer Tools console of the preview window. Scripts in the `<head>` execute as they are parsed.

[Choice 1 (정답 100%)]

In the browser Developer Tools Console.

[Choice 2]

Directly on the webpage.

[Choice 3]

It will not run because scripts must be at the end of the body.

[Choice 4]

In the StackBlitz terminal tab.

[Korean]
StackBlitz에서 새 HTML/JS 프로젝트를 열면 Console(콘솔)을 볼 수 있습니다. `<head>` 태그 안에 `<script>console.log('Test');</script>`를 추가하면, 이 출력 결과는 정확히 어디에 나타납니까?



---




[Question name] Q06 (wb01) [Medium]

## Engineer Questioning Method ##

[Question type] multiple choice

[Question text]

According to the Engineer Questioning method taught in Week 1, which of the following is an essential component when asking for help with an error?

[General feedback]

The 4 elements are: Current State (Symptom), Expected State (Goal), What you tried, and Exact Error. Including what you tried is crucial so others do not suggest things you have already done.

[Choice 1 (정답 100%)]

What you tried to fix it.

[Choice 2]

Your emotional state.

[Choice 3]

The exact line number of every file.

[Choice 4]

A screenshot of your entire desktop.

[Korean]
1주차에 배운 '엔지니어식 질문법(Engineer Questioning method)'에 따르면, 오류에 대해 도움을 요청할 때 다음 중 필수적으로 포함되어야 하는 요소는 무엇입니까?



---




[Question name] Q07 (wb01) [Easy]

## Business Email Structure ##

[Question type] multiple choice

[Question text]

When writing a business email to a professor, where is the most appropriate place to state the main purpose of your email?

[General feedback]

Business communication favors the BLUF (Bottom Line Up Front) approach, stating the main point or request immediately to respect the reader's time.

[Choice 1 (정답 100%)]

In the very first sentence of the body (BLUF - Bottom Line Up Front).

[Choice 2]

At the end, after a long explanation of the background.

[Choice 3]

In the postscript (P.S.).

[Choice 4]

In an attached Word document.

[Korean]
교수님께 비즈니스 이메일을 작성할 때, 이메일의 핵심 목적을 밝히기에 가장 적절한 위치는 어디입니까?



---




[Question name] Q08 (wb01) [Medium]

## GitHub Commit Verification ##

[Question type] multiple choice

[Question text]

You committed and pushed a file named `index.html` to your GitHub repository. How can you verify that the exact code you wrote was successfully uploaded?

[General feedback]

The definitive way to check a successful push is to navigate to the repository URL on GitHub.com and visually inspect the file contents there.

[Choice 1 (정답 100%)]

By clicking on the file name in the GitHub web interface and reading the code.

[Choice 2]

By checking if the StackBlitz preview updates.

[Choice 3]

By looking at your local file manager.

[Choice 4]

By refreshing your browser.

[Korean]
`index.html`이라는 파일을 GitHub 저장소에 커밋하고 푸시(push)했습니다. 작성한 코드가 성공적으로 업로드되었는지 어떻게 확인할 수 있습니까?



---




[Question name] Q10 (wb02) [Medium]

## Image Alt Attribute ##

[Question type] multiple choice

[Question text]

What is the primary technical purpose of the `alt` attribute in an `<img>` tag?

[General feedback]

The `alt` attribute specifies alternative text that is displayed if the image cannot be loaded and is read by screen readers for accessibility.

[Choice 1 (정답 100%)]

To provide alternative text if the image fails to load or for screen readers.

[Choice 2]

To define a tooltip when the user hovers over the image.

[Choice 3]

To specify a secondary image URL.

[Choice 4]

To center the image.

[Korean]
`<img>` 태그에서 `alt` 속성의 주요 기술적 목적은 무엇입니까?



---




[Question name] Q11 (wb02) [Hard]

## HTML Nested Lists ##

[Question type] multiple choice

[Question text]

You want to create a bulleted list where the second item has its own sub-list. Which HTML structure is valid?

[General feedback]

A nested list must be placed *inside* an `<li>` element. Placing a `<ul>` directly as a child of another `<ul>` (outside an `<li>`) is invalid HTML.

[Choice 1 (정답 100%)]

<ul><li>Item 1</li><li>Item 2 <ul><li>Sub</li></ul></li></ul>

[Choice 2]

<ul><li>Item 1</li><ul><li>Item 2</li></ul></ul>

[Choice 3]

<ul><li>Item 1</li><li>Item 2</li><ul><li>Sub</li></ul></ul>

[Choice 4]

<ul><li>Item 1</li><li>Item 2</li><li><ul><li>Sub</li></ul></li></ul>

[Korean]
두 번째 항목이 자체 하위 목록(sub-list)을 가지는 글머리 기호 목록(bulleted list)을 만들고 싶습니다. 어떤 HTML 구조가 유효합니까?



---




[Question name] Q13 (wb03) [Medium]

## Form Input Labeling ##

[Question type] multiple choice

[Question text]

To correctly associate a `<label>` with an `<input>` for accessibility, which attributes must match?

[General feedback]

A label is linked to an input by setting the label's `for` attribute to the exact value of the input's `id` attribute.

[Choice 1 (정답 100%)]

The `for` attribute of the label and the `id` attribute of the input.

[Choice 2]

The `name` attribute of the label and the `name` attribute of the input.

[Choice 3]

The `id` attribute of the label and the `class` attribute of the input.

[Choice 4]

The `for` attribute of the label and the `class` attribute of the input.

[Korean]
접근성을 위해 `<label>`과 `<input>`을 올바르게 연결하려면 어떤 속성들이 일치해야 합니까?



---




[Question name] Q14 (wb03) [Easy]

## Form Required Validation ##

[Question type] multiple choice

[Question text]

How do you prevent a form from being submitted if a specific text input is left empty by the user?

[General feedback]

The `required` attribute is a standard HTML5 feature that prevents form submission if the input is empty.

[Choice 1 (정답 100%)]

Add the `required` boolean attribute to the `<input>` tag.

[Choice 2]

Set `validate="true"` on the form.

[Choice 3]

Use CSS `content: required;`.

[Choice 4]

Change the button type to `required-submit`.

[Korean]
사용자가 특정 텍스트 입력을 비워둔 경우 폼(form)이 제출되지 않도록 하려면 어떻게 해야 합니까?



---




[Question name] Q15 (wb03) [Easy]

## Checkbox Default State ##

[Question type] multiple choice

[Question text]

Which attribute should you add to an `<input type="checkbox">` to make it selected by default when the page loads?

[General feedback]

The `checked` boolean attribute makes a checkbox or radio button selected by default.

[Choice 1 (정답 100%)]

checked

[Choice 2]

selected

[Choice 3]

default

[Choice 4]

value="true"

[Korean]
페이지가 로드될 때 기본적으로 선택된 상태로 만들려면 `<input type="checkbox">`에 어떤 속성을 추가해야 합니까?



---




[Question name] Q19 (wb05) [Medium]

## CSS Hex Color Code ##

[Question type] multiple choice

[Question text]

In the CSS color code `#FF0000`, what color does this represent?

[General feedback]

Hex codes are structured as #RRGGBB. FF is the maximum value for Red, and 00 is zero for Green and Blue, resulting in pure red.

[Choice 1 (정답 100%)]

Red

[Choice 2]

Green

[Choice 3]

Blue

[Choice 4]

White

[Korean]
CSS 색상 코드 `#FF0000`은 무슨 색을 나타냅니까?



---




[Question name] Q20 (wb05) [Easy]

## CSS External File Link ##

[Question type] multiple choice

[Question text]

Which HTML tag is used to link an external CSS file named `style.css` to an HTML document?

[General feedback]

The `<link>` tag with `rel="stylesheet"` and the `href` attribute is the standard way to connect external CSS.

[Choice 1 (정답 100%)]

<link rel="stylesheet" href="style.css">

[Choice 2]

<style src="style.css"></style>

[Choice 3]

<css href="style.css"></css>

[Choice 4]

<script src="style.css"></script>

[Korean]
`style.css`라는 이름의 외부 CSS 파일을 HTML 문서에 연결하는 데 사용되는 HTML 태그는 무엇입니까?



---




[Question name] Q21 (wb06) [Easy]

## DevTools Element Selection ##

[Question type] multiple choice

[Question text]

In Chrome DevTools, what is the shortcut or method to quickly select an element on the page for inspection?

[General feedback]

Right-clicking and selecting 'Inspect' (or using the inspect tool icon) directly highlights the element in the Elements panel.

[Choice 1 (정답 100%)]

Right-click the element on the page and select 'Inspect'.

[Choice 2]

Press F5.

[Choice 3]

View Page Source.

[Choice 4]

You must manually search through the HTML tree.

[Korean]
Chrome DevTools에서 페이지의 요소를 검사하기 위해 빠르게 선택하는 단축키나 방법은 무엇입니까?



---




[Question name] Q23 (wb06) [Medium]

## Box-Sizing Property ##

[Question type] multiple choice

[Question text]

What happens when you apply `box-sizing: border-box;` to an element?

[General feedback]

`box-sizing: border-box` forces the specified width to include the content, padding, and border, making layout calculations much easier.

[Choice 1 (정답 100%)]

Padding and border are included within the element's specified width and height.

[Choice 2]

The element loses its margin.

[Choice 3]

The element behaves like an inline element.

[Choice 4]

Padding expands the total width beyond the specified width.

[Korean]
요소에 `box-sizing: border-box;`를 적용하면 어떻게 됩니까?



---




[Question name] Q25 (wb07) [Medium]

## Flexbox Cross Axis Alignment ##

[Question type] multiple choice

[Question text]

If a flex container has `flex-direction: row;`, which property aligns the items vertically?

[General feedback]

With `row` direction, the main axis is horizontal. The cross axis is vertical. `align-items` controls alignment along the cross axis.

[Choice 1 (정답 100%)]

align-items

[Choice 2]

justify-content

[Choice 3]

vertical-align

[Choice 4]

align-content

[Korean]
플렉스 컨테이너(flex container)가 `flex-direction: row;`를 가질 때, 항목들을 수직으로 정렬하는 속성은 무엇입니까?



---




[Question name] Q26 (wb07) [Easy]

## Flexbox Wrap ##

[Question type] multiple choice

[Question text]

When you have too many items in a flex container, they might shrink to fit on one line. What property prevents shrinking and allows them to flow to the next line?

[General feedback]

`flex-wrap: wrap` tells the container to wrap items onto multiple lines if they exceed the container's width.

[Choice 1 (정답 100%)]

flex-wrap: wrap;

[Choice 2]

flex-flow: row;

[Choice 3]

overflow: visible;

[Choice 4]

display: block;

[Korean]
플렉스 컨테이너에 항목이 너무 많을 때, 한 줄에 맞추기 위해 축소될 수 있습니다. 항목이 축소되는 것을 방지하고 다음 줄로 넘어가게 하는 속성은 무엇입니까?



---




[Question name] Q27 (wb07) [Medium]

## Flex Item Property ##

[Question type] multiple choice

[Question text]

Which of the following properties is applied to a flex ITEM (the child), rather than the flex CONTAINER (the parent)?

[General feedback]

`flex-grow`, `flex-shrink`, and `flex-basis` are applied directly to the child items to control how they distribute space. The others are container properties.

[Choice 1 (정답 100%)]

flex-grow

[Choice 2]

justify-content

[Choice 3]

align-items

[Choice 4]

flex-direction

[Korean]
다음 중 플렉스 컨테이너(부모)가 아닌 플렉스 항목(자식 아이템)에 적용되는 속성은 무엇입니까?



---




[Question name] Q28 (wb07) [Medium]

## Flexbox Space Between ##

[Question type] multiple choice

[Question text]

What does `justify-content: space-between;` do?

[General feedback]

`space-between` maximizes the distance between the outermost items, pushing them to the edges of the container.

[Choice 1 (정답 100%)]

Pushes the first item to the start, the last item to the end, and evenly distributes space between the rest.

[Choice 2]

Centers all items with equal space around them.

[Choice 3]

Adds equal space before the first item and after the last item.

[Choice 4]

Removes all margins from the items.

[Korean]
`justify-content: space-between;`은 어떤 역할을 합니까?



---




[Question name] Q29 (wb07) [Easy]

## Flexbox Gap ##

[Question type] multiple choice

[Question text]

What is the modern CSS property specifically designed to add spacing between flex items without using margins?

[General feedback]

The `gap` property (formerly `grid-gap`) works in Flexbox to add exact spacing between items without affecting outer margins.

[Choice 1 (정답 100%)]

gap

[Choice 2]

spacing

[Choice 3]

margin-between

[Choice 4]

flex-space

[Korean]
마진(margin)을 사용하지 않고 플렉스 항목 간에 간격을 추가하기 위해 특별히 설계된 최신 CSS 속성은 무엇입니까?



---
\n
[Question name] Q30 (wb02) [Easy]

## Image Tag Characteristics ##

[Question type] multiple choice

[Question text]

In HTML, the `<img>` tag is unique compared to tags like `<h1>` or `<p>`. Which of the following statements correctly describes the `<img>` tag?

[General feedback]

The `<img>` tag is an "empty tag" (or "self-closing tag") and does not require a closing tag.

[Choice 1 (정답 100%)]

It is an empty tag and does not require a closing tag.

[Choice 2]

It must always be closed with `</img>`.

[Choice 3]

It can only be used inside the `<head>` section.

[Choice 4]

It automatically adds a border around the image.

[Korean]
HTML에서 `<img>` 태그는 `<h1>`이나 `<p>`와 같은 태그와 비교할 때 독특한 특징을 가집니다. 다음 중 `<img>` 태그를 올바르게 설명한 것은 무엇입니까?

[Question name] Q30 (wb07) [Medium]

## Flexbox Layout Matching ##

[Question type] matching

[Question text]

Match the given `justify-content` values with their resulting layout descriptions for items inside a Flexbox container (assuming `flex-direction: row`).

[General feedback]

- `center`: Packs items around the center.
- `space-between`: Distributes items evenly, first item at start, last at end.
- `flex-end`: Packs items toward the end line.

[Match 1]
center
[Answer 1]
항목들이 컨테이너의 중앙에 모입니다. (Items packed at the center)

[Match 2]
space-between
[Answer 2]
첫 번째 항목은 시작점에, 마지막 항목은 끝점에 배치되고 나머지는 고르게 분포됩니다. (Evenly distributed, first at start, last at end)

[Match 3]
flex-end
[Answer 3]
항목들이 컨테이너의 끝점(오른쪽)에 모입니다. (Items packed at the end)

[Korean]
다음 `justify-content` 속성 값들을 Flexbox 컨테이너 내의 결과 레이아웃 설명과 올바르게 짝지으세요.

---

[Question name] Q31 (wb02) [Easy]

## HTML Skeleton Body ##

[Question type] multiple choice

[Question text]

When structuring an HTML document, where should you place the content (like headings, paragraphs, and images) that you actually want to be visible on the browser screen?

[General feedback]

The `<body>` tag holds the visible content of the web page, while the `<head>` contains metadata that operates behind the scenes.

[Choice 1 (정답 100%)]

Inside the `<body>` tag.

[Choice 2]

Inside the `<head>` tag.

[Choice 3]

Inside the `<html>` tag, but outside the `<body>` tag.

[Choice 4]

Directly at the very top of the document before any tags.

[Korean]
HTML 문서를 구조화할 때, 브라우저 화면에 실제로 표시되기를 원하는 내용(제목, 문단, 이미지 등)은 어디에 배치해야 합니까?

---

[Question name] Q32 (wb02) [Medium]

## HTML Head Tag Purpose ##

[Question type] multiple choice

[Question text]

What is the primary purpose of the `<head>` tag in an HTML document?

[General feedback]

The `<head>` tag contains metadata, the page title, and links to stylesheets, but its contents are not directly displayed on the main white canvas of the web page.

[Choice 1 (정답 100%)]

To hold metadata, settings, and links to stylesheets that are not directly displayed on the page canvas.

[Choice 2]

To display the largest and most important heading at the top of the webpage.

[Choice 3]

To hold all the images and multimedia files.

[Choice 4]

To visually separate the top section of the webpage from the bottom section.

[Korean]
HTML 문서에서 `<head>` 태그의 주요 목적은 무엇입니까?

---

[Question name] Q33 (wb03) [Easy]

## Form Label Element ##

[Question type] multiple choice

[Question text]

When creating a form input (like a text box for an email), which tag is used to attach a descriptive text "name tag" next to it to improve usability and accessibility?

[General feedback]

The `<label>` tag is specifically used to bind a text label to a specific input field, helping users know exactly what to type.

[Choice 1 (정답 100%)]

<label>

[Choice 2]

<span>

[Choice 3]

<description>

[Choice 4]

<name>

[Korean]
폼(form) 입력을 만들 때(예: 이메일을 입력하는 텍스트 상자), 사용성 및 접근성을 높이기 위해 입력 필드 옆에 설명 텍스트("이름표")를 붙일 때 사용하는 태그는 무엇입니까?

---

[Question name] Q34 (wb05) [Easy]

## CSS Inheritance Concept ##

[Question type] multiple choice

[Question text]

In CSS, what is the meaning of "Inheritance"?

[General feedback]

Inheritance is the phenomenon where child tags naturally inherit the design (like font or color) given to a parent tag.

[Choice 1 (정답 100%)]

Child tags naturally receive the styling (like fonts or colors) applied to their parent tag.

[Choice 2]

Images automatically copy the size of the previous image.

[Choice 3]

HTML tags inherit the styles from a completely different website.

[Choice 4]

Styles are automatically passed from the bottom of the page to the top.

[Korean]
CSS에서 "상속(Inheritance)"의 의미는 무엇입니까?

---

[Question name] Q35 (wb05) [Medium]

## CSS Class vs ID ##

[Question type] multiple choice

[Question text]

When applying CSS styles, when should you use an ID (`#`) instead of a Class (`.`)?

[General feedback]

An ID (`#`) is a unique identifier used for a specific, single element, while a Class (`.`) is a group designation used for multiple elements.

[Choice 1 (정답 100%)]

When you want to uniquely identify and style one specific, single element on the page.

[Choice 2]

When you want to apply the exact same uniform to hundreds of elements.

[Choice 3]

When you want to change the background color of the entire body.

[Choice 4]

When you want to write an HTML comment.

[Korean]
CSS 스타일을 적용할 때, 언제 클래스(`.`) 대신 아이디(`#`)를 사용해야 합니까?

---

[Question name] Q36 (wb06) [Easy]

## Box Model Margin ##

[Question type] multiple choice

[Question text]

In the CSS Box Model, which property is used to create "social distancing" (space outside the border) between two separate boxes?

[General feedback]

Margin creates space outside the border of an element, effectively pushing other nearby elements away.

[Choice 1 (정답 100%)]

Margin

[Choice 2]

Padding

[Choice 3]

Border

[Choice 4]

Content

[Korean]
CSS 박스 모델(Box Model)에서 두 개의 독립된 박스 사이에 "사회적 거리두기(social distancing)" (즉, 테두리 바깥쪽의 공간)를 만들기 위해 사용되는 속성은 무엇입니까?

---

[Question name] Q37 (wb06) [Medium]

## Box Model Padding ##

[Question type] multiple choice

[Question text]

In the CSS Box Model, what is the role of Padding?

[General feedback]

Padding acts like "bubble wrap" that protects the content. It adds space inside the box, between the content and the border.

[Choice 1 (정답 100%)]

It adds space inside the box, between the content and the border.

[Choice 2]

It pushes other boxes away from the current box.

[Choice 3]

It defines the physical line that surrounds the box.

[Choice 4]

It determines the color of the text inside the box.

[Korean]
CSS 박스 모델(Box Model)에서 패딩(Padding)의 역할은 무엇입니까?

---

[Question name] Q38 (wb06) [Easy]

## CSS Box Sizing ##

[Question type] multiple choice

[Question text]

Which CSS property declaration should be added to ensure that padding and border are included within an element's specified width, preventing layout breakage?

[General feedback]

`box-sizing: border-box;` forces the width and height properties to include the content, padding, and border, making layouts much more predictable.

[Choice 1 (정답 100%)]

box-sizing: border-box;

[Choice 2]

margin-box: include;

[Choice 3]

display: block;

[Choice 4]

overflow: hidden;

[Korean]
패딩(padding)과 테두리(border)가 요소에 지정된 너비 안에 포함되게 하여 레이아웃이 깨지는 것을 방지하려면 어떤 CSS 속성 선언을 추가해야 합니까?

---

[Question name] Q39 (wb07) [Medium]

## Flexbox Overflow Handling ##

[Question type] multiple choice

[Question text]

When using Flexbox, what might happen if a child element has a fixed width (like `width: 1000px;`) but the parent container is smaller and tries to flex?

[General feedback]

If a child element is too rigid and large for a flexing parent container, it will break out of the container, causing an Overflow.

[Choice 1 (정답 100%)]

The child element will break out of the container, causing an Overflow.

[Choice 2]

The child element will magically disappear from the screen.

[Choice 3]

The parent container will automatically change into a Grid layout.

[Choice 4]

The child element's text will change color to red to indicate an error.

[Korean]
Flexbox를 사용할 때, 자식 요소가 고정된 너비(예: `width: 1000px;`)를 가지고 있지만 부모 컨테이너가 더 작아서 유연하게 줄어들려고 할 때 어떤 일이 발생할 수 있습니까?

---
\n
[Question name] Q40 (wb01) [Easy]

## Internet vs Web ##

[Question type] multiple choice

[Question text]

According to the Week 1 lecture, what is the primary difference between the "Internet" and the "Web"?

[General feedback]

The Internet is the global physical infrastructure of connected computers (the highway), while the Web (World Wide Web) is just one of the many services that run on top of it.

[Choice 1 (정답 100%)]

The Internet is the physical network infrastructure, and the Web is a service that runs on top of it.

[Choice 2]

They are exactly the same thing.

[Choice 3]

The Web is the physical hardware, and the Internet is a software application.

[Choice 4]

The Internet is only for emails, while the Web is for videos.

[Korean]
1주차 강의에 따르면, "인터넷(Internet)"과 "웹(Web)"의 가장 핵심적인 차이는 무엇입니까?

---

[Question name] Q41 (wb05) [Medium]

## Incognito Mode Purpose ##

[Question type] multiple choice

[Question text]

When using a public computer (like in a library or cafe), why is it strongly recommended to use Chrome's "Incognito Mode" (시크릿 모드)?

[General feedback]

Incognito Mode ensures that your browsing history, cookies, and login sessions are automatically deleted when the window is closed, protecting you from hacking on public PCs.

[Choice 1 (정답 100%)]

To ensure that your login history, passwords, and cookies are automatically deleted when the window closes, preventing hacking.

[Choice 2]

To make your internet connection speed twice as fast.

[Choice 3]

To hide your IP address from the government.

[Choice 4]

To automatically translate foreign websites into Korean.

[Korean]
공용 컴퓨터(도서관이나 카페 등)를 사용할 때 크롬의 "시크릿 모드(Incognito Mode)"를 사용하는 것이 강력히 권장되는 이유는 무엇입니까?

---

[Question name] Q42 (wb05) [Easy]

## Incognito Mode Shortcut ##

[Question type] multiple choice

[Question text]

What is the Windows keyboard shortcut to instantly open a new Incognito window in Google Chrome?

[General feedback]

The shortcut for a new Incognito window is Ctrl+Shift+N (Cmd+Shift+N on Mac).

[Choice 1 (정답 100%)]

Ctrl + Shift + N

[Choice 2]

Ctrl + C

[Choice 3]

Alt + F4

[Choice 4]

Ctrl + T

[Korean]
구글 크롬에서 새로운 시크릿 창(Incognito window)을 즉시 열기 위한 윈도우(Windows) 키보드 단축키는 무엇입니까?

---

[Question name] Q43 (wb06) [Medium]

## Paste Values Only Shortcut ##

[Question type] multiple choice

[Question text]

When copying text from a web page and pasting it into a document, what keyboard shortcut should you use to paste ONLY the raw text without bringing along the messy background colors, fonts, and HTML formatting?

[General feedback]

Ctrl+Shift+V pastes only the raw text values without the original styling.

[Choice 1 (정답 100%)]

Ctrl + Shift + V

[Choice 2]

Ctrl + V

[Choice 3]

Ctrl + C

[Choice 4]

Ctrl + Z

[Korean]
웹 페이지에서 텍스트를 복사하여 문서에 붙여넣을 때, 지저분한 배경색, 폰트, HTML 서식 등을 빼고 오직 순수한 '원시 텍스트(raw text)'만을 붙여넣으려면 어떤 키보드 단축키를 사용해야 합니까?

---

[Question name] Q44 (wb06) [Easy]

## Google Search: Exact Match ##

[Question type] multiple choice

[Question text]

Which Google Search operator should you use if you want to find pages that contain an exact phrase, strictly in that specific order without any missing words?

[General feedback]

Wrapping your search phrase in quotation marks ("") forces Google to find the exact phrase.

[Choice 1 (정답 100%)]

Quotation marks (e.g., "exact phrase")

[Choice 2]

Minus sign (e.g., -exact phrase)

[Choice 3]

Asterisk (e.g., *exact phrase)

[Choice 4]

Hashtag (e.g., #exact phrase)

[Korean]
단어 하나도 빠짐없이, 지정한 순서 그대로 '정확하게 일치하는 문구'가 포함된 페이지를 찾으려면 어떤 구글 검색 연산자를 사용해야 합니까?

---

[Question name] Q45 (wb06) [Easy]

## Google Search: Exclude Word ##

[Question type] multiple choice

[Question text]

You want to search for "Apple" the fruit, but your results are flooded with Apple computers and iPhones. Which Google Search operator will remove results containing the word "iPhone"?

[General feedback]

The minus sign (-) placed directly before a word tells Google to exclude results containing that word.

[Choice 1 (정답 100%)]

Apple -iPhone

[Choice 2]

Apple "iPhone"

[Choice 3]

Apple +iPhone

[Choice 4]

Apple exclude:iPhone

[Korean]
과일 "Apple"을 검색하고 싶은데, 애플 컴퓨터와 아이폰 결과가 너무 많이 나옵니다. 검색 결과에서 "iPhone"이라는 단어를 포함하는 문서를 제외하려면 어떤 구글 검색 연산자를 사용해야 합니까?

---

[Question name] Q46 (wb06) [Easy]

## Google Search: Filetype ##

[Question type] multiple choice

[Question text]

When researching for a university paper, you want to easily find official PDF reports about "Web Design Trends". What is the fastest search query to achieve this?

[General feedback]

The `filetype:pdf` operator restricts search results to only PDF files.

[Choice 1 (정답 100%)]

Web Design Trends filetype:pdf

[Choice 2]

Web Design Trends "pdf"

[Choice 3]

Web Design Trends -pdf

[Choice 4]

Web Design Trends doc:pdf

[Korean]
대학 리포트 조사를 할 때, "Web Design Trends"와 관련된 공식적인 PDF 문서만 빠르게 찾고 싶습니다. 이를 위한 가장 빠른 검색어 조합은 무엇입니까?

---

[Question name] Q47 (wb06) [Medium]

## Google Search: Site Specific ##

[Question type] multiple choice

[Question text]

How can you use Google to search for the keyword "Scholarship" ONLY within the official Seoul Theological University website (stu.ac.kr)?

[General feedback]

The `site:` operator restricts search results to a specific domain.

[Choice 1 (정답 100%)]

Scholarship site:stu.ac.kr

[Choice 2]

Scholarship link:stu.ac.kr

[Choice 3]

Scholarship in:stu.ac.kr

[Choice 4]

Scholarship "stu.ac.kr"

[Korean]
오직 서울신학대학교 공식 웹사이트(stu.ac.kr) 내에서만 "장학금(Scholarship)"이라는 키워드를 검색하려면 구글을 어떻게 활용해야 합니까?

---

[Question name] Q48 (wb06) [Medium]

## Spreadsheet Pivot Table ##

[Question type] multiple choice

[Question text]

In Google Sheets or Excel, what feature allows you to instantly summarize thousands of rows of data (like grouping passengers by class to find their average age) without writing complex formulas?

[General feedback]

A Pivot Table is a powerful data summarization tool that can automatically group, count, average, or calculate the median of large datasets.

[Choice 1 (정답 100%)]

Pivot table

[Choice 2]

Conditional formatting

[Choice 3]

VLOOKUP

[Choice 4]

Find and Replace

[Korean]
구글 스프레드시트나 엑셀에서 복잡한 수식을 직접 작성하지 않고도 수천 줄의 데이터를 즉시 요약(예: 탑승객을 클래스별로 그룹화하여 평균 연령 계산)할 수 있게 해주는 기능은 무엇입니까?

---

[Question name] Q49 (wb05) [Medium]

## Browser Language Settings ##

[Question type] multiple choice

[Question text]

When navigating foreign technical sites like StackOverflow, what built-in Chrome feature can dramatically reduce the language barrier by using AI to instantly translate the entire page?

[General feedback]

Chrome's Auto-translate setting uses AI to instantly translate foreign websites into your native language.

[Choice 1 (정답 100%)]

The Auto-translate setting (Settings > Languages)

[Choice 2]

Incognito Mode

[Choice 3]

Developer Tools (F12)

[Choice 4]

The Network Tab

[Korean]
StackOverflow와 같은 외국의 기술 사이트를 탐색할 때, AI를 사용하여 전체 페이지를 즉시 번역함으로써 언어 장벽을 획기적으로 줄여주는 크롬(Chrome)의 내장 기능은 무엇입니까?
## StackBlitz Local Image Path ##

[Question type] true/false

[Question text]

When building an HTML project on StackBlitz, if you use a local file path for an image like `<img src="C:/Users/student/images/logo.png">`, anyone visiting your StackBlitz URL will be able to see that image.

[General feedback]

False. A local path points to a file on your specific physical computer drive (like C:). When other people visit the StackBlitz URL, their browser will look for `C:/...` on their own computers, not yours, and the image will fail to load. Images must be hosted online or uploaded to the project.

[Answer]

False

[Korean]
참/거짓: StackBlitz에서 HTML 프로젝트를 만들 때, `<img src="C:/Users/student/images/logo.png">`처럼 이미지에 로컬 파일 경로를 사용하면, 다른 사람이 당신의 StackBlitz URL을 방문했을 때도 그 이미지를 볼 수 있습니다.

---
