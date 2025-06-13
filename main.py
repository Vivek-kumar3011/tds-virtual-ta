from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# ✅ Root endpoint to check server status
@app.get("/")
def read_root():
    return {"message": "TDS Virtual TA is running!"}

# Define request body
class Question(BaseModel):
    question: str
    image: Optional[str] = None  # base64 encoded image if any

# Define response structure
class Link(BaseModel):
    url: str
    text: str

class AnswerResponse(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=AnswerResponse)
def get_answer(q: Question):
    question_text = q.question.lower()
    # Dummy Logic — replace with your scraped data processing or simple if-else
    if "docker" in question_text or "podman" in question_text:
        return {
            "answer": "It's recommended to use Podman, but Docker is acceptable.",
            "links": [
                {"url": "https://tds.s-anand.net/#/docker", "text": "Docker vs Podman discussion"}
            ]
        }

    elif "deadline" in question_text or "exam date" in question_text or "end term" in question_text:
        return {
            "answer": "The End-Term exam is scheduled for 31st August 2025.",
            "links": []
        }

    elif "discourse" in question_text or "forum" in question_text:
        return {
            "answer": "You can post your doubts or find discussions on the course Discourse Forum.",
            "links": [
                {"url": "https://discourse.iitm.ac.in/c/tds-jan2025", "text": "Discourse Forum"}
            ]
        }

    elif "course portal" in question_text or "study portal" in question_text:
        return {
            "answer": "Visit the IITM BS Study Portal for course materials and updates.",
            "links": [
                {"url": "https://study.iitm.ac.in/ds/", "text": "IITM BS Study Portal"}
            ]
        }

    else:
        return {
            "answer": "I'm not sure about that. Please check the course Discourse forum or Study Portal for more information.",
            "links": [
                {"url": "https://discourse.iitm.ac.in/c/tds-jan2025", "text": "Discourse Forum"},
                {"url": "https://study.iitm.ac.in/ds/", "text": "IITM BS Study Portal"}
            ]
        }
