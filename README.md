# Article Summarizer API

A FastAPI-based web service that fetches article content from a given URL and summarizes it using Google’s **Gemini 1.5 Flash** model.

---

## 🚀 Features

- Accepts a URL and scrapes article content
- Uses Gemini 1.5 Flash to generate a summary
- REST API built with FastAPI
- Handles invalid URLs or empty content gracefully

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework for the API
- **Pydantic** – Data validation
- **Requests** – HTTP requests for fetching webpage content
- **BeautifulSoup (bs4)** – HTML parsing and content extraction
- **Google Generative AI (Gemini 1.5 Flash)** – For generating summaries
- **python-dotenv** – Securely loads API keys from `.env` file
- **Uvicorn** – ASGI server for running FastAPI apps

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/article-summarizer-api.git
   cd article-summarizer-api
## Install dependencies

bash
Copy
Edit
pip install -r requirements.txt



## Create a .env file and add your Google API key

env
Copy
Edit
GOOGLE_API_KEY_1=your_google_api_key_here



## Running the App
bash
Copy
Edit
uvicorn main:app --reload
The API will be available at: http://127.0.0.1:8000

Access the Swagger UI at: http://127.0.0.1:8000/docs

## 🧪 Example Usage
Request
POST /summarize

Body:

json
Copy
Edit
{
  "url": "https://example.com/some-article"
}

Response
json
Copy
Edit
{
  "summary": "This article discusses..."
}


## 🧠 Notes
Make sure the target webpage has visible <p> tag content.

The Gemini model may return a generic summary if the article is too short or unstructured.

## 📄 License
This project is open source and available under the MIT License.

