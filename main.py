from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. Update Schema to support missing metrics using Optional or None
class Candidate(BaseModel):
    candidate_name: str
    technical_skills: Optional[int] = None
    communication: Optional[int] = None
    problem_solving: Optional[int] = None

@app.get("/")
def home():
    return {"message": "Structured Feedback Generator API"}

@app.post("/generate-feedback")
def generate_feedback(candidate: Candidate):
    # 2. Extract scores into a list to filter out missing data
    scores = [
        candidate.technical_skills, 
        candidate.communication, 
        candidate.problem_solving
    ]
    
    # Filter out any 'None' values dynamically (Handles the requested Edge Case)
    valid_scores = [s for s in scores if s is not None]

    # Fallback safety net if absolutely no scores were provided
    if not valid_scores:
        return {
            "overall_rating": 0,
            "recommendation": "Unable to assess - Missing all metrics"
        }

    # 3. Dynamic Average Calculation (Divide by len(valid_scores) instead of a hardcoded 3)
    overall = sum(valid_scores) / len(valid_scores)

    # 4. Recommendation Mapping Logic
    if overall >= 8:
        recommendation = "Proceed to Next Round"
    elif overall >= 6:
        recommendation = "Consider for Further Evaluation"
    else:
        recommendation = "Not Recommended"
        
    summary = "Candidate evaluation completed."    

    # 5. Automated Structured Output
    return {
    "candidate_name": candidate.candidate_name,
    "technical_skills_score": candidate.technical_skills,
    "communication_score": candidate.communication,
    "problem_solving_score": candidate.problem_solving,
    "overall_rating": round(overall, 2),
    "recommendation": recommendation,
    "summary": "Strong technical and problem-solving skills. Communication could be improved."
    }