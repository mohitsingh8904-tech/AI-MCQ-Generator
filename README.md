#  AI MCQ Generator

An AI-powered web application that automatically generates Multiple Choice Questions (MCQs) from PDF notes using Natural Language Processing (NLP). Users can upload study notes, generate quizzes, attempt tests, and track their performance.

---

##  Project Overview

AI MCQ Generator is a Django-based web application that converts PDF notes into interactive quizzes. The application extracts text from uploaded PDFs, processes it using NLP techniques, generates MCQs, evaluates user responses, and stores quiz history.

---

##  Features

- User Registration & Login
- Upload PDF Notes
- Automatic Text Extraction
- AI-Based MCQ Generation
- Interactive Quiz System
- Instant Score Calculation
- Quiz History
- Download Quiz Result as PDF

---

##  Tech Stack

**Backend**
- Django
- Python

**Frontend**
- HTML
- CSS
- JavaScript

**AI & NLP**
- Hugging Face FLAN-T5
- NLTK
- Scikit-learn (TF-IDF)

**Database**
- SQLite

---

## Project Structure

```text
student_notes_mcq_ai/
├── blog/
├── mcq_app/
├── media/
├── static/
├── templates/
├── student_notes_mcq_ai/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/mohitsingh8904-tech/AI-MCQ-Generator.git
```

Go to the project directory

```bash
cd student_notes_mcq_ai
```

Install the required packages

```bash
pip install -r requirements.txt
```

Apply database migrations

```bash
python manage.py migrate
```

Run the project

```bash
python manage.py runserver
```

Open your browser

```text
http://127.0.0.1:8000/
```

---

## Future Scope

- Integration with Gemini/OpenAI APIs
- Difficulty Level Selection
- Subject-wise Question Generation
- Timer-Based Quiz
- Cloud Deployment
- Performance Analytics Dashboard

---


Mohit singh chandawat

- B.Tech Computer Science Engineering
- Sangam University
- Email: ms8904794@gmail.com
- GitHub: https://github.com/mohitsingh8904-tech
