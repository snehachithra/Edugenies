"""Concept explanation module using local LaMini-Flan-T5-783M."""
from transformers import pipeline

MODEL_ID = "MBZUAI/LaMini-Flan-T5-783M"
_pipe = None


def _get_pipeline():
    global _pipe
    if _pipe is None:  # lazy load so the app starts fast
        _pipe = pipeline("text2text-generation", model=MODEL_ID)
    return _pipe


def explain_concept(topic: str) -> str:
    prompt = f"Explain the following concept in simple terms for a beginner: {topic}"
    try:
        out = _get_pipeline()(prompt, max_length=256, do_sample=True, temperature=0.7)
        return out[0]["generated_text"].strip()
    except Exception as e:
        return f"Error generating explanation: {e}"
