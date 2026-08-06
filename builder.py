from pathlib import Path

from config import TEMPLATE_DIR, OUTPUT_TEX
from sections.projects import get_project
from sections.skills import get_technology as get_skill


def read_tex(filename):
    return (TEMPLATE_DIR / filename).read_text(
        encoding="utf-8"
    )


def build_resume(company, role, project1, project2, technology):

    template = read_tex("resume_template.tex")

    template = template.replace(
        "{{PREAMBLE}}",
        read_tex("preamble.tex")
    )

    template = template.replace(
        "{{HEADER}}",
        read_tex("header.tex")
    )

    template = template.replace(
        "{{EDUCATION}}",
        read_tex("education.tex")
    )

    template = template.replace(
        "{{EXPERIENCE}}",
        read_tex("experience.tex")
    )

    template = template.replace(
        "{{CODING_PROFILES}}",
        read_tex("coding_profiles.tex")
    )

    

    projects = (
        get_project(project1)
        + "\n\n"
        + get_project(project2)
    )

    template = template.replace(
        "{{PROJECTS}}",
        projects
    )

    template = template.replace(
    "{{TECHNOLOGIES}}",
    get_skill(technology)
)

    OUTPUT_TEX.mkdir(
        parents=True,
        exist_ok=True
    )

    tex_path = OUTPUT_TEX / "resume.tex"

    tex_path.write_text(
        template,
        encoding="utf-8"
    )

    return tex_path