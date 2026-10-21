
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

for skill in missing_skills:
    print("Improve:", skill)
    print("Suggestion: Learn the basics and build a small project.")
