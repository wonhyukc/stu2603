import json
import os

questions = [
    {
        "name": "StackBlitz HTML Rendering (wb02) [Medium]",
        "text": "Run the following exact code in a StackBlitz HTML project. Do not modify the code.\n\n```html\n<!DOCTYPE html>\n<html>\n<body>\n  <a href=\"https://google.com\">\n    <div style=\"width: 100px; height: 100px; background-color: blue;\">\n      <a href=\"https://apple.com\">Click Here</a>\n    </div>\n  </a>\n</body>\n</html>\n```\nWhen you open this in the StackBlitz preview and click exactly on the blue square area (but NOT on the \"Click Here\" text), which website does the browser navigate to?",
        "type": "MCQ",
        "choices": [
            "It navigates to google.com",
            "It navigates to apple.com",
            "It does not navigate anywhere (click is ignored)",
            "It throws a console error"
        ],
        "answer": 1,
        "feedback": "In HTML5, placing a block-level `<div>` inside an inline `<a>` tag is valid. Clicking anywhere on the blue `<div>` triggers the outer `<a>` tag, navigating to google.com. AI often hallucinates that nested `<a>` tags break the layout entirely, but the browser correctly maps the click area of the outer anchor to the block element."
    },
    {
        "name": "CSS Specificity & Chrome DevTools (wb05, wb06) [Hard]",
        "text": "Copy the following code into a StackBlitz `index.html` file. \n\n```html\n<style>\n  div p { color: blue; }\n  .box p { color: green; }\n  #main p { color: red; }\n</style>\n<div id=\"main\" class=\"box\" style=\"color: purple;\">\n  <p>Hello World</p>\n</div>\n```\nOpen Chrome DevTools and inspect the `<p>` element. According to the \"Computed\" tab in DevTools, what is the exact applied color of the text \"Hello World\"?",
        "type": "MCQ",
        "choices": [
            "red",
            "purple",
            "green",
            "blue"
        ],
        "answer": 1,
        "feedback": "The `color: purple;` inline style is applied to the parent `<div>`, not the `<p>`. The `<p>` tag inherits color, but explicit CSS rules targeting `<p>` override inheritance. The ID selector (`#main p`) has the highest specificity (1,0,1), overriding the class selector (`.box p`) and element selector (`div p`). Therefore, the color is red."
    },
    {
        "name": "Flexbox Layout Halucination Check (wb07) [Medium]",
        "text": "An AI generated the following CSS to center an item both vertically and horizontally.\n\n```css\n.container {\n  display: flexbox;\n  align-content: center;\n  justify-items: center;\n  width: 100vw;\n  height: 100vh;\n}\n```\nTest this code in a browser. Which of the properties used in the code above are completely invalid or hallucinated CSS values that browsers will ignore? Type the exact invalid values separated by a comma (e.g., value1, value2).",
        "type": "CLOZE",
        "answer": "{1:SHORTANSWER:*flexbox, justify-items: center*~*flexbox, justify-items*~*display: flexbox, justify-items: center*}",
        "feedback": "The correct value for display is `flex`, not `flexbox`. In CSS Flexbox, horizontal alignment is controlled by `justify-content`, not `justify-items` (which belongs to CSS Grid). `align-content` is valid but only applies to multi-line flex containers, whereas `align-items` is needed for a single line."
    },
    {
        "name": "Box Model Padding Calculation (wb06) [Hard]",
        "text": "Test the following element in your browser or StackBlitz.\n\n```html\n<div style=\"width: 200px; padding: 10%; border: 5px solid black; margin: 20px;\">\n  Box\n</div>\n```\nAssuming the parent element (`<body>`) has a width of 800px. What is the total rendered pixel width of this `<div>` element as shown in the Chrome DevTools box model diagram? Type only the number (e.g., 500).",
        "type": "CLOZE",
        "answer": "{1:SHORTANSWER:*370*}",
        "feedback": "In CSS, percentage-based padding is calculated based on the width of the **parent** element. 10% of the 800px body width is 80px. Therefore, left padding is 80px and right padding is 80px. The total width = 200px (content) + 80px (left padding) + 80px (right padding) + 5px (left border) + 5px (right border) = 370px."
    },
    {
        "name": "Form Submission Button Default (wb03) [Easy]",
        "text": "You have the following form:\n\n```html\n<form action=\"https://example.com/submit\" method=\"GET\">\n  <input type=\"text\" name=\"username\">\n  <button>Send Data</button>\n</form>\n```\nWhen a user types \"testuser\" and clicks the \"Send Data\" button, what is the exact URL the browser attempts to navigate to?",
        "type": "MCQ",
        "choices": [
            "https://example.com/submit?username=testuser",
            "https://example.com/submit",
            "It does not navigate anywhere because the button lacks type=\"submit\"",
            "https://example.com/submit/testuser"
        ],
        "answer": 1,
        "feedback": "Any `<button>` inside a `<form>` defaults to `type=\"submit\"` unless specified otherwise. When a GET method form is submitted, the browser automatically appends the input's name and value to the URL as a query string (e.g., `?username=testuser`)."
    }
]

