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

### [Task A] eCampus Submission (Peer Evaluation)
* **Objective:** Submit your fully styled, brand-themed Online Business Card (Build-up Phase 3).
* **Submission Requirements:** 
  You must submit a text document or direct entry containing:
  1. The direct **Share URL** from StackBlitz. (Make sure your project is public or accessible via link).
  2. The link **MUST NOT return a 404 Error**. It must properly display your HTML/CSS code when clicked.
* **Where to Submit:** eCampus "Week 5 Assignment" Board.
* **Peer Evaluation Rule:** You will be assigned another student's submission. You must award 1 point for a valid URL format, 1 point for an accessible link/hash, and 1 point if the page loads correctly without an error.

### [Task B] Email Submission (Self-Reflection & AI Critique)
* **Email Title Format:** `Assignment0.5 20240001` (Replace with your actual student ID. Failure to use this exact format will result in a 0 score as the automatic email filter will skip your submission).
* **Where to Submit:** `wonhyukc@stu.ac.kr`
* **Content Guidelines (Approx. half an A4 page as email body):**
  1. **[AI Prompt]:** Ask an AI to generate CSS code that changes your HTML online business card to match your favorite brand's HEX colors. Provide the exact text prompt you used. (e.g., "Give me the CSS code for a Spotify brand theme with a dark background and bright green text for my HTML profile.")
  2. **[AI Critique]:** Analyze the AI's response. Did it give you an incorrect color? Did it explain where to paste the code accurately? Were the selectors matching your actual HTML? Did it make a mistake regarding inheritance?
  3. **[Final Result]:** Attach a small screenshot of your final working code and the visual output in the browser.
* **Deadline:** 11:59 PM on the night before the next class.
