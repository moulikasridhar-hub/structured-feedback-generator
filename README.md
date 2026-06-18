# Structured Feedback Generator

A FastAPI-based backend application that automates recruiter-friendly feedback reports and dynamically handles missing evaluation metrics.

## 🚀 Features
- **Automated Calculations:** Automatically averages evaluation metrics and generates hiring recommendations.
- **Edge-Case Resilience:** Gracefully handles missing/null evaluation metrics without crashing the application.
- **FastAPI Backend:** Lightweight and high-performance API framework.
- **Structured Output:** Returns clean, structured JSON responses for feedback reports.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn

---

## 🛠️ Setup & Installation

1. **Install Dependencies:**
   Make sure you have Python installed, then run the following command to install FastAPI and Uvicorn:
   ```bash
   pip install -r requirements.txt
   ## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

The API will start at:

http://127.0.0.1:8000

## Sample Request

POST /generate-feedback

```json
{
  "candidate_name": "John Doe",
  "technical_skills": 7,
  "communication": 6,
  "problem_solving": 8
}
```

## Sample Response

```json
{
  "candidate_name": "John Doe",
  "technical_skills_score": 7,
  "communication_score": 6,
  "problem_solving_score": 8,
  "overall_rating": 7.0,
  "recommendation": "Consider for Further Evaluation",
  "summary": "Candidate evaluation completed."
}
```