# Generate additional questions to reach 30
additional = [
    # wb01 (Web Intro, Environment)
    {
        "name": "StackBlitz Console Output (wb01) [Easy]",
        "text": "When you open a new HTML/JS project in StackBlitz, you can view the Console. If you add `<script>console.log('Test');</script>` inside the `<head>` tag, where exactly will this output appear?",
        "type": "MCQ",
        "choices": [
            "In the browser Developer Tools Console.",
            "Directly on the webpage.",
            "It will not run because scripts must be at the end of the body.",
            "In the StackBlitz terminal tab."
        ],
        "answer": 1,
        "feedback": "StackBlitz captures console output and displays it in the Developer Tools console of the preview window. Scripts in the `<head>` execute as they are parsed."
    },
    {
        "name": "Engineer Questioning Method (wb01) [Medium]",
        "text": "According to the Engineer Questioning method taught in Week 1, which of the following is an essential component when asking for help with an error?",
        "type": "MCQ",
        "choices": [
            "What you tried to fix it.",
            "Your emotional state.",
            "The exact line number of every file.",
            "A screenshot of your entire desktop."
        ],
        "answer": 1,
        "feedback": "The 4 elements are: Current State (Symptom), Expected State (Goal), What you tried, and Exact Error. Including what you tried is crucial so others do not suggest things you have already done."
    },
    {
        "name": "Business Email Structure (wb01) [Easy]",
        "text": "When writing a business email to a professor, where is the most appropriate place to state the main purpose of your email?",
        "type": "MCQ",
        "choices": [
            "In the very first sentence of the body (BLUF - Bottom Line Up Front).",
            "At the end, after a long explanation of the background.",
            "In the postscript (P.S.).",
            "In an attached Word document."
        ],
        "answer": 1,
        "feedback": "Business communication favors the BLUF (Bottom Line Up Front) approach, stating the main point or request immediately to respect the reader's time."
    },
    {
        "name": "GitHub Commit Verification (wb01) [Medium]",
        "text": "You committed and pushed a file named `index.html` to your GitHub repository. How can you verify that the exact code you wrote was successfully uploaded?",
        "type": "MCQ",
        "choices": [
            "By clicking on the file name in the GitHub web interface and reading the code.",
            "By checking if the StackBlitz preview updates.",
            "By looking at your local file manager.",
            "By refreshing your browser."
        ],
        "answer": 1,
        "feedback": "The definitive way to check a successful push is to navigate to the repository URL on GitHub.com and visually inspect the file contents there."
    },
    # wb02 (HTML basics)
    {
        "name": "HTML Heading Hierarchy (wb02) [Easy]",
        "text": "In a well-structured HTML document, how many `<h1>` tags should ideally be present on a single page for SEO and accessibility?",
        "type": "MCQ",
        "choices": [
            "Exactly one.",
            "As many as needed for big text.",
            "Zero, because it is outdated.",
            "One per `<section>`."
        ],
        "answer": 1,
        "feedback": "Best practices dictate that a page should have exactly one `<h1>` tag to represent the main title or topic of the page."
    },
    {
        "name": "Image Alt Attribute (wb02) [Medium]",
        "text": "What is the primary technical purpose of the `alt` attribute in an `<img>` tag?",
        "type": "MCQ",
        "choices": [
            "To provide alternative text if the image fails to load or for screen readers.",
            "To define a tooltip when the user hovers over the image.",
            "To specify a secondary image URL.",
            "To center the image."
        ],
        "answer": 1,
        "feedback": "The `alt` attribute specifies alternative text that is displayed if the image cannot be loaded and is read by screen readers for accessibility."
    },
    {
        "name": "HTML Nested Lists (wb02) [Hard]",
        "text": "You want to create a bulleted list where the second item has its own sub-list. Which HTML structure is valid?",
        "type": "MCQ",
        "choices": [
            "<ul><li>Item 1</li><li>Item 2 <ul><li>Sub</li></ul></li></ul>",
            "<ul><li>Item 1</li><ul><li>Item 2</li></ul></ul>",
            "<ul><li>Item 1</li><li>Item 2</li><ul><li>Sub</li></ul></ul>",
            "<ul><li>Item 1</li><li>Item 2</li><li><ul><li>Sub</li></ul></li></ul>"
        ],
        "answer": 1,
        "feedback": "A nested list must be placed *inside* an `<li>` element. Placing a `<ul>` directly as a child of another `<ul>` (outside an `<li>`) is invalid HTML."
    },
    {
        "name": "Paragraph Tag Default Margin (wb02) [Medium]",
        "text": "When you place a `<p>` tag in an empty HTML file, it does not sit flush against the top of the browser window. Why?",
        "type": "MCQ",
        "choices": [
            "Browsers apply a default CSS margin to the `<p>` element and `<body>`.",
            "The `<p>` tag has padding built into the HTML specification.",
            "It is a bug in StackBlitz.",
            "Text always requires 10px of space."
        ],
        "answer": 1,
        "feedback": "Browsers have User Agent Stylesheets that apply default margins to `<body>` and block-level text elements like `<p>`."
    },
    # wb03 (Forms)
    {
        "name": "Form Input Labeling (wb03) [Medium]",
        "text": "To correctly associate a `<label>` with an `<input>` for accessibility, which attributes must match?",
        "type": "MCQ",
        "choices": [
            "The `for` attribute of the label and the `id` attribute of the input.",
            "The `name` attribute of the label and the `name` attribute of the input.",
            "The `id` attribute of the label and the `class` attribute of the input.",
            "The `for` attribute of the label and the `class` attribute of the input."
        ],
        "answer": 1,
        "feedback": "A label is linked to an input by setting the label's `for` attribute to the exact value of the input's `id` attribute."
    },
    {
        "name": "Form Required Validation (wb03) [Easy]",
        "text": "How do you prevent a form from being submitted if a specific text input is left empty by the user?",
        "type": "MCQ",
        "choices": [
            "Add the `required` boolean attribute to the `<input>` tag.",
            "Set `validate=\"true\"` on the form.",
            "Use CSS `content: required;`.",
            "Change the button type to `required-submit`."
        ],
        "answer": 1,
        "feedback": "The `required` attribute is a standard HTML5 feature that prevents form submission if the input is empty."
    },
    {
        "name": "Checkbox Default State (wb03) [Easy]",
        "text": "Which attribute should you add to an `<input type=\"checkbox\">` to make it selected by default when the page loads?",
        "type": "MCQ",
        "choices": [
            "checked",
            "selected",
            "default",
            "value=\"true\""
        ],
        "answer": 1,
        "feedback": "The `checked` boolean attribute makes a checkbox or radio button selected by default."
    },
    {
        "name": "Input Placeholder vs Value (wb03) [Medium]",
        "text": "What is the difference between the `placeholder` attribute and the `value` attribute on a text input?",
        "type": "MCQ",
        "choices": [
            "Placeholder is hint text that disappears when typing; Value is the actual submitted data.",
            "They are interchangeable.",
            "Value is hint text; Placeholder is the submitted data.",
            "Placeholder is only used for passwords."
        ],
        "answer": 1,
        "feedback": "`placeholder` provides a visual hint but is not submitted. `value` defines the initial data of the input, which is submitted if not changed."
    },
    # wb05 (CSS basics)
    {
        "name": "CSS Inheritance Testing (wb05) [Hard]",
        "text": "Create this structure in StackBlitz: `<div style=\"border: 1px solid red; color: blue;\"><p>Text</p></div>`. Open DevTools. Does the `<p>` element inherit the border from the `<div>`?",
        "type": "MCQ",
        "choices": [
            "No, borders are not inherited by default.",
            "Yes, all CSS properties are inherited.",
            "Yes, but only if the paragraph is empty.",
            "No, because inline styles cannot be inherited."
        ],
        "answer": 1,
        "feedback": "In CSS, typography properties (like color, font-family) are typically inherited, but layout properties (like border, margin, padding) are NOT inherited by default."
    },
    {
        "name": "CSS Class Multiple Assignment (wb05) [Easy]",
        "text": "Can an HTML element have more than one CSS class applied to it?",
        "type": "MCQ",
        "choices": [
            "Yes, separated by spaces within the class attribute.",
            "No, an element can only have one class.",
            "Yes, separated by commas.",
            "Yes, by using multiple class attributes."
        ],
        "answer": 1,
        "feedback": "Elements can have multiple classes by separating them with a space (e.g., `class=\"btn btn-primary\"`)."
    },
    {
        "name": "CSS Hex Color Code (wb05) [Medium]",
        "text": "In the CSS color code `#FF0000`, what color does this represent?",
        "type": "MCQ",
        "choices": [
            "Red",
            "Green",
            "Blue",
            "White"
        ],
        "answer": 1,
        "feedback": "Hex codes are structured as #RRGGBB. FF is the maximum value for Red, and 00 is zero for Green and Blue, resulting in pure red."
    },
    {
        "name": "CSS External File Link (wb05) [Easy]",
        "text": "Which HTML tag is used to link an external CSS file named `style.css` to an HTML document?",
        "type": "MCQ",
        "choices": [
            "<link rel=\"stylesheet\" href=\"style.css\">",
            "<style src=\"style.css\"></style>",
            "<css href=\"style.css\"></css>",
            "<script src=\"style.css\"></script>"
        ],
        "answer": 1,
        "feedback": "The `<link>` tag with `rel=\"stylesheet\"` and the `href` attribute is the standard way to connect external CSS."
    },
    # wb06 (Box model, DevTools)
    {
        "name": "DevTools Element Selection (wb06) [Easy]",
        "text": "In Chrome DevTools, what is the shortcut or method to quickly select an element on the page for inspection?",
        "type": "MCQ",
        "choices": [
            "Right-click the element on the page and select 'Inspect'.",
            "Press F5.",
            "View Page Source.",
            "You must manually search through the HTML tree."
        ],
        "answer": 1,
        "feedback": "Right-clicking and selecting 'Inspect' (or using the inspect tool icon) directly highlights the element in the Elements panel."
    },
    {
        "name": "Box Model Margin Collapse (wb06) [Hard]",
        "text": "You have two `<div>` elements stacked vertically. The top div has `margin-bottom: 20px;`. The bottom div has `margin-top: 30px;`. How much vertical space is rendered between them?",
        "type": "MCQ",
        "choices": [
            "30px",
            "50px",
            "20px",
            "10px"
        ],
        "answer": 1,
        "feedback": "Due to margin collapsing in regular block formatting contexts, adjoining vertical margins collapse to the larger of the two values (30px), rather than adding them together (50px)."
    },
    {
        "name": "Box-Sizing Property (wb06) [Medium]",
        "text": "What happens when you apply `box-sizing: border-box;` to an element?",
        "type": "MCQ",
        "choices": [
            "Padding and border are included within the element's specified width and height.",
            "The element loses its margin.",
            "The element behaves like an inline element.",
            "Padding expands the total width beyond the specified width."
        ],
        "answer": 1,
        "feedback": "`box-sizing: border-box` forces the specified width to include the content, padding, and border, making layout calculations much easier."
    },
    {
        "name": "DevTools Network Tab (wb06) [Medium]",
        "text": "If an image fails to load (shows a broken icon), which tab in Chrome DevTools is most helpful to see why the request failed (e.g., 404 error)?",
        "type": "MCQ",
        "choices": [
            "Network",
            "Elements",
            "Sources",
            "Performance"
        ],
        "answer": 1,
        "feedback": "The Network tab displays all HTTP requests made by the page, showing their status codes (like 404 Not Found) and response details."
    },
    # wb07 (Flexbox)
    {
        "name": "Flexbox Cross Axis Alignment (wb07) [Medium]",
        "text": "If a flex container has `flex-direction: row;`, which property aligns the items vertically?",
        "type": "MCQ",
        "choices": [
            "align-items",
            "justify-content",
            "vertical-align",
            "align-content"
        ],
        "answer": 1,
        "feedback": "With `row` direction, the main axis is horizontal. The cross axis is vertical. `align-items` controls alignment along the cross axis."
    },
    {
        "name": "Flexbox Wrap (wb07) [Easy]",
        "text": "When you have too many items in a flex container, they might shrink to fit on one line. What property prevents shrinking and allows them to flow to the next line?",
        "type": "MCQ",
        "choices": [
            "flex-wrap: wrap;",
            "flex-flow: row;",
            "overflow: visible;",
            "display: block;"
        ],
        "answer": 1,
        "feedback": "`flex-wrap: wrap` tells the container to wrap items onto multiple lines if they exceed the container's width."
    },
    {
        "name": "Flex Item Property (wb07) [Medium]",
        "text": "Which of the following properties is applied to a flex ITEM (the child), rather than the flex CONTAINER (the parent)?",
        "type": "MCQ",
        "choices": [
            "flex-grow",
            "justify-content",
            "align-items",
            "flex-direction"
        ],
        "answer": 1,
        "feedback": "`flex-grow`, `flex-shrink`, and `flex-basis` are applied directly to the child items to control how they distribute space. The others are container properties."
    },
    {
        "name": "Flexbox Space Between (wb07) [Medium]",
        "text": "What does `justify-content: space-between;` do?",
        "type": "MCQ",
        "choices": [
            "Pushes the first item to the start, the last item to the end, and evenly distributes space between the rest.",
            "Centers all items with equal space around them.",
            "Adds equal space before the first item and after the last item.",
            "Removes all margins from the items."
        ],
        "answer": 1,
        "feedback": "`space-between` maximizes the distance between the outermost items, pushing them to the edges of the container."
    },
    {
        "name": "Flexbox Gap (wb07) [Easy]",
        "text": "What is the modern CSS property specifically designed to add spacing between flex items without using margins?",
        "type": "MCQ",
        "choices": [
            "gap",
            "spacing",
            "margin-between",
            "flex-space"
        ],
        "answer": 1,
        "feedback": "The `gap` property (formerly `grid-gap`) works in Flexbox to add exact spacing between items without affecting outer margins."
    }
]

questions.extend(additional)

with open('/home/hyuk/nvme_data/prj/stu/stu2603/web-output/wb08/mid-eval-q.md', 'w') as f:
    for q in questions:
        f.write(f"[Question name]\n{q['name']}\n\n[Question text]\n{q['text']}\n\n")
        if q['type'] == 'MCQ':
            for i, choice in enumerate(q['choices']):
                if i + 1 == q['answer']:
                    f.write(f"[Choice {i+1} (정답 100%)]\n{choice}\n\n")
                else:
                    f.write(f"[Choice {i+1}]\n{choice}\n\n")
            f.write(f"[Answer 1]\n{q['answer']}\n\n")
        elif q['type'] == 'CLOZE':
            f.write(f"{q['answer']}\n\n")
            
        f.write(f"[General feedback]\n{q['feedback']}\n\n---\n\n")

print(f"Generated {len(questions)} questions.")
