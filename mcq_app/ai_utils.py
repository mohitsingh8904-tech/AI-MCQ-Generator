import os
from google import genai

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_mcqs(text):
    """
    Generate MCQs using Gemini 2.5 Flash
    """

    prompt = f"""
You are an AI MCQ Generator.

Generate exactly 5 Multiple Choice Questions from the given text.

Rules:
- Return only MCQs.
- Each question must have 4 options.
- Mention the correct answer.
- Keep questions concise.

Format:

Q1. Question

A) Option

B) Option

C) Option

D) Option

Answer: A

TEXT:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


def run_flan_t5(prompt: str):
    """
    Compatibility function.
    Existing views.py calls this function.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text