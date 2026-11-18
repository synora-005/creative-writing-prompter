"""Your code. One stub per milestone; build them in order and keep each one small."""

import re
from collections import Counter


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
def count_ngrams(tokens, n=2):
    """Count every n-gram, and every context (the first n-1 words of each n-gram)."""
    ngram_counts = Counter()
    context_counts = Counter()
    for i in range(len(tokens) - n + 1):
        ngram = tuple(tokens[i:i + n])
        ngram_counts[ngram] += 1
        context_counts[ngram[:-1]] += 1
    return ngram_counts, context_counts


def mle_probability(word, context, ngram_counts, context_counts):
    """P(word | context) = count(context + word) / count(context)."""
    context = tuple(context)
    total = context_counts[context]
    if total == 0:
        return 0.0
    return ngram_counts[context + (word,)] / total


# --- Milestone 3: Add add-k smoothing to handle unseen n-grams.
# Hint: Implement add-k smoothing.
def get_vocab(tokens):
    """Return the set of different tokens in the corpus."""
    return set(tokens)


def smoothed_probability(word, context, ngram_counts, context_counts, vocab_size, k=1.0):
    """P(word | context) with add-k smoothing:
    (count(context + word) + k) / (count(context) + k * vocab_size)."""
    context = tuple(context)
    numerator = ngram_counts[context + (word,)] + k
    denominator = context_counts[context] + k * vocab_size
    return numerator / denominator


# --- Milestone 4: Develop a function to generate text by sampling from the model.
# Hint: Utilize probability distribution sampling.
def milestone_4():  # TODO(milestone 4)
    raise NotImplementedError("TODO(milestone 4)")


# --- Milestone 5: Create a CLI interface for users to input text and get suggestions.
# Hint: Build a command-line interface for user interaction.
def milestone_5():  # TODO(milestone 5)
    raise NotImplementedError("TODO(milestone 5)")