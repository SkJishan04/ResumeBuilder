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