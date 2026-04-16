# wb07 Handout: Flexbox Layouts

## 1. Concept References

This week, we will conquer arranging layouts effortlessly using **Flexbox**, dive into **Refactoring**, and learn essential **Windows Survival Skills**.

### 1-1. Flexbox Mastery: The "Alignment Manager"
Flexbox (`display: flex`) is a powerful "Alignment Manager" for your web house. It allows you to instinctively align and distribute space among items in a container, even when their size is unknown.
*   **The Mother Principle (Parent-Child)**: `display: flex` is ALWAYS declared on the **parent container**. This instantly turns the children into flex items. Applying it to a child only aligns that child's own descendants.
*   **flex-direction (The Orientation)**: Determines the alignment flow. `row` (horizontal) is essential for navigation bars, while `column` (vertical) is often used for entire mobile layouts.
*   **justify-content (Main Axis Spacing)**: Like magic, the computer finds the best spacing.
    *   `center`: Gathers everything in the middle.
    *   `space-between`: Pins the first/last items to the edges and distributes space in between.
    *   `space-around`: Gives equal space on both sides of every item.
*   **align-items (Cross Axis Alignment)**: Manages vertical alignment. 
    *   `center`: Perfectly centers icons and text.
    *   `flex-start`: Aligns items to the top "ceiling" of the container.
    *   `baseline`: Aligns the bottom lines of text even when boxes have different sizes—crucial for typography.
*   **flex-wrap (The Overflow Guard)**: Determines what happens when items run out of space.
    *   `nowrap` (Default): Forces everything onto one line, often squashing items.
    *   `wrap`: Naturally moves overflowing items to the next line, forming the basis of **Responsive Web Design**.

### 1-2. Layout Refactoring & Debugging: "The Stethoscope"
Writing code is only half the battle; fixing and improving it (**Refactoring**) is the other half. Simple functioning isn't enough; we aim for code that is restructured in a better, more professional way.
*   **Developer Tools (F12)**: This is your doctor's stethoscope. Use the **Elements** tab to view the **DOM Tree** (HTML structure) and the **Styles** panel to see real-time CSS.
*   **Precision Debugging**: Use the Inspector icon to target an overflowing element. You'll often find that a child stands firm with a fixed `width: 1000px;` (like a piece of iron) while the parent container tries to flex like a rubber band, causing an **Overflow**.
*   **The golden rule of F12**: Modifications in DevTools are **temporary**. Always follow the sequence: **Check in Tools → Apply to CSS File → Save**.

### 1-3. Windows Survival Skills (Computer Utilization)
Mastering your operating system is as important as mastering code. It protects your data and skyrockets your productivity.
*   **Search, Don't Sort**: Stop building deep, confusing folder hierarchies. Use strong names (e.g., `20261015_Portfolio_John_v1.html`) and rely on `Win + F`. **Search, Don't Sort** is the heart of file management.
*   **File Extension Guard**: Enable "Show File Extensions" in Explorer. A file that looks like a PDF might actually be a dangerous `.exe` file.
*   **Clipboard History (`Win + V`)**: Forget the frustration of losing a copied link. Enable your history to see a list of everything you've copied today and paste selectively.
*   **Screen Capture Master (`Win + Shift + S`)**: Don't use `Print Screen` and Paint. Crop exactly what you need; it copies instantly to your clipboard so you can `Ctrl + V` directly into KakaoTalk, Email, or Slack.
*   **Snapping & Virtual Desktops**: Use `Win + Arrow Keys` to snap windows to the half-screen instantly—no manual resizing needed. Use `Win + Tab` to create multiple Virtual Desktops (e.g., one for class, one for personal work) to mimic a multi-monitor setup on one screen.
*   **Task Manager (`Ctrl + Shift + Esc`)**: When a program freezes, don't hold the power button (which risks data loss). Open the Task Manager to "End Task" on the specific unresponsive program and "Kill" hidden processes that are hogging your CPU.
*   **Extraction Habit**: Never run contents directly from a `.zip` file. Always **Right-click > Extract All** first. Running from temporary paths is a leading cause of path errors and "It's not working" headaches.

