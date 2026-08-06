from pathlib import Path
from datetime import datetime

from sections.projects import get_project
from sections.skills import get_skills


def read_file(path):
    return Path(path).read_text(encoding="utf8")


def build_resume(company, role, p1, p2, skill):

    header = read_file("templates/header.tex")
    education = read_file("templates/education.tex")
    experience = read_file("templates/experience.tex")
    coding = read_file("templates/coding_profiles.tex")

    project1 = get_project(p1)
    project2 = get_project(p2)

    skills = get_skills(skill)

    template = read_file("templates/resume_template.tex")

    template = template.replace("{{HEADER}}", header)
    template = template.replace("{{EDUCATION}}", education)
    template = template.replace("{{EXPERIENCE}}", experience)
    template = template.replace("{{CODING}}", coding)
    template = template.replace("{{PROJECT1}}", project1)
    template = template.replace("{{PROJECT2}}", project2)
    template = template.replace("{{SKILLS}}", skills)

    output = Path("output/tex")
    output.mkdir(parents=True, exist_ok=True)

    tex_file = output / "resume.tex"

    tex_file.write_text(template, encoding="utf8")

    return tex_file