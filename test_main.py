from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_missing_metrics():
    response = client.post(
        "/generate-feedback",
        json={
            "candidate_name": "John",
            "technical_skills": 8,
            "problem_solving": 6
        }
    )

    assert response.status_code == 200