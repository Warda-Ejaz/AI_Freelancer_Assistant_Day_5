🚀 AI Freelancer Assistant - Day 5

**A 5-Day End-to-End SaaS Application for Freelancers | Built with Python & Streamlit**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

### **📌 Project Overview**
AI Freelancer Assistant Pro is a comprehensive, all-in-one SaaS toolkit designed to automate and streamline a freelancer's entire workflow. From generating Fiverr/Upwork gigs to sending client replies and creating invoices, this app eliminates manual, repetitive tasks.

This project was built as the Capstone for the **Meta AI Freelancer Program 2026** over 5 days.


**📂 GitHub Repo**: [https://github.com/Warda-Ejaz/AI_Freelancer_Assistant_Day_5]

---

### **✨ Key Features - Day Wise Breakdown**

| Day | Module | Description | Tech |
| --- | --- | --- | --- |
| **Day 1** | **Business Dashboard** | Real-time analytics with KPIs: Gigs, Quotes, Invoices, AI Credits. Responsive UI with custom CSS. | Streamlit, session_state |
| **Day 2** | **AI Content Suite** | 1. Gig Generator with SEO Keywords + FAQs<br>2. Cover Letter Generator<br>3. Resume Builder with.txt export | Python, time.sleep for AI sim |
| **Day 3** | **Smart Pricing & Database** | Dynamic Pricing Calculator with Complexity/Urgency multipliers. Market comparison + AI pricing tips. Gig Database with Pandas search/filter. | Pandas, DataFrame |
| **Day 4** | **Client Communication** | AI Client Reply Generator with 3 tones. Invoice & Contract Generator with automatic tax calculation and FPDF export. | FPDF, re |
| **Day 5** | **History, Profile & Settings** | Centralized Document History for all modules. User Profile with Image Upload via PIL. Application Settings for Theme, Language, API Key. | PIL, session_state |

---

### **🛠️ Tech Stack**
- **Frontend/Backend**: Streamlit
- **Data Handling**: Pandas, session_state
- **PDF Generation**: FPDF
- **Image Handling**: Pillow (PIL)
- **Deployment**: Streamlit Community Cloud

---

### **🚀 How to Run Locally**

1. **Clone the repository**
    ```bash
    git clone [Your Repo Link]
    cd ai-freelancer-assistant
2. *Install dependencies*
    pip install streamlit pandas fpdf pillow
3. *Run the Streamlit app*
    streamlit run app.py
The app will open at `http://localhost:8501`.

---

### *🎯 What I Learned*
1. *State Management*: Mastered `st.session_state` for persistent, multi-tab data.
2. *Streamlit Rerun Logic*: Fixed widget errors by storing outputs in session_state and using `st.rerun()`.
3. *File I/O*: Implemented PDF and.txt generation and download.
4. *SaaS Architecture*: Built a scalable, multi-module application with a clean UX.

---

### *📈 Future Enhancements*
- [ ] OpenAI API integration for real AI generation
- [ ] User Authentication & Database with SQLite/Postgres
- [ ] Stripe Integration for actual invoicing
- [ ] Dark/Light Theme toggle functionality

---

### *👩‍💻 Author*
*Warda Ejaz*
 AI Freelancer Program | 2026
 wardaejaz039@gmail.com

*License*: This project is licensed under the MIT License.
