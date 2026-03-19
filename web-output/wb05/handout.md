# Week 5: CSS Box Model & Layouts

## 1. Concept Reference Guide

Welcome to Week 5! Every HTML element is effectively a rectangular box. CSS manages these boxes using what we call the **Box Model**. Understanding the box model is crucial to positioning elements and creating well-structured web layouts.

### The CSS Box Model Anatomy
Think of a framed picture hanging on a wall. The Box Model works exactly like that:
* **Content:** The actual photo. (Text, images, etc.)
* **Padding:** The white space inside the frame, between the photo and the frame itself.
* **Border:** The wooden frame itself.
* **Margin:** The empty wall space around the outside of the frame, keeping it apart from other frames.

### Key CSS Properties
* `margin`: Pushes other elements away. Values can be pixels (`10px`), percentages (`5%`), or `auto` (often used to center block elements).
* `padding`: Expands the space inside the element, pushing the content inward.
* `border`: Adds a visible line around the padding and content. Example: `border: 1px solid black;`
* `width` & `height`: By default, this only defines the *content* area. Adding padding or borders will make the overall box larger.
* `box-sizing: border-box;`: A pro-tip property that forces the browser to calculate the width/height including the padding and border, preventing unexpected layout expansions.

*Remember: "Margin Collapsing" happens when two vertical margins touch. Instead of adding together, the browser only uses the larger margin!*

## 2. Lab Assignment

In this week's lab, you will expand the online business card you built previously to make it look much more spacious and professional using the Box Model.

**Instructions:**
Please open your **StackBlitz** project from the previous week and follow the instructor's live demonstration to apply the Box Model concepts.

**Submission Process:**
* Complete the lab on StackBlitz.
* Take a screenshot of your result and copy the StackBlitz URL.
* Submit both on **eCampus** for the Week 5 Lab Assignment.
* *Do not forget to participate in the Peer Review process after submitting your own work!*

## 3. Micro-Assignment (0.x 과제)

**Tasks to complete for your email submission:**
1. **Class Reflection:** Write a short paragraph (3-4 sentences) about what you learned this week. Was the Box Model confusing at first? 
2. **Additional Practice:** Add a small `div` that acts as a "Badge" (like "New" or "Pro") purely using `padding`, `background-color`, and `border-radius`, then position it with `margin`.
3. **AI Collaboration (Prompt / Critique / Result):**
   * **Prompt:** Ask your AI: "Please explain the difference between margin and padding in CSS to a 10-year-old."
   * **Critique:** Read the AI's explanation. Was it helpful? Did it use a good analogy (like the picture frame or winter coat)? 
   * **Result:** Provide a screenshot or copy-paste the AI's answer.

**How to Submit:**
* Send an email to **wonhyukc@stu.ac.kr**.
* **CRITICAL:** The subject line must be exactly `과제0.5 [Your Student ID]` (e.g., `과제0.5 20240001`).
* **Deadline:** Please submit before the next class.
* Include your reflection, practice proof, and AI critique in the body of the email.
