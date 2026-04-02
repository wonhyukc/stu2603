---
marp: true
theme: default
class: lead
---

# Week 06: Box Model & Information Hunter
## Foundations of CSS Layout & Data Structuring
**Web Programming (E-Track)**

---

# 📌 Core Learning Objectives

- **The Box Model Mastery**: Understand the physical structure of Margin, Border, and Padding.
- **Precision Spacing**: Control element intervals and "Social Distancing" (White space).
- **Information Hunter**: Use advanced Google Search operators to find answers in 1 second.
- **Data Analysis Expertise**: Summarize multi-dimensional data using Pivot Tables.

---

# 📦 Everything on the Web is a "Box"
### Break Your Stereotypes
- Round buttons, sharp logos—all are **rectangular boxes** to the computer.
- The arrangement of these boxes is what we call **Layout** design.
- **[Content] - [Padding] - [Border] - [Margin]**

---

# 🚚 The Delivery Box Analogy

1. **Content**: The actual item you ordered (Text, Image).
2. **Padding**: The **Bubble Wrap** inside the box (Space between content and box wall).
3. **Border**: The **Cardboard Box** itself (The boundary line and thickness).
4. **Margin**: **Social Distancing** from the next-door box (Space outside the border).

---

# 🕵️ Expert's Secret Tool: Developer Tools (F12)

### "Why doesn't it look like I intended?"
- **Inspect**: Hover to see color-coded areas.
- **Blue**: Content / **Green**: Padding (Bubble wrap) / **Orange**: Margin (Social distancing).
- **Computed Tab**: Verify the final box dimensions calculated by the browser.

---

# ✨ Layout Solver: `border-box`

- Solve the problem where the box keeps growing when adding padding or borders.
- **`box-sizing: border-box;`**
- Forces the border and padding to be included *inside* the defined width.
- **Essential declaration for all web developers (`* { box-sizing: border-box; }`)**

---

# 🛡️ [Special] Information Hunter: Advanced Google (1)
### Exclusion Operator: `-` (Minus)
- Exclude unnecessary words from search results.
- Useful for filtering out ads or click-bait.
- **Example**: `CSS Box Model -ads -shopping`

---

# 🛡️ [Special] Information Hunter: Advanced Google (2)
### Source Operator: `site:`
- Search only within a specific site or domain.
- Extract data from official docs or reliable communities.
- **Example**: `box-sizing site:developer.mozilla.org`

---

# 🛡️ [Special] Information Hunter: Advanced Google (3)
### File Operator: `filetype:`
- Search only for specific file extensions.
- Absolute tool for finding original PDF reports or research.
- **Example**: `web design trend 2024 filetype:pdf` 

---

# 💡 [Special] Data Hunting: Importing External Data

1. **Plain Web Table Copy**: `Ctrl+Shift+V` (Paste Values Only).
   - Extract pure data by removing messy formatting (colors, fonts) from websites.
2. **CSV File Import**: Convert massive data chunks.
   - **[File] - [Import] - [Upload]**
   - Comma-separated data is split like magic! (Separator: 'Detect automatically').
3. **Excel (.xlsx) Compatibility**: Upload to Google Drive and **[Open with Google Sheets]**.

---

# 🏗️ Data at a Glance: Structuring

### Use `Freeze Panes`
- Lock the 1st row (the Header) of your data.
- **[View] - [Freeze] - [1 Row]**
- Don't lose track of which column is which, even when scrolling through thousands of rows.

---

# 🔍 Visual Sorting Step 1: Sorting

- Rearrange random data based on specific criteria.
- Click Column Header (A, B, C) ➡️ **Sort Sheet**.
  - `Ascending (A-Z)`: Smallest to Largest.
  - `Descending (Z-A)`: Largest to Smallest.
- Build a leaderboard structure in seconds.

---

# 🎨 Visual Sorting Step 2: Conditional Formatting

### Data that Speaks with Color
- Select Range ➡️ **[Format] - [Conditional formatting] - [Color Scale]**.
- Apply gradients like a thermal camera based on the values.
- Implement stunning **Data Visualization** without a single line of syntax!

---

# ✨ Smart Pre-processing: Flash Fill (Auto-fill)
- Quickly pick out desired patterns from a massive bunch of text.
- Type the pattern manually in the next cell about 3 times; the sheet identifies the pattern and previews the rest in gray (**Press Enter to auto-fill!**).

---

# 📊 Pivot Table Analysis Foundations

### Summarize Data with a Few Clicks
- **[Insert] - [Pivot table]** ➡️ 'New Sheet'.
- Derive sum, average, or median of huge data instantly without complex math functions.
- **How-to**: Add data to 'Values' area and change criteria (Count ➡️ Average).

---

# 🧩 Completing Cross-Tabulation (Advanced Pivot)

### Multi-dimensional Comparison Analysis
- Intersection of Rows and Values to discover new insights.
- **Example**: Sales by Gender/Region or Market Share by Browser.
- ➡️ Realistic Cross-Analysis Table Completed!

---

# 🏗️ [Build-up] Mission: Polishing Your Card

1. **Load Previous Project**: Open your final code from Week 05 in StackBlitz.
2. **Visualize Box**: Add a `border` to the `.card` element to see the box.
3. **Add Breathing Space**: Use `padding` to let the content breathe.
4. **Align Buttons**: Separate stuck buttons using `margin-right`.
5. **Data Hunter Mission**: Use Google operators to find original data, and create a "Data Map" in Google Sheets using **Sort/Conditional Formatting/Pivot Tables**.

---

# Wrap-up (Q&A)

- **Box Model**: The most powerful physical foundation of web design.
- **Debugging**: Trust the Developer Tools, not just your eyes.
- **Data Analysis**: The skill to turn "hunted" data into knowledge in a sea of information.

**"Now, breathe life into your business card and data like a pro!"**
