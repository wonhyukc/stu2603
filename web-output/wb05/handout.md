# Web Programming (E-Track) Week 5 Handout: CSS Basics & Survival Skills

Welcome to Week 5! This week, we breathe life and color into our structural HTML skeletons using CSS.

## 1. Concept Reference Area

### 📍 What is CSS?
HTML provides the bare content and structural "bones" of a webpage. **CSS (Cascading Style Sheets)** is the "interior design" tool that coats those bones with colors, layouts, and beautiful visual decorations.

### 🎨 Three Ways to Apply CSS
1. **Inline Style:** Writing directly inside the HTML tag (e.g., `<h1 style="color: red;">`). Avoid using this unless absolutely necessary.
2. **Internal Style:** Wrapping styles inside a `<style>` block located within the `<head>` section of the HTML file.
3. **External Style:** Creating a completely separate file like `style.css` to manage all styling like a centralized wardrobe. (This is the industry standard).

### 🎯 Selectors: "Who should wear this outfit?"
* **Element Selector:** Selects all tags of that type universally (e.g., `p`, `h1`).
* **Class Selector (`.`):** Groups multiple elements under a specific name (e.g., `.box`, `.profile-img`). Think of it as a team uniform.
* **ID Selector (`#`):** A unique, one-of-a-kind name for a single element on the page (e.g., `#main-header`). Do not reuse an ID.

### 🐛 Mental Model for Survival (Communicating with Errors & Inheritance)
* **CSS Inheritance**: Sometimes, if you style a parent element (like `<body>`), all the child elements naturally inherit that font or color. Be extremely aware of this when debugging!
* **NEVER instantly click "X" on error pop-ups!** An error message is a frantic SOS signal from the computer asking for your help.
* The absolute fundamental skill is to naturally highlight the error text, copy it, and paste it into Google or an AI to ask for the root cause. Do not panic!

### ⌨️ Magical Universal Keyboard Shortcuts [Special Training]
* **`Ctrl + A` (Cmd + A)** : Select All.
* **`Ctrl + C / V / X`** : Copy / Paste / Cut.
* **`Ctrl + Z`** : Undo. (The ultimate time machine!).
* **`Ctrl + F` / `Ctrl + H`** : Find / Replace text.
* **`Ctrl + Shift + T`** : Resurrect the browser tab you accidentally closed a second ago.

### 💻 Chrome Survival Setup [Special Training]
* Automatic translation of foreign sites inside Chrome settings.
* **Incognito Mode** (`Ctrl + Shift + N`): Mandatory for public library PCs.
* Mobile to PC syncing via official Google accounts.

---

## 2. Lab Section

This week's lab will exclusively take place on your browser, requiring no local installations. This exercise is designed to take at least **25 minutes** of deep focus. 
For clear instructions, assignment terminology and submission methods are newly classified into two types:
* **Assignment**: The main lab exercise based on class content, submitted via Google Form, followed by peer evaluation between students.
* **Microassignment**: A simple sub-assignment submitted via email according to a designated format, same as the previous 0.x assignments.


**Platform:** **StackBlitz**

**Step-by-Step Instructions:**
1. **Open your StackBlitz Project:**
   Access the previous week's 'Online Business Card' project URL that you saved. Make sure you can see both `index.html` and `style.css` in the file explorer.
2. **Connect the External CSS:**
   Ensure your HTML `<head>` has the `<link rel="stylesheet" href="style.css">` tag connecting it to your wardrobe. 
3. **Brand Color Transformation (10 mins):**
   Choose your favorite global brand (e.g., Apple, Starbucks, Netflix). Use a search engine or an AI tool to find the exact HEX color codes associated with that brand. Apply those HEX colors to the `background-color` and text `color` properties in your `style.css` file to see real-time updates.
4. **Selector Practice (10 mins):**
   Assign a unique ID (`id="profile-name"`) to your name tag and a Class (`class="card-info"`) to your contact details. Target them appropriately in your CSS using `#` and `.` respectively. Change their `font-size` and `font-family`.
