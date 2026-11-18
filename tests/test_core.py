"""Your tests. Each milestone in README.md gets one here: write the test first, then make it pass.

They start skipped. Remove the `skip` line as you work on each milestone.
"""
import pytest

from app.core import (
    tokenize,
    count_ngrams,
    mle_probability,
    get_vocab,
    smoothed_probability,
    generate_text,
)


# Milestone 1: Prepare a text corpus of short stories.
def test_milestone_1():
    tokens = tokenize("The cat sat. The dog ran!")
    assert tokens == [
        "<s>", "the", "cat", "sat", ".", "</s>",
        "<s>", "the", "dog", "ran", "!", "</s>",
    ]


# Milestone 2: Implement n-gram counting and maximum-likelihood probabilities.
def test_milestone_2():
    tokens = tokenize("the cat sat. the cat ran. the dog sat.")
    ngram_counts, context_counts = count_ngrams(tokens, 2)
    assert ngram_counts[("the", "cat")] == 2
    assert mle_probability("cat", ["the"], ngram_counts, context_counts) == pytest.approx(2 / 3)
    assert mle_probability("dog", ["the"], ngram_counts, context_counts) == pytest.approx(1 / 3)
    assert mle_probability("sat", ["cat"], ngram_counts, context_counts) == pytest.approx(1 / 2)
    assert mle_probability("ran", ["dog"], ngram_counts, context_counts) == 0.0


# Milestone 3: Add add-k smoothing to handle unseen n-grams.
def test_milestone_3():
    tokens = tokenize("the cat sat. the cat ran. the dog sat.")
    ngram_counts, context_counts = count_ngrams(tokens, 2)
    vocab = get_vocab(tokens)
    v = len(vocab)

    # a pair never seen in the text is no longer impossible
    p_unseen = smoothed_probability("ran", ["dog"], ngram_counts, context_counts, v, k=1.0)
    assert p_unseen > 0

    # seen pairs follow the formula: (2 + 1) / (3 + 8)
    p_seen = smoothed_probability("cat", ["the"], ngram_counts, context_counts, v, k=1.0)
    assert p_seen == pytest.approx(3 / 11)

    # probabilities over the whole vocabulary add up to 1
    total = sum(
        smoothed_probability(w, ["the"], ngram_counts, context_counts, v, k=1.0)
        for w in vocab
    )
    assert total == pytest.approx(1.0)


# Milestone 4: Develop a function to generate text by sampling from the model.
def test_milestone_4():
    tokens = tokenize("the cat sat. the cat sat.")
    ngram_counts, context_counts = count_ngrams(tokens, 2)
    vocab = get_vocab(tokens)

    # the text only ever says "the cat sat.", so with tiny k that is what we get
    text = generate_text(ngram_counts, context_counts, vocab, n=2, k=1e-9, seed=0)
    assert text == "The cat sat."

    # a prompt is continued
    text = generate_text(ngram_counts, context_counts, vocab, n=2, k=1e-9,
                         prompt="the cat", seed=0)
    assert text == "The cat sat."

    # max_words stops the generation early
    text = generate_text(ngram_counts, context_counts, vocab, n=2, k=1.0,
                         max_words=3, seed=1)
    assert len(text.replace(".", " .").split()) <= 3


# Milestone 5: Create a CLI interface for users to input text and get suggestions.
@pytest.mark.skip(reason="remove this line when you start milestone 5")
def test_milestone_5():
    raise NotImplementedError("write the test for milestone 5")