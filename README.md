# 💌 ColdMail-AI

**ColdMail-AI** is an LLM-powered web application that automatically generates personalized cold emails for job applications. Users simply input a job posting URL, and the app takes care of the rest — from scraping and cleaning the content to generating a tailored email with their LinkedIn profile included.

---

## 🧠 Overview

ColdMail-AI streamlines outreach in the job-hunting process by combining real-time web scraping, intelligent parsing, and LLM-based reasoning to understand job descriptions and generate context-aware emails.

### 🔍 Features

- ✅ Accepts job URL as input
- 🧼 Scrapes and cleans job posting content
- 🧠 Extracts role, skills, experience, and responsibilities
- ✉️ Generates a customized cold email aligned with the job post
- 🔗 Embeds user’s LinkedIn/profile link into the email

---

## 🏗️ System Architecture

```text
Job URL
   ↓
Web Scraper
   ↓
Text Cleaner (Regex)
   ↓
LangChain Pipeline
   ↓
LLM (Groq + LLaMA3)
   ↓
Tailored Cold Email
   ↓
Display via Streamlit
```

## 🛠️ Tech Stack
- Python  
- Streamlit  
- LangChain  
- Groq API (LLaMA3)  
- Regex (Text Preprocessing)

---
🖼️ Demo Preview

