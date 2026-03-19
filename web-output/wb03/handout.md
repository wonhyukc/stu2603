# Week 3 Handout: Input Forms Basics

**Instructor:** Wonhyuk William Chung (wonhyukc@stu.ac.kr)

Welcome to Week 3 of Web Programming! Last week, we built a digital business card. This week, we will make our website interactive by adding an "Input Form" so that visitors can leave messages.

---

## 1. Core Concepts Summary

An HTML Form is a section of a document containing interactive controls to submit information. It is like a digital questionnaire or survey.

### Essential Form Tags

- `<form>`: The container for all input fields. It defines where the data will be sent.
- `<input>`: The most commonly used form control. Its appearance changes based on the `type` attribute.
- `<textarea>`: A multi-line text input field, perfect for longer messages.
- `<button>`: A clickable button used to submit the form data.
- `<label>`: A text label bound to a specific input field to improve usability and accessibility.

### Frequently Used Input Types

| Input Code | Description | Appearance |
|---|---|---|
| `<input type="text">` | Default single-line text field. | A normal text box. |
| `<input type="password">` | Masks characters (e.g., dots or asterisks). | `••••••••` |
| `<input type="email">` | Built-in email validation. Requires an `@`. | Email format box. |
| `<input type="date">` | Pops up a calendar for a date selection. | Calendar widget. |

> **Tip:** When you click a `<button type="submit">` inside a form, the browser's default behavior is to refresh the page and send the data. This is normal!

---

## 2. Lab Activity: Building a Guestbook Form

During class, open **StackBlitz** and resume working on the `my-intro` repository you created last week. We will keep building upon it!

### Step-by-Step Lab Guide

1. **Open Your Project:** Go to StackBlitz, connect to your GitHub, and open the `my-intro` branch from last week.
2. **Setup the Form Container:** Below your profile picture and biography, add a heading and a `<form>` tag.
   ```html
   <hr>
   <h2>Leave a Message</h2>
   <form>
     <!-- Inputs will go here -->
   </form>
   ```
3. **Add Input Fields:** Add fields for the visitor's name, their email, and a message. Use `<label>` tags so users know what to type.
   ```html
   <label>Name:</label>
   <input type="text" placeholder="Your Name"><br><br>

   <label>Email:</label>
   <input type="email" placeholder="you@domain.com"><br><br>

   <label>Message:</label><br>
   <textarea rows="4" cols="30" placeholder="Say hello!"></textarea><br><br>
   ```
4. **Add a Submit Button:** Inside the form, add a button.
   ```html
   <button type="submit">Send Message</button>
   ```
5. **Test Your Form:** Try entering a generic word (like "hello") into the email field and hit submit. Notice the built-in warning bubble? That is the power of `type="email"`.
6. **Upload to GitHub:** Upload today's progress to your GitHub repository.
7. **Submit for Peer Evaluation (Important):**
   - Copy the GitHub file link and commit hash of today's work.
   - Submit this text to the **[Week 3 Lab Assignment]** board on eCampus.
   - **Deadline:** Check eCampus for the strict deadline. Late submissions are not accepted.
8. **Conduct Peer Evaluation:**
   - After the deadline, the instructor will provide a Peer Evaluation form. Review the code of your assigned peers and score them using the rubric criteria.

---

## 3. Micro-Assignment

### Assignment 0.3: Form Building and AI Collaboration

Submit your assignment via email following the exact format. Keep your writing concise (half an A4 page).

1. **Class Reflection**
   - Write your thoughts on the Week 3 class: What was the most interesting part of building forms?

2. **AI Assistance for Forms**
   - Use an AI (ChatGPT or Gemini) to generate a customized contact form for your specific hobby or interest (e.g., a form to book a tennis game, a form to order custom coffee).
   - Apply the AI's code to your StackBlitz project and take a screenshot of the working form. Attach this screenshot.

3. **Form Validation AI Critique**
   - Experiment: Change the input type in the AI's code to `<input type="email">`. Try submitting the form by typing just regular text instead of an email address.
   - Take a screenshot of the warning message the browser shows. Attach it.

4. **AI Usage Experience**
   - **AI Prompt:** "Write a short HTML form for booking a [your hobby] session."
   - **AI Critique:** Evaluate the form the AI provided. Did it use the right input types? Was there a mistake? Write one sentence of critique.

---

### Micro-Assignment Submission Guide

- **Submit to:** `wonhyukc@stu.ac.kr`
- **Subject:** `과제0.3 학번` (Example: `과제0.3 20240001`)
- **⚠️ Warning:** Do not add spaces un-necessarily or any extra words in the subject line! Automated email filters will miss your homework if you fail to strictly follow the `과제0.3 학번` format.
