from pathlib import Path

MY_NAME = "Sk_Jishan"

ROOT = Path(__file__).parent

TEMPLATE_DIR = ROOT / "templates"

OUTPUT_TEX = ROOT / "output" / "tex"
OUTPUT_PDF = ROOT / "output" / "pdf"

LATEX_COMPILER = "pdflatex"