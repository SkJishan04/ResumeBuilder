from builder import build_resume
from compiler import compile_pdf

from sections.projects import show_projects
from sections.skills import show_technologies as show_skills


def main():

    print("=" * 60)
    print("Resume Builder")
    print("=" * 60)

    company = input("Company Name : ").strip()
    role = input("Job Role / ID : ").strip()

    show_projects()
    project1 = int(input("Select Project 1 : "))

    show_projects()
    project2 = int(input("Select Project 2 : "))

    show_skills()
    technology = int(input("Select Technology Profile : "))

    tex_path = build_resume(
        company,
        role,
        project1,
        project2,
        technology
    )

    compile_pdf(
        tex_path,
        company,
        role
    )


if __name__ == "__main__":
    main()