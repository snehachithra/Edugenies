"""Quiz generation module (Gemini). Returns 3 MCQs with 4 options each."""
import json
import re
from gemini_client import generate


def clean_json_block(text: str) -> str:
    """Strip Markdown code fences (```json ... ```) from a model response."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    prompt = f"""Create exactly 3 multiple-choice questions from the passage or topic below.
Each question must have 4 plausible options and one correct answer.
Respond ONLY with valid JSON, no extra text, in this format:
[
  {{"question": "...", "options": ["A", "B", "C", "D"], "answer": "<exact text of the correct option>"}}
]

Passage/Topic:
{passage}
"""
    try:
        raw = generate(prompt)
        quiz = json.loads(clean_json_block(raw))
        if not isinstance(quiz, list):
            raise ValueError("Quiz response was not a list.")
        return quiz
    except json.JSONDecodeError as e:
        return {"error": f"Could not parse quiz JSON: {e}"}
    except Exception as e:
        return {"error": f"Error generating quiz: {e}"}