5. **Survival Keyboard Training (5 mins):**
   Open a "New Incognito Window" in Google Chrome (`Ctrl + Shift + N`). Understand that no login session or browsing history is preserved here. Close the tab, and aggressively practice the `Ctrl + Shift + T` shortcut to see if it restores the incognito tab (Spoiler: It won't, to protect privacy. Try it on normal tabs). Deliberately use `Ctrl + C`, `V`, and `Z` repeatedly inside your code editor to develop muscle memory.

---

## 3. Homework Section

You have two mandatory submissions for this week. Please carefully follow the instructions below.

### Assignment: Google Form Submission via GitHub (Peer Evaluation)
* **Deadline:** Every Friday by Midnight (23:59)
* **Objective:** Submit your fully styled, brand-themed Online Business Card (Build-up Phase 3) using GitHub, along with your personal shortcut keys document.
* **Submission Requirements:** 
  Instead of StackBlitz or eCampus, we are now migrating to the global standard: **GitHub**.
  1. **Personal Shortcut Keys Google Doc**: Create a Google Doc containing a list of your personal essential shortcut keys **(including at least 5 new Windows shortcut keys and 5 new Chrome shortcut keys that you did not know before)**. Set the share permissions exactly to **'Anyone with the link can view'** and copy the link. (You must grant read permission. Verify it yourself by opening the link in Incognito mode to ensure it is readable.)
  2. Create a **Public Repository** on your GitHub account for Week 5.
  3. Upload/Commit your HTML and CSS files to this repository. Please make sure to include your **Google Doc Link** inside your repository (e.g., inside a `README.md` file or as an HTML comment).
  4. Copy your latest **Commit Hash** (the unique alphanumeric code representing your commit).
* **Where to Submit:** 
  Submit your **Repository Link** and **Commit Hash** to the **designated Google Form** (link provided in class/eCampus). 
  *Note: The time of your Google Form submission is strictly recorded. If your Commit Hash does not exist in the repo or if you overwrite it after the deadline, it will be considered assignment manipulation and will result in a 0 score.*
* **Assignment Acknowledgment:** 
  To indicate that you have read this assignment, enter 1 in the `homework 05 ping` column of the Google Sheet.
* **Peer Evaluation Rule:** You will be assigned another student's submission. You must evaluate if their GitHub link is accessible, verify their webpage properly loads without errors, find their Commit Hash, and check if their Google Doc link is accessible.

### Microassignment 0.5: Email Submission 
* **Deadline:** Every Friday by Midnight (23:59)
* **Email Title Format:** `Assignment0.5 20240001` (Replace with your actual student ID. The number of spaces before the student ID does not matter. **Do not add any other words to the title and submit exactly like this. This rule must be strictly followed.** Failure to use this format exactly will result in a 0 score as the automatic email filter will skip your submission).
* **Where to Submit:** `wonhyukc@stu.ac.kr`
* **Content Guidelines:**

### 1. Class Reflection

Write your thoughts on the class in 3 lines or less.

---

### 2. Campus Exploration

Explore every corner of the campus. Visit two places you haven't been to before, spend at least 5 minutes there, and write down where you went in the body of your email.

---

### 3. Pomodoro Technique Practice

Search for GTD (Getting Things Done) and the Pomodoro Technique, and actually try using a Pomodoro timer. Briefly describe how it felt.

---

### 4. Hour of Code Certificate

Complete the 'Hour of Code' and take a photo of yourself with your certificate (containing your name) displayed on the monitor, then attach it to the email.

---

### 5. 30-Day Challenge Resolution

Watch the TED talk 'Matt Cutts: Try something new for 30 days' and write down your own 30-day challenge resolution.

---

### 6. English Typing Practice

Continue the English typing practice you did in last week's Assignment 0.4 for at least 5 more minutes. Enter your measured results in the `0.5 type: word per min` column of the Google Sheet.

---

### 7. Advanced Learning (Optional)

If the above assignments are too easy for your level, independently find the next suitable topic for this course and study it with Gemini. Write down what you studied in 3 lines or less in the body of your email.
