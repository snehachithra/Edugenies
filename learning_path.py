"""Learning path / recommendation module (Gemini)."""
from gemini_client import generate


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""Create a personalized, structured learning path for: {topic}

Include:
1. Beginner, Intermediate and Advanced stages with key concepts for each
2. Suggested timeline per stage
3. Useful resources (videos, articles, books)
4. Practice suggestions

Keep it clear and well organized."""
    try:
        return generate(prompt)
    except Exception as e:
        return f"Error generating learning path: {e}"
