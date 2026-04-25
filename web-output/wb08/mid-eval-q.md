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
