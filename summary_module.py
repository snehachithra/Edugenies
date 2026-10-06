"""Summarization module (Gemini)."""
from gemini_client import generate


def summarize_text(text: str) -> str:
    prompt = (
        "Summarize the following educational passage into a concise, easy-to-understand "
        "version that keeps the core information and removes redundancy:\n\n" + text
    )
    try:
        return generate(prompt)
    except Exception as e:
        return f"Error generating summary: {e}"
