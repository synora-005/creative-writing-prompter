"""Your code. One stub per milestone; build them in order and keep each one small."""

import re


# --- Milestone 1: Prepare a text corpus of short stories.
# Hint: Use text preprocessing and tokenization.
def load_text(path):
    """Read a text file and return its contents as one string."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def tokenize(text):
    """Lowercase the text and split it into word and punctuation tokens.
    Each sentence is wrapped in <s> ... </s> markers."""
    text = text.lower()
    sentences = re.split(r"(?<=[.!?])\s+", text)
    tokens = []
    for sentence in sentences:
        words = re.findall(r"[a-z']+|[.,!?;]", sentence)
        if words:
            tokens += ["<s>"] + words + ["</s>"]
    return tokens


# --- Milestone 2: Implement n-gram counting and maximum-likelihood probabilities.
# Hint: Apply n-gram model and frequency counting.
def milestone_2():  # TODO(milestone 2)
    raise NotImplementedError("TODO(milestone 2)")


# --- Milestone 3: Add add-k smoothing to handle unseen n-grams.
# Hint: Implement add-k smoothing.
def milestone_3():  # TODO(milestone 3)
    raise NotImplementedError("TODO(milestone 3)")


# --- Milestone 4: Develop a function to generate text by sampling from the model.
# Hint: Utilize probability distribution sampling.
def milestone_4():  # TODO(milestone 4)
    raise NotImplementedError("TODO(milestone 4)")


# --- Milestone 5: Create a CLI interface for users to input text and get suggestions.
# Hint: Build a command-line interface for user interaction.
def milestone_5():  # TODO(milestone 5)
    raise NotImplementedError("TODO(milestone 5)")