# Resume Builder

A lightweight Python-based resume automation tool that generates **job-specific PDF resumes** from a reusable LaTeX template.

Instead of manually editing a resume for every job application, this project allows you to select the company, role/job ID, projects, and technology profile from the terminal. The application then combines the selected components with your fixed resume sections and automatically compiles the final LaTeX document into a PDF.

---

## Overview

Applying to multiple jobs often requires changing the resume according to the requirements of each position.

For example:

- An **AI/ML** position may require CNN, machine learning, and deep learning projects.
- An **LLM/Generative AI** position may require RAG, LLM, and GenAI projects.
- A **Data Analytics** position may require analytics-oriented projects and technologies.
- A **Full Stack** position may require web-development projects and technologies.

The education, experience, and coding-profile sections of the resume generally remain unchanged.

This project separates the resume into:

- Fixed sections
- Selectable projects
- Selectable technology profiles
- A reusable LaTeX template

The Python program combines these components and produces a job-specific PDF.

---
## Features

- Generate a customized resume from the terminal
- Select two projects dynamically
- Select a technology/skill profile dynamically
- Keep education, experience, and coding profiles unchanged
- Store projects as separate `.tex` files
- Store technology profiles as separate `.tex` files
- Use a reusable LaTeX template
- Automatically compile LaTeX using `pdflatex`
- Automatically generate a dated PDF filename
- Keep generated `.tex` and `.pdf` files organized
- Easily add new projects and technology profiles

---

## Current Workflow

```text
                    Resume Builder
                          |
                          v
                Enter Company Name
                          |
                          v
                  Enter Job Role / ID
                          |
                          v
                  Select Project 1
                          |
                          v
                  Select Project 2
                          |
                          v
              Select Technology Profile
                          |
                          v
                  Build resume.tex
                          |
                          v
                    pdflatex
                          |
                          v
                    Resume PDF
```

The generated filename follows:

```text
<NAME>_<COMPANY>_<ROLE>_<DATE>.pdf
```

For example:

```text
Sk_Jishan_abc_abc123_2026-08-07.pdf
```

---

# Project Structure

```text
ResumeBuilder/
│
├── main.py
├── builder.py
├── compiler.py
├── config.py
├── requirements.txt
├── README.md
│
├── sections/
│   ├── projects.py
│   └── skills.py
│
├── templates/
│   ├── resume_template.tex
│   ├── preamble.tex
│   ├── header.tex
│   ├── education.tex
│   ├── experience.tex
│   ├── coding_profiles.tex
│   │
│   ├── projects/
│   │   ├── rag.tex
│   │   ├── req2arch.tex
│   │   ├── cnn.tex
│   │   ├── sentiment.tex
│   │   ├── expense_tracker.tex
│   │   └── transcription.tex
│   │
│   └── skills/
│       ├── aiml.tex
│       ├── llm.tex
│       ├── data_analytics.tex
│       └── fullstack.tex
│
└── output/
    ├── tex/
    │   └── resume.tex
    │
    └── pdf/
        └── generated_resume.pdf
```

---
# Architecture

The project has four main layers.

## 1. User Interface

`main.py`

Responsible for:

- Taking user input
- Displaying available projects
- Displaying available technology profiles
- Passing selections to the builder
- Starting PDF compilation

---

## 2. Resume Builder

`builder.py`

Responsible for:

- Loading the master LaTeX template
- Loading fixed resume sections
- Loading selected projects
- Loading the selected technology profile
- Replacing placeholders
- Creating the final `resume.tex`

Conceptually:

```text
resume_template.tex
        |
        +── header.tex
        |
        +── education.tex
        |
        +── experience.tex
        |
        +── coding_profiles.tex
        |
        +── selected project 1
        |
        +── selected project 2
        |
        +── selected technology profile
        |
        v
    resume.tex
```

---