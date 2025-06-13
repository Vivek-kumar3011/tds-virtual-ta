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
            "answer": "Podman is recommended for the course, but Docker is also acceptable.",
            "links": [
                {"url": "https://tds.s-anand.net/#/docker", "text": "Docker vs Podman guidance"}
            ]
        }

    # Exam deadline / date related query
    elif "deadline" in question_text or "exam date" in question_text or "end term" in question_text:
        return {
            "answer": "Sorry, the deadline date for the exam is not available yet based on the context provided.",
            "links": [{"url": "https://study.iitm.ac.in/ds/", "text": "IITM BS Study Portal"}]
        }

    # GPT model question clarification (GA5)
    elif "gpt-3.5" in question_text or "gpt-4o-mini" in question_text or "gpt4" in question_text or "gpt3" in question_text:
        return {
            "answer": "Clarifies use of gpt-3.5-turbo-0125 is not possible; use gpt-4o-mini instead.",
            "links": [
                {"url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939", 
                 "text": "GA5 Question 8 Clarification"}
            ]
        }

    # GA4 Dashboard marks display question
    elif "ga4" in question_text and "dashboard" in question_text:
        return {
            "answer": "If you score 10/10 plus a bonus, your dashboard will display 110.",
            "links": [
                {"url": "https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959",
                 "text": "GA4 Discussion Thread"}
            ]
        }

    # Discourse / Forum related query
    elif "discourse" in question_text or "forum" in question_text:
        return {
            "answer": "You can post your doubts or find discussions on the course Discourse Forum.",
            "links": [
                {"url": "https://discourse.iitm.ac.in/c/tds-jan2025", "text": "Discourse Forum"}
            ]
        }

    # Course portal related query
    elif "course portal" in question_text or "study portal" in question_text:
        return {
            "answer": "Visit the IITM BS Study Portal for course materials and updates.",
            "links": [
                {"url": "https://study.iitm.ac.in/ds/", "text": "IITM BS Study Portal"}
            ]
        }

    # Default response for unrecognized questions
    else:
        return {
            "answer": "I'm not sure about that. Please check the course Discourse forum or Study Portal for more information.",
            "links": [
                {"url": "https://discourse.iitm.ac.in/c/tds-jan2025", "text": "Discourse Forum"},
                {"url": "https://study.iitm.ac.in/ds/", "text": "IITM BS Study Portal"}
            ]
        }
