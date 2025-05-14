from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/summarize")
def summarize(request: URLRequest):
    try:
        # Scrape the article content
        response = requests.get(request.url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text() for p in paragraphs if p.get_text())

        if not content:
            raise HTTPException(status_code=404, detail="No readable content found on the page.")

        # Summarize using Gemini Chat
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat()
        result = chat.send_message(f"Summarize this news article:\n\n{content}")

        return {"summary": result.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
