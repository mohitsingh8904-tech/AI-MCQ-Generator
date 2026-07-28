import os

os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"

from transformers import pipeline

_generator = None


def get_generator():
    global _generator
    if _generator is None:
        _generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-small"
        )
    return _generator


def generate_mcqs(text):
    generator = get_generator()

    prompt = f"""
TASK: Generate Multiple Choice Questions ONLY.

RULES:
- DO NOT explain theory
- DO NOT summarize
- DO NOT repeat text
- OUTPUT ONLY MCQs

FORMAT (STRICT):

Q1. Question?
A) Option
B) Option
C) Option
D) Option
Answer: A

Q2. Question?
A) Option
B) Option
C) Option
D) Option
Answer: B

TEXT:
{text}
"""

    result = generator(
        prompt,
        max_length=600,
        do_sample=False
    )

    return result[0]["generated_text"]
from transformers import T5ForConditionalGeneration, T5Tokenizer

MODEL_NAME = "google/flan-t5-small"

tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)

def run_flan_t5(prompt: str) -> str:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_new_tokens=128)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

