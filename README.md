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

## 3. Project & Technology Selection

`sections/projects.py`

Contains the available projects and maps each selection to a LaTeX file.

Current projects:

```text
1. AI PM Assistant (RAG)
2. Req2Arch
3. CNN Image Classification
4. Sentiment Analysis
5. Expense Tracker
6. Automated Transcription System
```

---

`sections/skills.py`

Contains the available technology profiles.

Current profiles:

```text
1. AI / Machine Learning
2. LLM / Generative AI
3. Data Analytics
4. Full Stack
```

The project uses Python `match/case` to map selections to the corresponding `.tex` files.

---

## 4. LaTeX Compiler

`compiler.py`

Responsible for:

- Calling `pdflatex`
- Creating the PDF
- Creating the output directory
- Generating the final filename
- Adding company, role/job ID, and date to the filename

The compiler used by this project is:

```text
MiKTeX + pdfLaTeX
```

---

# LaTeX Template Design

The main template acts as the skeleton of the resume.

Conceptually:

```latex
\documentclass[...]

{{PREAMBLE}}

\begin{document}

{{HEADER}}

{{EDUCATION}}

{{EXPERIENCE}}

{{CODING_PROFILES}}

{{PROJECTS}}

{{TECHNOLOGIES}}

\end{document}
```

The Python application replaces these placeholders with the appropriate `.tex` content.

This allows the fixed resume structure to remain unchanged while projects and technology profiles can be swapped dynamically.

---

# Fixed vs Dynamic Content

## Fixed Sections

These sections remain the same for every generated resume:

```text
Header
Education
Experience
Coding Profiles
```

They are stored separately as:

```text
header.tex
education.tex
experience.tex
coding_profiles.tex
```

---

## Dynamic Sections

These sections change according to the job:

```text
Projects
Technology Profile
```

Projects are stored individually:

```text
projects/
├── rag.tex
├── req2arch.tex
├── cnn.tex
├── sentiment.tex
├── expense_tracker.tex
└── transcription.tex
```

Technology profiles are also stored individually:

```text
skills/
├── aiml.tex
├── llm.tex
├── data_analytics.tex
└── fullstack.tex
```

This makes it easy to add or modify content without changing the core Python application.

---

# Requirements

## Software

You need:

- Python 3.x
- MiKTeX
- pdfLaTeX

The Python program uses the local `pdflatex.exe` executable to compile the generated `.tex` file.

---

