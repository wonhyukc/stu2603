# Week 2 Handout: Introduction to HTML

**Instructor:** Wonhyuk William Chung (wonhyukc@stu.ac.kr)

Welcome to Week 2 of Web Programming! This week, we will learn the basics of HTML, which forms the skeleton of all websites. We will create our first web page: a digital business card.

---

## 1. Core Concepts Summary

HTML (HyperText Markup Language) is the standard markup language used to create web pages. It provides the structure of the page, much like a human skeleton.

### Essential HTML Structure

- `<html>`: The root element that wraps everything.
- `<head>`: Contains metadata, title, and invisible settings. (Like the brain: important but invisible.)
- `<body>`: Contains the visible content of the web page. (Everything the user actually sees.)

### Frequently Used Tags

| Tag | Description | Example |
|---|---|---|
| `<h1> ~ <h6>` | Headings. `<h1>` is the largest and most important. | `<h1>Hello</h1>` |
| `<p>` | A paragraph of text. | `<p>My name is ...</p>` |
| `<img>` | Inserts an image. **It has no closing tag** (empty tag). | `<img src="url">` |

### Image Paths: Absolute vs. Relative Paths

| Type | When to use | Example |
|---|---|---|
| **Absolute Path** | Link to an image on the internet | `https://example.com/photo.jpg` |
| **Relative Path** | Link to an image in the same folder | `./images/photo.jpg` |

> **Tip:** If there is a typo in the `src` URL, a broken image icon will appear. Always double-check your paths!

---

## 2. Lab Activity: Writing Your First HTML Code

During class, open **StackBlitz** (stackblitz.com) in your browser and follow along with the instructor's live coding demonstration. No separate installation is required.

### Step-by-Step Lab Guide

1. **Open StackBlitz:** Go to [stackblitz.com](https://stackblitz.com) and click "Blank Project" -> "Static (HTML/JS/CSS)".

2. **Examine the Basic Skeleton:** Open the `index.html` file. You can see the standard HTML structure (`<html>`, `<head>`, `<body>`).

3. **Add Content:** Inside the `<body>` tag, clear the existing content and enter your self-introduction. Make sure to include your **hobbies, good things about your hometown, and your computer experience**:
   ```html
   <h1>Hello, I am [Name]!</h1>
   <p>Welcome to my digital business card. I like [Hobbies], and my hometown is [Hometown], famous for [Attractions/Features]. I have [very little/some] experience using computers.</p>
   ```

4. **Add an Image:** Use the `<img>` tag to add your profile picture. Copy a desired image URL from the internet and paste it into the `src` attribute.
   ```html
   <img src="https://example.com/your-image.jpg" width="200">
   ```
   Since it's a homepage, it is public by default. Do not upload content that should not be shared publicly.

5. **Live Preview:** As you type your code, notice that the Preview panel on the right updates instantly! This is your very first web page.

6. **Learn Version Control with AI:** Ask AI to explain the following concepts and learn them: What are Git and GitHub, and why do we use them? What is a Commit? What is a Repository? What is the difference between Public and Private repositories? You don't need to understand everything today. You will use these like lifelong friends and continue to learn about them.
   
   Create a new git repo, different from the one you submitted as an assignment in Week 1. Let's name it `my-intro`. You must create a **Public** repo so others can evaluate it.

7. **Upload to GitHub:** Upload your HTML code to your newly created GitHub repository (`my-intro`). Double-check that your repository is set to **Public**.

8. **Submit for Peer Evaluation (Important):** 
   - Copy the link and hash of the commit you just uploaded.
      - Example Link: `https://github.com/wonhyukc/my-intro/blob/main/index.html`
      - Example Hash: `a06b10558bc9741a48f18819d0baf0dea9de9964`
   - Submit this text (Link and Hash) to the **[Week 2 Lab Assignment]** board on eCampus.
   - **Deadline:** You must submit before **March 20, 0:00**. Submissions will be closed after this time.

9. **Conduct Peer Evaluation:**
   - **Period:** March 20, 0:00 ~ March 22, 0:00
   - After the submission deadline, the instructor will announce a **Peer Evaluation Matching Table** and a **Google Form Link for Grading**.
   - Check the matching table and open the links of the 3 peers assigned to you.
   - Review their code and submit your grading scores via the provided Google Form based on the rubric (3 points: O/X).
   - **Warning:** You must complete the evaluations for all 3 assigned peers to receive your own participation points for peer evaluation.

---

## 3. Micro-Assignment

### Assignment 0.1: Summary of All Submissions

The submission should be about half an A4 page long. You do not need to write extensively. It must include the following items:

1. **Class Reflection**
   - Please write your thoughts on the class, suggestions, or any free comments.

2. **Attach Your Photo**
   - This is intended to help us remember you, so please attach a photo of yourself.
   - The file size of the photo should not exceed 500Kb. If the photo is too large, please reduce its size before sending. If you don't know how, google "how to reduce photo size" and learn how to do it yourself this time.
   - Name the photo file exactly with your name only (do not include your student ID or department). Example: `Wonhyuk.jpg`
   - Please use a photo that looks like you in real life. If it's overly photoshopped and your real face is unrecognizable, it will be hard to remember you later.

3. **Register Your Photo on eCampus**
   - Nowadays, many activities happen online. Staying completely anonymous there can often be disadvantageous. Even if you are introverted, please try to register it.
   - Furthermore, if the information registered on eCampus (especially your email address) is incorrect, please fix it. You don't need to make it public. (In your email, just write "Registration complete".)

4. **Experience with Chrome and AdBlock**
   - Install Chrome, log in, and try using it.
   - After that, install and use the AdBlock extension, and write your thoughts. (Make sure you verify the extension so you don't accidentally install a similar malicious extension.)

5. **Study Keyboard Shortcuts**
   - Search for Windows and Chrome keyboard shortcuts on your own, learn at least five of them, and write down the list and your thoughts.

6. **AI Usage Experience**
   - **AI Prompt:** Write the exact prompt you asked the AI. (e.g., *"What is git?"*)
   - **AI Critique:** Analyze the AI's response in one sentence. (e.g., *"The explanation was difficult, so I asked it to explain it more easily."*)   

---

### Micro-Assignment Submission Guide

This micro-assignment should be submitted via email.

- **Submit to:** `wonhyuk@stu.ac.kr`
- **Subject:** `Assignment 0.2 학번` (Example: `Assignment 0.2 20240001`)
- **⚠️ Warning:** Since emails are automatically filtered by code, if you do not follow the rules, your submission will be missed during grading. You must follow them. The subject line must contain ONLY "Assignment 0.2", one or more spaces, and your "Student ID". Do not include any other characters.
