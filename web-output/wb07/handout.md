# wb07 Handout: Flexbox Layouts

## 1. Concept References

This week, we will conquer arranging layouts effortlessly using **Flexbox**, dive into **Refactoring**, and learn essential **Windows Survival Skills**.

### 1-1. Flexbox Layouts
Flexbox (`display: flex`) is a powerful CSS layout module that allows you to instinctively align and distribute space among items in a container, even when their size is unknown.
*   **Flex Container**: The parent element (e.g., `<ul>`, `<div class="container">`) where you apply `display: flex;`. This instantly turns the children into flex items.
*   **flex-direction**: Defines the direction items are placed:
    *   `row`: Horizontal placement (left to right). Essential for making navigation bars.
    *   `column`: Vertical placement (top to bottom).
*   **justify-content**: Aligns items along the main axis. Useful values include:
    *   `center`: Gathers items in the middle.
    *   `space-between`: Distributes items evenly with the first item at the start and the last at the end.
    *   `space-around`: Distributes items evenly with equal space around them.
*   **align-items**: Aligns items vertically across the cross axis (e.g., `center`).

### 1-2. Layout Refactoring & Debugging
Writing code is only half the battle; fixing broken code (Refactoring) is equally important.
*   **Developer Tools (F12)**: Your "stethoscope" for diagnosing layout issues. Use it to find overlapping or out-of-bounds elements.
*   **Overflow Issues**: Often caused by fixed pixel widths on child elements ignoring their parent container's flexible size. Fix these by using relative units like `%` or `max-width: 100%` so elements can shrink flexibly.

### 1-3. Windows Survival Skills (Computer Utilization)
Beyond coding, mastering your operating system significantly improves your productivity and data safety.
*   **Search, Don't Sort**: Stop making deep folder hierarchies. Use strong, contextual file names (e.g., `20261015_Portfolio_John_v1.html`) and rely on your OS's search function.
*   **File Extensions**: Ensure hidden extensions (`.exe`, `.jpg`, `.pdf`) are visible in your File Explorer to avoid malicious files.
*   **Clipboard History (`Win + V`)**: Saves multiple copied items so you can paste selectively.
*   **Screen Capture Master (`Win + Shift + S`)**: Directly copy a specific cropped area to your clipboard instead of capturing the whole screen.
*   **Virtual Desktops & Split Screen (`Win + Tab` / `Win + Arrow Keys`)**: Efficiently split your screen for coding on one side and documentation on the other, or use virtual desktops for more space.
*   **Task Manager (`Ctrl + Shift + Esc`)**: Safely force-quit (Kill) unresponsive programs instead of holding the power button.
*   **Zip Extraction**: Always unzip files completely before attempting to run their contents to avoid path errors.

---

## 2. 실습 과제 (Assignment)

This week, your assignment is a coding layout lab.

1.  **Flexbox Portfolio (Coding)**: 
    *   Open your project in StackBlitz.
    *   Use the Flexbox properties (`display: flex; justify-content: space-around;`) to arrange your top navigation menu horizontally.
    *   Ensure that any layout overlaps from last week are fixed.
    *   Submit the StackBlitz URL of your updated portfolio to the Google Form: [실습 상호평가 제출](https://docs.google.com/forms/d/e/1FAIpQLSd-WAEm3i5NjCuVmgvr8nr41mJ0o6En8xpII543oNAi44BRuw/viewform).

2.  **Ping your Checkbox**: Once you have completed all tasks, navigate to the class assignment Google Sheet and type `1` in the Ping column by your name to confirm completion.

---

## 3. Email Assignment (Assignment 0.7)

Complete the tasks below and submit them directly in the body of your email to `wonhyukc@stu.ac.kr`. Do not attach MS Word or PDF files unless specifically requested.

**Email Subject Format**: `Assignment 0.7 StudentID` (Example: `Assignment 0.7 20240001`)

1.  **Class Reflections (수업 소감)**: Write a brief (max 3 lines) reflection on both the online Flipped Learning video and the physical offline class.
2.  **TED Video Reflection (TED 시청 소감)**: Watch Derek Sivers' TED Talk "How to start a movement" and write briefly about what you learned.
3.  **Article Search and Reflection (아티클 검색 및 소감 작성 (AI 및 웹 검색 활용))**:
    *   Search and read about "How Passwords Changed My Life (비밀번호가 어떻게 내 삶을 바꿨는가)". Write your thoughts.
    *   **Ebbinghaus Forgetting Curve**: Google "Ebbinghaus forgetting curve", explain what it is, and write how you can apply this to your personal study habits.
    *   Search and read articles relating to "Brain damage and Multitasking" and write your thoughts.
    *   Repeatedly search for "best job 2025" and the best/worst jobs of the year for at least four different years. Write your conclusions.
4.  **Passkey Practice (패스키(Passkey) 실습)**:
    *   Ask Gemini what a "Passkey" is, study it, and write a brief reflection on your findings.
    *   Register a Passkey on your personal smartphone first.
    *   Then, go to the public lab computer at school and attempt to log in using the Passkey you just created.
    *   **Attach a screenshot (under 100KB)** of the screen where you are logging in using a Passkey to your email submission.

---

### [공통/상시] 심화 및 발표 관련 (Boilerplate)
*(The following is common for all assignments)*

*   **Deep Learning (Optional)**: If the assignment above is too easy for you, ask Gemini to give you the next step in web development. Study it, and summarize your findings in your email in under 3 lines.
*   **Presentation Request**: If you are willing to deliver a short presentation on the class topics, a tech trend, or your life/hometown (e.g., sharing how difficult your part-time job is), please write to apply. Bonus points are given!
*   **Q&A Board**: Post any questions you encounter while studying on the class Q&A board. If you do not get an answer, ask me again in class. You can also request to teach a specific topic.
*   **30-Day Challenge & Typing Practice**: Continue these persistently. Even if not specifically requested, if you practiced this week, summarize it in your email in under 3 lines.
