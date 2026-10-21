
# AI Interviewer - Resume and Job Matching

from pathlib import Path
from pypdf import PdfReader

known_skills = [
    "Java",
    "Python",
    "SQL",
    "OOP",
    "Spring Boot",
    "Git",
    "HTML",
    "CSS",
    "JavaScript",
    "Machine Learning",
    "Power BI"
]

print("===== AI INTERVIEWER =====")

job_input = input(
    "Enter required job skills, separated by commas: "
)

resume_path = input(
    "Enter your resume file path (.txt or .pdf): "
).strip().strip('"')

job_skills = [
    skill.strip()
    for skill in job_input.split(",")
    if skill.strip()
]

try:
    path = Path(resume_path)

    if path.suffix.lower() == ".pdf":
        reader = PdfReader(str(path))
        resume_text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        ).lower()
    else:
        resume_text = path.read_text(
            encoding="utf-8"
        ).lower()

except FileNotFoundError:
    print("Error: Resume file not found. Check the file path.")
    raise SystemExit(1)

except Exception as error:
    print("Error reading resume:", error)
    raise SystemExit(1)

candidate_skills = [
    skill for skill in known_skills
    if skill.lower() in resume_text
]

matched_skills = [
    skill for skill in job_skills
    if skill.lower() in [
        candidate.lower() for candidate in candidate_skills
    ]
]

missing_skills = [
    skill for skill in job_skills
    if skill.lower() not in [
        candidate.lower() for candidate in candidate_skills
    ]
]

percentage = (
    len(matched_skills) / len(job_skills) * 100
    if job_skills else 0
)

suggestions = {
    "java": "Practice Java coding and OOP.",
    "sql": "Practice SQL queries and joins.",
    "oop": "Study encapsulation, inheritance, and polymorphism.",
    "spring boot": "Build a REST API using Spring Boot.",
    "git": "Practice Git add, commit, push, and pull.",
    "python": "Practice Python functions and collections.",
    "power bi": "Build an interactive analytics dashboard."
}

print("\n===== MATCH REPORT =====")
print("Job skills:", job_skills)
print("Resume skills found:", candidate_skills)
print("Matched skills:", matched_skills)
print("Missing skills:", missing_skills)
print(f"Matching percentage: {percentage:.2f}%")

print("\n===== IMPROVEMENT SUGGESTIONS =====")

for skill in missing_skills:
    suggestion = suggestions.get(
        skill.lower(),
        "Learn the fundamentals and build a small project."
    )
    print(f"{skill}: {suggestion}")

if not missing_skills:
    print("All required skills matched!")

report_path = Path("interview_report.txt")

with report_path.open("w", encoding="utf-8") as file:
    file.write("===== AI INTERVIEWER MATCH REPORT =====\n")
    file.write(f"Job skills: {job_skills}\n")
    file.write(f"Resume skills: {candidate_skills}\n")
    file.write(f"Matched skills: {matched_skills}\n")
    file.write(f"Missing skills: {missing_skills}\n")
    file.write(f"Matching percentage: {percentage:.2f}%\n")

    file.write("\n===== IMPROVEMENT SUGGESTIONS =====\n")

    for skill in missing_skills:
        suggestion = suggestions.get(
            skill.lower(),
            "Learn the fundamentals and build a small project."
        )
        file.write(f"{skill}: {suggestion}\n")

print(f"\nReport saved to: {report_path.resolve()}")
