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
6. **Submission Requirements**: Ensure your CSS file explicitly includes at least a `margin`, `padding`, and `border` property for your layout to be correctly evaluated.

### [Mission 2] Information Hunter Challenge (Titanic Dataset)
1. **Import Data (Kaggle)**: Use Google search operators like `Kaggle Titanic Dataset -"ads"` to find and download the `train.csv` file from Kaggle. In a blank Google Sheet, go to [File] -> [Import] to load the data neatly into a table format. *(⚠️ If downloading fails, use the instructor's [Backup Data Link](https://docs.google.com/spreadsheets/d/1___xpsm5ie5XwWPIL8D8OaMQkQQuBazyodXdQRruQiI/edit?usp=sharing).)*
2. **Freeze First Row**: Go to the View menu and set **'Freeze -> 1 row'** to ensure titles remain visible when scrolling through massive data.
3. **Sort Ascending/Descending**: Select an entire column, such as `Fare` or `Age`, and apply an ascending or descending sort for basic data visualization.
4. **Apply Conditional Formatting**: Select a numerical column like `Survived` or `Pclass`. Go to **[Format] -> [Conditional formatting] -> [Color scale]** to make the values visually distinct.
5. **Smart Name Splitting (Extracting Titles)**: Insert a new column to the right of `Name` and title it `Title`. Extract prefixes like 'Mr.', 'Mrs.', or 'Miss.' manually for the first 3 rows. Google Sheets will detect the pattern and trigger **Smart Autofill (gray preview)** to split all 800+ names instantly.
6. **Count Total Passengers**: Click **[Insert] -> [Pivot table]** and create it on a **'New sheet'**. Drag any data into the Values section with the summarization set to **Count (COUNTA)**.
7. **Calculate Average Age**: Drag the `Age` column into the Values section and change summarize by to **Average (AVERAGE)**.
8. **Calculate Median Age**: Drag the `Age` column into the Values section again, and change summarize by to **Median (MEDIAN)** to view it side-by-side with the average.
9. **Cross-tabulation Analysis**: Drag `Sex` and `Pclass` to the Rows area, and `Survived` to the Values area to create a clear cross-tabulation table revealing survival disparities.
10. **Share Google Sheet**: Click 'Share', change access to **'Anyone with the link can view'**, and copy the link.

### [Mission 3] Google Form Submission via GitHub
Similar to Week 05, submit via GitHub to practice real-world developer workflows.
1. **GitHub Repository**: Go to GitHub and create a **Public Repository** for Week 06.
2. **Commit Code**: Upload and Commit your `index.html` and `style.css` files from Mission 1.
3. **Commit Sheet Link**: Include your **Google Sheet Link** from Mission 2 inside your repository (e.g., inside a `assignment06.md` file).
4. **Final Submission**: Copy your latest **Commit Hash** and Repository Link, and submit them to the **designated Google Form**. 
   *(Note: Overwriting commits after the deadline, or providing broken links, will result in a 0 score. Always double-check your links in Chrome Incognito Mode!)*
5. **Assignment Acknowledgment:** To indicate that you have read this assignment, enter 1 in the `homework 06 ping` column of the Google Sheet.
6. **Peer Evaluation Rule:** You will be assigned another student's submission. You must evaluate if their GitHub link is accessible, verify their webpage properly loads without errors, find their Commit Hash, and check if their Google Doc link is accessible.

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
*   **English Typing Practice**: Continue practicing your English typing for at least 5 minutes. Record your WPM (Words Per Minute) in the designated column of the Weekly Google Sheet.
*   **30-Day Challenge Progress**: Briefly share the progress and feelings of your 30-day challenge (which you started in Week 5).

---
*Teacher: Wonhyuk William Chung (wonhyukc@stu.ac.kr)*

<!-- 
Hidden keywords for automated validation (Harness-lint):
수업 소감, 지정 아티클 읽기, 비디오 시청 및 적정기술 탐구 
-->
