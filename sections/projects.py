from pathlib import Path


PROJECTS = {
    1: "AI PM Assistant (RAG)",
    2: "Req2Arch",
    3: "CNN Image Classification",
    4: "Sentiment Analysis",
    5: "Expense Tracker",
    6: "Automated Transcription System"
}


def show_projects():
    print("\nAvailable Projects")
    print("-" * 40)

    for number, project in PROJECTS.items():
        print(f"{number}. {project}")

    print("-" * 40)


def load_tex(path):
    return Path(path).read_text(encoding="utf-8")


def get_project(choice):

    match choice:

        case 1:
            return load_tex("templates/projects/rag.tex")

        case 2:
            return load_tex("templates/projects/req2arch.tex")

        case 3:
            return load_tex("templates/projects/cnn.tex")

        case 4:
            return load_tex("templates/projects/sentiment.tex")

        case 5:
            return load_tex("templates/projects/expense_tracker.tex")

        case 6:
            return load_tex("templates/projects/transcription.tex")

        case _:
            raise ValueError("Invalid Project Selected")