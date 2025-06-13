# TDS Virtual TA

A **FastAPI-based virtual teaching assistant** for IITM's **Tools in Data Science (TDS) Jan 2025** course.  
This API answers student queries based on course topics and discussions from Discourse.

---

## 🚀 Deployed Link

🔗 [https://tds-virtual-ta.onrender.com](https://tds-virtual-ta.onrender.com)

✔️ On opening this link, you will see:
{
  "message": "TDS Virtual TA is running. Use POST /api/ to ask questions."
}

📡 API Usage
POST /api/ — to get answers for course-related questions.

Request JSON example:
{
  "question": "What is Docker?"
}

Response example:
{
  "answer": "It's recommended to use Podman, but Docker is acceptable.",
  "links": [
    {
      "url": "https://tds.s-anand.net/#/docker",
      "text": "Docker vs Podman discussion"
    }
  ]
}

⚙️ Run Locally
pip install -r requirements.txt
uvicorn main:app --reload
Access at:
http://127.0.0.1:8000/

🧹 Discourse Scraper
This repository includes scraper.py to scrape posts from the TDS Discourse forum for a given date range.

To run the scraper:
python scraper.py

📦 Project Structure
├── main.py          # FastAPI backend
├── scraper.py       # Discourse scraper
├── requirements.txt
└── README.md

👤 Author
Vivek Kumar