---

## 2. Lab Assignment

This week's lab is to refine your **Personal Profile (Name Card) page** using Flexbox. Open the files in the `lab/` folder and follow these steps:

### [Step 1] Navigation Menu Alignment
*   **File**: `styles.css`
*   **Mission**: Align the vertical menu buttons horizontally by applying `display: flex;` to the navigation menu. Use the `justify-content` property to distribute space evenly between buttons.

### [Step 2] Horizontal Card Layout
*   **File**: `styles.css` (.content-wrapper)
*   **Mission**: Apply `display: flex;` to the content wrapper to place the two stacked cards side-by-side. Also, use the `gap` property to adjust the spacing between the cards. (If you only have one card, add another one to practice horizontal alignment.)

### [Step 3] Fix Image Overflow
*   **File**: `index.html` or `styles.css`
*   **Mission**: Using **fixed pixel (px) sizes** like `1000px` causes images to overflow on smaller screens. **Do not delete the fixed size code; comment it out (`/* ... */`)** and then write the correct code using `max-width: 100%;` below it. (If you're not sure how to 'comment out' code, ask Gemini "How to add comments in HTML/CSS" before you start!)

---

### [Submission Instructions]
1.  **GitHub Submission**: Upload your `index.html` and `styles.css` files to your GitHub repository and submit the **GitHub repository URL** to the [Lab Peer Evaluation](https://docs.google.com/forms/d/e/1FAIpQLSd-WAEm3i5NjCuVmgvr8nr41mJ0o6En8xpII543oNAi44BRuw/viewform) form.
2.  **Ping your Checkbox**: Once completed, type `1` in the Ping column of the class Google Sheet.

---

## 3. Email Assignment (Assignment 0.7)

Complete the tasks below and submit them directly in the body of your email to `wonhyukc@stu.ac.kr`. Do not attach MS Word or PDF files unless specifically requested.

**Email Subject Format**: `Assignment 0.7 StudentID` (Example: `Assignment 0.7 20240001`)

1.  **Class Reflections** <!-- 수업 소감 -->: Write a brief (max 3 lines) reflection on both the online Flipped Learning video and the physical offline class.
2.  **TED Video Reflection**: Watch Derek Sivers' TED Talk "How to start a movement" and write briefly about what you learned.
3.  **Article Search and Reflection** <!-- 아티클 검색 및 소감 작성 (AI 및 웹 검색 활용) -->:
    *   Search and read about "How Passwords Changed My Life" <!-- 비밀번호가 어떻게 내 삶을 바꿨는가 -->. Write your thoughts.
    *   **Ebbinghaus Forgetting Curve**: Google "Ebbinghaus forgetting curve", explain what it is, and write how you can apply this to your personal study habits.
    *   Search and read articles relating to "Brain damage and Multitasking" and write your thoughts.
    *   Repeatedly search for "best job 2025" and the best/worst jobs of the year for at least four different years. Write your conclusions.
4.  **Passkey Practice** <!-- 패스키(Passkey) 실습 -->:
    *   Ask Gemini what a "Passkey" is, study it, and write a brief reflection on your findings.
    *   Register a Passkey on your personal smartphone first.
    *   Then, go to the public lab computer at school and attempt to log in using the Passkey you just created.
    *   **Attach a screenshot (under 100KB)** of the screen where you are logging in using a Passkey to your email submission.

---

### Boilerplate (Optional Missions & Q&A)
*(The following is common for all assignments)*

*   **Deep Learning (Optional)**: If the assignment above is too easy for you, ask Gemini to give you the next step in web development. Study it, and summarize your findings in your email in under 3 lines.
*   **Presentation Request**: If you are willing to deliver a short presentation on the class topics, a tech trend, or your life/hometown (e.g., sharing how difficult your part-time job is), please write to apply. Bonus points are given!
*   **Q&A Board**: Post any questions you encounter while studying on the class Q&A board. If you do not get an answer, ask me again in class. You can also request to teach a specific topic.
*   **30-Day Challenge & Typing Practice**: Continue these persistently. Even if not specifically requested, if you practiced this week, summarize it in your email in under 3 lines.
