from builder import build_resume
from compiler import compile_pdf


def main():
    print("=" * 50)
    print("        Resume Builder")
    print("=" * 50)

    company = input("Company Name : ").strip()
    role = input("Job Role / Job ID : ").strip()

    # -------------------- Projects --------------------
    print("\nSelect Project 1")
    print("1. AI PM Assistant (RAG)")
    print("2. Req2Arch")
    print("3. CNN Image Classification")
    print("4. Sentiment Analysis")

    project1 = int(input("Choice : "))

    print("\nSelect Project 2")
    print("1. AI PM Assistant (RAG)")
    print("2. Req2Arch")
    print("3. CNN Image Classification")
    print("4. Sentiment Analysis")

    project2 = int(input("Choice : "))

    # -------------------- Skills --------------------
    print("\nSelect Skill Set")
    print("1. AI / Machine Learning")
    print("2. Data Analytics")
    print("3. LLM / Generative AI")
    print("4. Full Stack")

    skill = int(input("Choice : "))

    # -------------------- Build Resume --------------------
    tex_path = build_resume(
        company=company,
        role=role,
        project1=project1,
        project2=project2,
        skill=skill
    )

    # -------------------- Compile PDF --------------------
    compile_pdf(tex_path, company, role)

    print("\nResume Generated Successfully!")


if __name__ == "__main__":
    main()