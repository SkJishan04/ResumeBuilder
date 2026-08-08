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

# Installation

## 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ResumeBuilder
```

---

## 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Install Python dependencies

```powershell
pip install -r requirements.txt
```

The current project is intentionally lightweight and primarily uses Python's standard library.

---

## 4. Install MiKTeX

Install MiKTeX on your system and make sure `pdflatex` is available.

Verify:

```powershell
pdflatex --version
```

You should see the installed pdfTeX/MiKTeX version.

---

# Configuration

The LaTeX compiler path is configured in:

```text
config.py
```

Example:

```python
LATEX_COMPILER = r"C:\Users\<username>\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
```

If `pdflatex` is already available through the system PATH, the project can also use:

```python
LATEX_COMPILER = "pdflatex"
```

For portability, the compiler path should ideally be configurable rather than hard-coded to a specific user's Windows directory.

---

# Running the Application

Run:

```powershell
python main.py
```

You will see:

```text
============================================================
Resume Builder
============================================================

Company Name :
Job Role / ID :
```

Enter the company and role.

Then select two projects:

```text
Available Projects
----------------------------------------
1. AI PM Assistant (RAG)
2. Req2Arch
3. CNN Image Classification
4. Sentiment Analysis
5. Expense Tracker
6. Automated Transcription System
----------------------------------------

Select Project 1 :
```

Then select Project 2.

Finally select the technology profile:

```text
Available Skill Sets
----------------------------------------
1. AI / Machine Learning
2. LLM / Generative AI
3. Data Analytics
4. Full Stack
----------------------------------------

Select Technology Profile :
```

The application then generates and compiles the resume automatically.

---

# Example

Suppose the input is:

```text
Company Name : Google
Job Role / ID : ML-Engineer-01

Project 1 : AI PM Assistant (RAG)
Project 2 : CNN Image Classification

Technology Profile : AI / Machine Learning
```

The application creates a resume containing:

```text
Fixed Sections
    +
AI PM Assistant (RAG)
    +
CNN Image Classification
    +
AI / Machine Learning Technologies
```

and generates:

```text
Sk_Jishan_Google_ML-Engineer-01_2026-08-07.pdf
```

---

# Output

Generated LaTeX files are stored in:

```text
output/tex/
```

The generated PDF is stored in:

```text
output/pdf/
```

Example:

```text
output/
│
├── tex/
│   └── resume.tex
│
└── pdf/
    └── Sk_Jishan_Google_ML-Engineer-01_2026-08-07.pdf
```

---

# Adding a New Project

To add a new project:

### 1. Create the LaTeX file

For example:

```text
templates/projects/new_project.tex
```

### 2. Add it to `projects.py`

Add a new entry:

```python
PROJECTS = {
    1: "AI PM Assistant (RAG)",
    2: "Req2Arch",
    3: "CNN Image Classification",
    4: "Sentiment Analysis",
    5: "Expense Tracker",
    6: "Automated Transcription System",
    7: "New Project"
}
```

### 3. Add the corresponding `match/case`

```python
case 7:
    return load_tex("templates/projects/new_project.tex")
```

The new project will then become available from the terminal.

---

# Adding a New Technology Profile

The same approach can be used for technologies.

For example:

```text
templates/skills/cloud_devops.tex
```

Add it to the dictionary:

```python
SKILLS = {
    1: "AI / Machine Learning",
    2: "LLM / Generative AI",
    3: "Data Analytics",
    4: "Full Stack",
    5: "Cloud / DevOps"
}
```

Then add:

```python
case 5:
    return load_tex("templates/skills/cloud_devops.tex")
```

---

# Why This Approach?

The main goal of this project is to avoid manually editing a LaTeX resume for every job application.

Instead of repeatedly modifying:

```text
Projects
Skills
Technologies
```

the content is modularized.

For example:

```text
Job A
    ├── RAG
    ├── Req2Arch
    └── LLM Profile

Job B
    ├── CNN
    ├── Sentiment Analysis
    └── AI/ML Profile

Job C
    ├── Expense Tracker
    ├── Req2Arch
    └── Full Stack Profile
```

The core resume remains unchanged.

---

# Design Principles

The project intentionally keeps the first version simple.

### No database

Resume components are stored as `.tex` files.

### No frontend

The current interface is terminal-based.

### No LLM

Selections are currently manual.

### No external API

The application works locally.

### Modular LaTeX

Projects and technology profiles are independent files.

This makes the project easy to understand, maintain, and extend.

---

# Current Limitations

The current version requires manually selecting:

```text
Project 1
Project 2
Technology Profile
```

It also currently assumes that the user maintains the LaTeX content manually.

Other limitations include:

- No automatic job-description analysis
- No automatic project recommendation
- No GUI
- No duplicate-project prevention
- No ranking of projects based on job requirements
- Compiler configuration is currently machine-dependent
- Generated auxiliary LaTeX files may need cleanup

---


# Future Improvements

Possible future versions can introduce progressively more automation.

## Version 2 — Better CLI

Add:

- Input validation
- Prevent selecting the same project twice
- Better error handling
- Cleaner menus
- Automatic cleanup of temporary LaTeX files

---

## Version 3 — Job Description Matching

Allow the user to provide a job description:

```text
Enter Job Description:
```

The application could analyze keywords such as:

```text
Python
PyTorch
TensorFlow
RAG
LLM
SQL
Power BI
React
Django
Docker
AWS
```

and recommend:

```text
Project 1 → CNN
Project 2 → RAG
Technology → AI/ML
```

---

## Version 4 — LLM-Powered Resume Customization

An LLM could analyze:

```text
Job Description
        +
Available Projects
        +
Available Technology Profiles
```

and recommend the strongest combination.

For example:

```text
Job Description
       |
       v
   LLM Analysis
       |
       +----> Required Skills
       |
       +----> Recommended Projects
       |
       +----> Recommended Technology Profile
       |
       v
   Resume Builder
       |
       v
     PDF
```

---

## Version 5 — GUI

A graphical interface could replace the terminal:

```text
+---------------------------------------+
|          Resume Builder               |
+---------------------------------------+
| Company                               |
| [ Google                         ]    |
|                                       |
| Role / Job ID                         |
| [ ML Engineer                    ]    |
|                                       |
| Project 1                             |
| [ AI PM Assistant (RAG) ▼       ]    |
|                                       |
| Project 2                             |
| [ CNN Image Classification ▼    ]    |
|                                       |
| Technology Profile                    |
| [ AI / Machine Learning ▼        ]   |
|                                       |
|          [ Generate Resume ]          |
+---------------------------------------+
```

---

# Tech Stack

```text
Language
    Python

Resume Format
    LaTeX

Compiler
    pdfLaTeX

LaTeX Distribution
    MiKTeX

Interface
    Command Line / Terminal

File Handling
    Python pathlib

Compilation
    Python subprocess
```

---