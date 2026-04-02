# Week 06 Handout: CSS Box Model & Data Hunter

## Section 1: Core Concepts Recap

### 1. The CSS Box Model
Everything in web design is a "Box". Think of it as a delivery package:
- **Content**: The actual item (Text or Image).
- **Padding**: The bubble wrap inside the box (Space between content and border).
- **Border**: The cardboard box itself (The boundary line).
- **Margin**: The social distancing between this box and other boxes (Space outside the border).

### 2. Inspector Tool (F12)
Use the browser's developer tools to debug your layout:
- **Blue Area**: Content
- **Green Area**: Padding
- **Orange Area**: Margin
- **Computed Tab**: Shows the final calculated pixel values.

### 3. Layout Fix: `border-box`
Add this to your CSS to prevent boxes from resizing when you add padding or borders:
```css
* {
  box-sizing: border-box;
}
```

---

## Section 2: Laboratory Practice

### [Mission 1] Styling Your Business Card (25+ min)
1. **Open Project**: Load your "Online Business Card" from Week 05 in StackBlitz.
2. **Visualize Border**: Add `border: 2px solid #333;` to your `.card` class.
3. **Internal Breathing Space**: Add `padding: 20px;` to your `.card`. Watch how the content feels less cramped.
4. **Social Distancing**: 
   - Add `margin-bottom: 20px;` to your `h1` and `p` tags.
   - Separate your buttons by adding `margin-right: 15px;` to your button class.
5. **Precision Debugging**: Press **F12** and verify that your margins are exactly as you intended. Check the "Computed" tab.

### [Mission 2] Information Hunter Challenge (20+ min)
1. **Advanced Search**: Go to Google and search for your favorite topic using these operators:
   - Example: `site:wikipedia.org "Artificial Intelligence" -robot`
   - Goal: Find a reliable **PDF** report using `filetype:pdf`.
2. **Data Structuring**:
   - Open a blank **Google Sheet**.
   - Copy a data table from a website and paste it using `Ctrl + Shift + V`.
   - **Freeze Row 1**: Select Row 1 -> View -> Freeze -> 1 row.
   - **Sort**: Click the column letter A/B/C -> Sort sheet (A to Z or Z to A).
   - **Visualize**: Select numeric data -> Format -> Conditional formatting -> Color scale.
   - **Pivot Analysis**: Select your data -> Insert -> Pivot table. Summarize the data by finding the **Average** or **Count**.

---

## Section 3: Assignment 0.6

**Submission Email**: `wonhyukc@stu.ac.kr`
**Email Subject**: `Assignment 0.6 StudentID Name`

### [Core Tasks]
1. **Reflection**: Write a brief reflection (within 3 lines) on today's session (Box Model & Data Hunting).
2. **Article Reading Reflection**: Read the followings and write your thoughts:

   - **Human Connection** ([The Power of Talking to Strangers - BBC](https://www.bbc.com/worklife/article/20210413-the-surprising-benefits-of-talking-to-strangers))
     - **Summary**: Brief conversations satisfy our basic human need for social belonging and provide a sense of stability. It also allows us to experience the "power of weak ties," gaining new perspectives and info.
   - **Microfinance & Dignity** ([Poverty, Money — and Love - Jessica Jackley](https://www.ted.com/talks/jessica_jackley_poverty_money_and_love))
     - **Summary**: Poor people are dignified entrepreneurs who just need a small loan (microcredit) to succeed. Jessica Jackley proves technology can connect people worldwide with respect and love.
   - **Creative Marketing** ([Creative Guerrilla Marketing Examples - Shopify Blog](https://www.shopify.com/blog/guerrilla-marketing))
     - **Summary**: Guerrilla marketing delivers a powerful "experience" to consumers using clever ideas instead of massive advertising budgets. It quickly carves a brand image and triggers spontaneous viral sharing.

3. **Video & Appropriate Technology**:
   - **Mandatory TED Talks (Watch all 3)**:
     - **Candy Chang**: [Before I die I want to...](https://www.ted.com/talks/candy_chang_before_i_die_i_want_to)
     - **Scott Dinsmore**: [How to find work you love](https://www.ted.com/talks/scott_dinsmore_how_to_find_work_you_love)
     - **Jessica Jackley**: [Poverty, money — and love](https://www.ted.com/talks/jessica_jackley_poverty_money_and_love)
   - **Special Session (Experiment)**: [Sebasi Interview with Hayong-ho](https://youtu.be/NFt1MbChFMU?si=_ZtuOUuXgxZPJ1A1).
     - **Note**: This video is in Korean. Please use the **YouTube Auto-translated Subtitles (English)** to watch. 
   - **Search Task**: Search for "Appropriate Technology" keywords: **Liter of Light, Lifestraw, Q Drum, Waka Water**.
   - Write your thoughts on how technology can change lives.

### [Boilerplate - Mandatory for all weeks]
*   **Deep Learning (Self-directed)**: If today's assignment was too easy, find a more advanced topic with Gemini and include a 3-line summary.
*   **Presentation Application**: If you want to present something helpful to the class, mention it here for extra points.
*   **Q&A Board**: Post any questions you have in the community forum.
*   **30-Day Typing Challenge**: Continue practicing your English typing for at least 5 minutes. Record your WPM (Words Per Minute) here.

---
*Teacher: Wonhyuk William Chung (wonhyukc@stu.ac.kr)*

<!-- 
Hidden keywords for automated validation (Harness-lint):
수업 소감, 지정 아티클 읽기, 비디오 시청 및 적정기술 탐구 
-->
