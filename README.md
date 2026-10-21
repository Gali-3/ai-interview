# AI Interviewer – Keyword Matching System

## About the Project
The AI Interviewer is a Python-based project that compares the skills required for a job with a candidate's skills. It calculates a matching percentage, identifies missing skills, and provides suggestions for improvement.

## Features
- Accepts job skills and candidate skills.
- Matches skills without case sensitivity.
- Calculates the skill matching percentage.
- Identifies missing skills.
- Provides skill-specific improvement suggestions.
- Saves the interview report to a text file.

## Technologies Used
- Python
- Visual Studio Code
- Git and GitHub

## How to Run

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open the terminal in the project folder.
5. Run:

   `python .\src\keyword_matcher.py`

6. Enter job skills and candidate skills separated by commas.

## Example

**Job skills:** Java, SQL, Python, Spring Boot

**Candidate skills:** Java, SQL, Python

**Expected matching percentage:** 75%

**Missing skill:** Spring Boot

## Project Structure

    ai-interview/
    ├── src/
    │   └── keyword_matcher.py
    ├── README.md
    └── interview_report.txt

## Future Improvements
- Resume upload and skill extraction.
- Interview question generation.
- Answer evaluation.
- A web interface for candidates.

## Author
Developed as a Python learning and interview preparation project.