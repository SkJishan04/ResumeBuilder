from pathlib import Path


SKILLS = {
    1: "AI / Machine Learning",
    2: "LLM / Generative AI",
    3: "Data Analytics",
    4: "Full Stack"
}


def show_technologies():
    print("\nAvailable Skill Sets")
    print("-" * 40)

    for number, skill in SKILLS.items():
        print(f"{number}. {skill}")

    print("-" * 40)


def load_tex(path):
    return Path(path).read_text(encoding="utf-8")


def get_technology(choice):

    match choice:

        case 1:
            return load_tex("templates/skills/aiml.tex")

        case 2:
            return load_tex("templates/skills/llm.tex")

        case 3:
            return load_tex("templates/skills/data_analytics.tex")

        case 4:
            return load_tex("templates/skills/fullstack.tex")

        case _:
            raise ValueError("Invalid Skill Set Selected")