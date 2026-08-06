import subprocess
from datetime import datetime
from pathlib import Path

from config import OUTPUT_PDF
from config import LATEX_COMPILER
from config import MY_NAME


def clean(text):

    return (
        text.replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
    )


def compile_pdf(tex_path, company, role):

    OUTPUT_PDF.mkdir(
        parents=True,
        exist_ok=True
    )

    # subprocess.run(
    #     [
    #         LATEX_COMPILER,
    #         "-interaction=nonstopmode",
    #         f"-output-directory={OUTPUT_PDF}",
    #         str(tex_path)
    #     ],
    #     check=True
    # )
    result = subprocess.run(
    [
        LATEX_COMPILER,
        "-interaction=nonstopmode",
        f"-output-directory={OUTPUT_PDF}",
        str(tex_path)
    ],
    text=True
    )

    if result.returncode != 0:
        print()
        print("=" * 60)
        print("WARNING : LaTeX returned warnings/errors.")
        print("A PDF may still have been generated.")
        print("=" * 60)

    pdf = OUTPUT_PDF / "resume.pdf"

    date = datetime.now().strftime("%Y-%m-%d")

    final_name = OUTPUT_PDF / (
        f"{MY_NAME}_"
        f"{clean(company)}_"
        f"{clean(role)}_"
        f"{date}.pdf"
    )

    pdf.rename(final_name)

    print()
    print("=" * 50)
    print("Resume Generated Successfully")
    print(final_name)
    print("=" * 50)