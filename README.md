# EduGenie – Gemini Powered Learning Assistant

FastAPI backend + HTML/CSS frontend. Features: Q&A, concept explanation, quiz generation,
summarization and personalised learning paths.

## Setup
```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # then paste your Gemini API key
uvicorn main:app --reload
```
Open http://127.0.0.1:8000

## Endpoints (POST, form field `text`)
`/qa`, `/explain`, `/quiz`, `/summarize`, `/learn/recommendations`

## Notes
- `/explain` uses the local model MBZUAI/LaMini-Flan-T5-783M (downloaded on first use).
- Set `GEMINI_MODEL` in `.env` to change the Gemini model.
