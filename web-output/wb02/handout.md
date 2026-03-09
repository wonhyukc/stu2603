# Week 2 Handout: Introduction to HTML

**Instructor:** Wonhyuk William Chung (wonhyukc@stu.ac.kr)

Welcome to Week 2! This week, we will learn the basics of HTML, the skeleton of every website. You will build your very first web page—a personal digital business card.

---

## 1. Core Concepts Reference

HTML (HyperText Markup Language) is the standard markup language used to create web pages. It provides the structure of the page, much like the skeleton of the human body.

### Essential HTML Structure

- `<html>`: The root element that wraps everything.
- `<head>`: Contains metadata, title, and invisible settings (like the brain — important but not visible).
- `<body>`: Contains the visible content of your web page (everything users actually see).

### Commonly Used Tags

| Tag | Description | Example |
|---|---|---|
| `<h1> ~ <h6>` | Headings. `<h1>` is the largest, most important. | `<h1>Hello</h1>` |
| `<p>` | A paragraph of text. | `<p>My name is ...</p>` |
| `<img>` | Embeds an image. **No closing tag** (empty/self-closing tag). | `<img src="url">` |

### Image Paths: Absolute vs. Relative

| Type | When to Use | Example |
|---|---|---|
| **Absolute Path** | Link to an image on the internet | `https://example.com/photo.jpg` |
| **Relative Path** | Link to an image in the same folder | `./images/photo.jpg` |

> **Tip:** A typo in the `src` URL causes the dreaded broken image icon (the "X-box"). Always double-check your path!

---

## 2. Lab Section

During the class, open **StackBlitz** (stackblitz.com) in your browser and follow along with the instructor's live coding demonstrations — no installation required.

---

## 3. Micro-Assignment

**Task:** Create and modify the basic skeleton of your online digital business card using AI, and submit the results.

### Assignment Format

Your submission must fit within half an A4 page and include the following three parts:

1. **AI Prompt**
   - Exactly what you asked the AI.
   - Example: *"Please generate a basic HTML skeleton for my personal digital business card."*

2. **AI Critique**
   - Analyze the AI's response in one sentence. What is correct and what is annoying or wrong?
   - Example: *"The structure was well-organized, but there were too many unnecessary styling tags that made the code look complicated."*

3. **Final Result**
   - Delete or modify at least **one** tag from the AI's output. Take a screenshot of your final version running in StackBlitz.
   - Example: Remove a complicated `<h2>` or add your own `<img>` with a photo you chose.

### Deadline & Submission

- **Deadline:** 23:59 on the day before Week 3 class.
- **Where to submit:** Upload your assignment file (MS Word or PDF) to the **eCampus** "Week 2 Micro-Assignment" board.
- **Title format:** `[wb02] 학번_이름` (e.g., `[wb02] 20240001_홍길동`)
