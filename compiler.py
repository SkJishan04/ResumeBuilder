import subprocess
from pathlib import Path
from datetime import datetime

from config import MY_NAME


def clean(text):
    return (
        text.replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
    )


def compile_pdf(tex_file, company, role):

    output_dir = Path("output/pdf")
    output_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run([
        "pdflatex",
        "-interaction=nonstopmode",
        f"-output-directory={output_dir}",
        str(tex_file)
    ])

    pdf = output_dir / "resume.pdf"

    date = datetime.now().strftime("%d-%m-%Y")

    new_name = output_dir / (
        f"{MY_NAME}_{clean(company)}_{clean(role)}_{date}.pdf"
    )

    if pdf.exists():
        pdf.rename(new_name)

    print("\nResume Generated Successfully")
    print(new_name)