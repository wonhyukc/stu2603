---
marp: true
theme: default
paginate: true
---

# Web Programming - Week 07
## Flexbox Principles & Layout Refactoring

**Instructor**: Wonhyuk William Chung

---

## [S1] Building the Block: HTML & CSS Journey

- **Past 6 Weeks**: We built the skeleton (HTML), painted it (CSS), and managed spacing (Box Model).
- **The Problem**: Have you ever tried to place boxes side-by-side, but they keep dropping to the next line? 
- Normal CSS flow stacks block elements vertically by default (heavy at the bottom, light on top).

---

## The Magic Spell: `display: flex`

- **Flexbox**: A powerful layout model that allows you to position elements freely.
- Meet the **"Alignment Manager"**.
- Allows alignment in horizontal rows, vertical columns, or perfectly spaced configurations without manually calculating pixels!

---

## Core Property 1: `flex-direction`

Determines the primary axis of alignment.

- `flex-direction: row;` (Default)
  - Elements are arranged horizontally from left to right.
  - Essential for Navigation Menu bars!
- `flex-direction: column;`
  - Elements are stacked vertically.
  - Often used for mobile phone layouts.

---

## Core Property 2: `justify-content`

Determines how elements are distributed along the **Main Axis** (Horizontal for `row`).

- `center`: Pushes everything to the middle.
- `space-between`: First and last items touch the edges; equal space between the rest.
- `space-around`: Equal space on both the left and right sides of every element. 

---

## Core Property 3: `align-items`

Determines how elements align along the **Cross Axis** (Vertical).

- `center`: Perfectly centers items vertically.
- `flex-start`: Aligns items to the top "ceiling".
- `baseline`: Aligns the bottom of the text (crucial for typography!).

---

## ⚠️ The Golden Rule of Flexbox

**Flexbox operates strictly on a Parent-Child relationship.**

- **DO**: Always declare `display: flex;` on the **Parent Container**.
- **DON'T**: Declare it on the child element itself (unless you want its inner contents to be a flex layout).
- Remember: `display: flex` goes to the "Mother" of the items you wish to align!

---

## [S2] Flexbox Lab: Live Demo

Let's move to **`lecture-demo/index.html`**

- **Observe the 4 Core Properties** in action.
- Changing `flex-direction` (`row` ↔ `column`).
- Introducing **`flex-wrap`**:
  - `nowrap` (squashes items to fit one line).
  - `wrap` (naturally moves items to the next line when space runs out).
- *This is the foundation of modern Responsive Web Design!*

---

## [S3] Layout Refactoring

Code doesn't always behave the way we expect.

- **What is Refactoring?**
  - Restructuring the code in a better way, while keeping it functional.
  - Fixing existing "spaghetti" code into clean code.
- Often, more time is spent *reading/fixing* code than writing new code!

---

## The Doctor's Stethoscope: Developer Tools

When a layout breaks, stop guessing and deleting code blindly.

- Press **F12** to open the Browser Developer Tools.
- **Left Panel (DOM Tree)**: The HTML structure.
- **Right Panel (Styles)**: The real-time CSS applied.
- The Inspector tool highlights the exact element causing the problem.

---

## Diagnosing & Fixing Overflow 

**The Bug**: An image piercing through the parent container's layout.
**The Cause**: The child image is restricted to a massive fixed width (e.g. `width: 1000px;`), ignoring the parent's flexibility.

**The Fix**:
```css
.profile-img-buggy {
    /* Remove the fixed pixel width! */
    max-width: 100%;
    height: auto;
}
```

---

## Debugging Best Practice

- **Modifications in Developer Tools are temporary!**
  - If you refresh, they vanish.
- **The Workflow**:
  1. Check and tweak within the Developer Tools.
  2. If it works, copy the styles to your actual CSS file.
  3. Save.

---

## Summary

1. Use **Flexbox** for layout mastery (`flex-direction`, `justify-content`, `align-items`, `flex-wrap`).
2. Apply `display: flex;` strictly to the Parent.
3. Do not just delete broken code. Use **Developer Tools (F12)** to diagnose issues.
4. Replace rigid pixel widths with `max-width: 100%` and `height: auto` for images.
