import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
    nltk.download("punkt_tab")


def generate_mcqs_from_text(text, num_questions=5):

    sentences = nltk.sent_tokenize(text)

    if not sentences:
        return []

    vectorizer = TfidfVectorizer(stop_words="english")

    X = vectorizer.fit_transform(sentences)

    scores = X.sum(axis=1).A1

    ranked = sorted(zip(scores, sentences), reverse=True)

    mcqs = []

    for i, (_, sent) in enumerate(ranked[:num_questions], start=1):

        words = sent.split()

        if len(words) < 6:
            continue

        answer = words[-2]

        question = sent.replace(answer, "_____")

        options = random.sample(words[:-2], min(3, len(words[:-2])))

        options.append(answer)

        random.shuffle(options)

        explanation = (
            f'"{answer}" is the correct word that originally appeared in the blank.'
        )

        mcqs.append(
            {
                "question": f"Q{i}. {question}",
                "options": options,
                "answer": answer,
                "explanation": explanation,
            }
        )

    return mcqs