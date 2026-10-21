
# AI Interviewer - Keyword Matching Project

# Sample job requirements
job_skills = [
    "Java",
    "SQL",
    "OOP",
    "Spring Boot",
    "Git"
]

# Sample candidate skills
candidate_skills = [
    "Java",
    "SQL",
    "OOP",
    "Git"
]

# Find matching and missing skills
matched_skills = []

for skill in job_skills:
    if skill.lower() in [s.lower() for s in candidate_skills]:
        matched_skills.append(skill)

missing_skills = []

for skill in job_skills:
    if skill.lower() not in [s.lower() for s in candidate_skills]:
        missing_skills.append(skill)

# Calculate percentage
total_skills = len(job_skills)
matched_count = len(matched_skills)

if total_skills > 0:
    percentage = (matched_count / total_skills) * 100
else:
    percentage = 0

# Display report
print("\n===== AI INTERVIEWER REPORT =====")
print("Job Skills:", job_skills)
print("Candidate Skills:", candidate_skills)
print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
print("Matching Percentage:", percentage, "%")

# Suggest improvements
print("\n===== SKILL IMPROVEMENT =====")

suggestions = {
    "java": "Practice Java coding and OOP.",
    "sql": "Practice SQL queries and joins.",
    "oop": "Study encapsulation, inheritance, and polymorphism.",
    "spring boot": "Build a REST API using Spring Boot.",
    "git": "Practice Git add, commit, push, and pull.",
    "python": "Practice Python functions and collections."
}

for skill in missing_skills:
    print("Improve:", skill)
    suggestion = suggestions.get(
        skill.lower(),
        "Learn the basics and build a small project."
    )
    print("Suggestion:", suggestion)

if not missing_skills:
    print("Great! All required skills matched.")
# Save the report to a text file

with open("interview_report.txt", "w", encoding="utf-8") as file:
    file.write("===== AI INTERVIEWER REPORT =====\n")
    file.write(f"Job Skills: {job_skills}\n")
    file.write(f"Candidate Skills: {candidate_skills}\n")
    file.write(f"Matched Skills: {matched_skills}\n")
    file.write(f"Missing Skills: {missing_skills}\n")
    file.write(f"Matching Percentage: {percentage:.2f}%\n")

    file.write("\n===== SKILL IMPROVEMENT =====\n")

    for skill in missing_skills:
        suggestion = suggestions.get(
            skill.lower(),
            "Learn the basics and build a small project."
        )
        file.write(f"Improve: {skill}\n")
        file.write(f"Suggestion: {suggestion}\n")

print("\nReport saved to interview_report.txt")