# Web Programming (E-Track) Week 5 Handout: CSS Basics & Survival Skills

## 1. Concept Reference Area

### 📍 What is CSS?
* HTML provides the bare content and structural "bones" of a webpage. **CSS (Cascading Style Sheets)** is the "interior design" tool that coats those bones with colors, layouts, and beautiful visual decorations.

### 🎨 Three Ways to Apply CSS
1. **Inline Style:** Writing directly inside the HTML tag (e.g., `<h1 style="color: red;">`). Do not use this unless absolutely necessary.
2. **Internal Style:** Wrapping styles inside a `<style>` block located within the `<head>` section of the HTML file.
3. **External Style:** Creating a completely separate file like `style.css` to manage all styling like a centralized wardrobe. (This is used 99% of the time in the industry.)

### 🎯 Selectors: "Who should wear this outfit?"
* **Element Selector:** Selects all tags of that type universally (e.g., `p`, `h1`).
* **Class Selector (`.`):** Groups multiple elements under a specific name (e.g., `.box`, `.profile-img`). Think of it as a team uniform.
* **ID Selector (`#`):** A unique, one-of-a-kind name for a single element on the page (e.g., `#main-header`).

### 🐛 Mental Model for Survival (Communicating with Errors)
* **NEVER instantly click "X" on error pop-ups!** An error message is a frantic SOS signal from the computer asking for your help to fix a logical problem.
* The absolute fundamental skill of a developer is to naturally highlight the English error text, copy it (`Ctrl + C`), and paste it into Google or ChatGPT to ask for the root cause. 

### ⌨️ Magical Universal Keyboard Shortcuts
* **`Ctrl + C` (Cmd + C)** : Copy text or files.
* **`Ctrl + V` (Cmd + V)** : Paste text or files.
* **`Ctrl + Z` (Cmd + Z)** : Undo. (The ultimate time machine to revert your recent mistake).
* **`Ctrl + Shift + T` (Cmd + Shift + T)** : Resurrect the browser tab you accidentally closed a second ago.

---

## 2. Lab Section

This week's lab will exclusively take place on your browser, requiring no local installations. This exercise is designed to take at least **25 minutes** of deep focus. 

**Platform:** **StackBlitz**

**Step-by-Step Instructions:**
1. **Open your StackBlitz Project:**
   Access the previous week's 'Online Business Card' project URL that you saved. Make sure you can see both `index.html` and `style.css` in the file explorer.
2. **Connect the External CSS:**
   If not already present, ensure your HTML `<head>` has the link tag connecting it to your `style.css` file. 
3. **Brand Color Transformation (10 mins):**
   Choose your favorite global brand (e.g., Apple, Starbucks, Netflix, Spotify). Use a search engine or an AI tool to find the exact HEX color codes associated with that brand. Apply those HEX colors to the `background-color` and text `color` properties in your `style.css` file.
4. **Selector Practice (10 mins):**
   Assign a unique ID (`id="profile-name"`) to your name tag and a Class (`class="card-info"`) to your contact details. Target them appropriately in your CSS using `#` and `.` respectively. Change their `font-size` and `font-family`.
5. **Survival Keyboard Training (5 mins):**
   Open a "New Incognito Window" in Google Chrome (`Ctrl + Shift + N`). Understand that no login session or browsing history is preserved here. Close the tab, and aggressively practice the `Ctrl + Shift + T` shortcut to see if it restores the incognito tab (Spoiler: It won't, to protect privacy. Try it on normal tabs). Deliberately use `Ctrl + C`, `V`, and `Z` repeatedly inside your code editor to develop muscle memory.

---

## 3. Homework Section

You have two mandatory submissions for this week. Please carefully follow the instructions below.

### [Task A] eCampus Submission (Peer Evaluation)
* **Objective:** Submit your fully styled, brand-themed Online Business Card (Build-up Phase 3).
* **Submission Requirements:** 
  You must submit a text document or direct entry containing:
  1. The direct **Share URL** from StackBlitz. (Make sure your project is public or accessible via link).
  2. If using GitHub integration, ensure the link contains a unique **commit hash**.
  3. The link **MUST NOT return a 404 Error**. It must properly display your HTML/CSS code when clicked.
* **Where to Submit:** eCampus "Week 5 Assignment" Board.
* **Peer Evaluation Rule:** You will be assigned another student's submission. You must award 1 point for a valid URL format, 1 point for finding the unique identifier/hash, and 1 point if the page loads correctly without an error.

### [Task B] Email Submission (Self-Reflection & AI Critique)
* **Email Title Format:** `과제5 20240001` (Replace with your actual student ID. Failure to use this exact format will result in a 0 score as the automatic email filter will skip your submission).
* **Where to Submit:** `wonhyukc@stu.ac.kr`
* **Content Guidelines (Approx. half an A4 page as email body):**
  1. **Class Reflection:** Briefly describe which part of the "Computer Survival Skills" (shortcuts, incognito mode, error pop-ups) surprised you or challenged you the most this week.
  2. **AI Usage Critique:**
     * **[AI Prompt]:** Document the exact instruction you gave to the AI. (e.g., "Give me the CSS code for a Spotify brand theme with a dark background and bright green text for my HTML profile.")
     * **[AI Critique]:** Analyze the AI's response. Did it give you an incorrect color? Did it explain where to paste the code accurately? Were the selectors matching your actual HTML? 
     * **[Final Result]:** Attach a small screenshot of your final working code and the visual output in the browser.
* **Deadline:** 11:59 PM on the night before the next class.
