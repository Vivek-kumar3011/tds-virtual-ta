from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

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
    # Dummy Logic — replace with your scraped data processing or simple if-else
    if "docker" in q.question.lower():
        return {
            "answer": "It's recommended to use Podman, but Docker is acceptable.",
            "links": [{"url": "https://tds.s-anand.net/#/docker", "text": "Docker vs Podman discussion"}]
        }
    elif "deadline" in q.question.lower():
        return {
            "answer": "The end-term exam date is not yet announced.",
            "links": []
        }
    else:
        return {
            "answer": "I am not sure about that. Please check the Discourse forum.",
            "links": []
        }

