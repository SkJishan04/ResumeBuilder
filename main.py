from builder import build_resume
from compiler import compile_pdf

company = input("Company Name : ")
role = input("Job Role / ID : ")

print("\nProjects")

print("1. LLM RAG")
print("2. CNN")
print("3. Sentiment Analysis")
print("4. Recommendation System")

project1 = int(input("Select Project 1 : "))
project2 = int(input("Select Project 2 : "))

print("\nSkill Set")

print("1. AIML")
print("2. Data Analytics")
print("3. LLM")
print("4. Full Stack")

skill = int(input("Select Skill : "))

tex_path = build_resume(
    company,
    role,
    project1,
    project2,
    skill
)

compile_pdf(tex_path, company, role)