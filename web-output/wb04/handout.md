# Week 4 Handout: CSS Basics and Selection

## 1. Concept Reference (Key Takeaways from Slides)

### 🎯 Learning Goals Checklist
- Apply CSS selectors and properties to style HTML.
- Design a personal business card with custom colors and fonts.
- Experience styling inheritance and debug collision errors.

### What is CSS? (The Clothing Metaphor)
- **HTML**: The skeleton structure (dividing regions).
- **CSS**: The flesh and clothes (design and layout).
- **Advantage of Separation**: Maintains design consistency across the website and makes future modifications much easier.

### 3 Ways to Apply CSS
1. **Inline**: Written inside the HTML tag (e.g., `<h1 style="...">`). *Not recommended.*
2. **Internal**: Written inside a `<style>` block within the `<head>` section.
3. **External**: Linked to a separate `.css` file. *Best practice!*

### Essential CSS Properties
- `color`: Changes text color.
- `background-color`: Changes the background color of an element.
- `font-size`: Adjusts the size of the text.

### CSS Selectors
- **Tag Selector**: Selects all elements of a specific HTML tag (e.g., `div { }`).
- **Class Selector (`.`)**: Used for multiple, repetitive elements (e.g., `.highlight`).
- **ID Selector (`#`)**: Used for a single, unique element (e.g., `#main-title`).

### 🐞 Debugging Techniques
- **Invisible Text?**: Suspect that the text color and the background color might be identical.
- **Inheritance Awareness**: Remember that styles applied to a parent element (like `<body>`) are inherited down to its child elements.
- **Style Collisions**: When multiple styles compete for the same element, understand how priority (specificity) determines the winner (ID > Class > Tag).

## 2. Lab Assignment
*Open the provided StackBlitz link on eCampus. This lab should take you approximately 25-30 minutes to complete.*

**Step 1. Link Your Stylesheet (3 min)** 
Review the initial HTML structure. Create a new file named `style.css` and link it inside the `<head>` of your `index.html` file using the `<link>` tag.

**Step 2. Global Styling (5 min)** 
In your `style.css`, use the `body` tag selector to apply a global background color. Test 3 different HTML color names (e.g., `aliceblue`, `lightgray`, `lavender`) and pick your favorite. Also, change the global `font-family` to `sans-serif`.

**Step 3. Unique Element Styling using IDs (7 min)** 
Identify the main heading of your business card (e.g., your name). Give it an `id` like `#main-title`. In your CSS, style this ID by giving it a unique text color, a larger `font-size` (e.g., `36px`), and text underline.

**Step 4. Group Styling using Classes (5 min)** 
Identify repetitive elements like your job title, location, or skills. Give them all the same class name, like `.card-desc`. Style this class to have a subtle text color (e.g., `gray` or `#555`) and make them *italic*.

**Step 5. Fix the "Invisible Text" Bug (5 min)** 
Scroll down to the bottom of the HTML where there is an `<div class="invisible-bug">`. The text inside is black, and the background is also set to black. In your CSS, target `.invisible-bug` and change the text `color` to `white` or `yellow` so it becomes readable again.

**Step 6. Final Submission** 
Submit the completed StackBlitz URL or a screenshot of your styled business card to eCampus for peer review.

## 3. Assignment
Please complete the items below and send them via email to **wonhyukc@stu.ac.kr**.
- **Deadline**: Please refer to the specific deadline posted on eCampus.
- **Email Subject Format**: `Assignment 0.4 20240001` (Replace `20240001` with your Student ID)
- **Length**: Approximately half an A4 page.

### Required Contents

**[1. Class Reflection]**
Briefly reflect on what you learned this week. How does CSS differ from HTML in terms of coding experience?

**[2. Try It Out (Build-up)]**
Use AI to find the brand colors of your favorite company and apply them to your business card on StackBlitz.

**[3. AI Usage Experience]**
Provide the text format exactly as follows:
- **AI Prompt**: What did you ask the AI? (e.g., "Give me the CSS HEX color code for the Nike logo.")
- **AI Critique**: Did you face any issues such as invisible text due to identical background and foreground colors? How did the AI help you debug it?
- **Final Result**: Were you able to successfully apply the designated style? Attach a link or screenshot.
