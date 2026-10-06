"""Question answering module (Gemini)."""
from gemini_client import generate


def get_answer(question: str) -> str:
    prompt = (
        "You are EduGenie, a helpful educational assistant. "
        "Answer the following question accurately and concisely.\n\n"
        f"Question: {question}\nAnswer:"
    )
    try:
        return generate(prompt)
    except Exception as e:
        return f"Error generating answer: {e}"
