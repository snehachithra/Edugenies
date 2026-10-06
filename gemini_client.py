"""Shared Gemini client used by qna, quiz, summary and learning_path modules."""
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
_client = None


def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file.")
        _client = genai.Client(api_key=api_key)
    return _client


def generate(prompt: str) -> str:
    """Send a prompt to Gemini and return the text, or raise on empty output."""
    response = get_client().models.generate_content(model=MODEL_NAME, contents=prompt)
    text = getattr(response, "text", None)
    if not text:
        raise ValueError("Gemini returned an empty or blocked response.")
    return text.strip()
