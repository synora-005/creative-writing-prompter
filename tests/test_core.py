"""Your tests. Each milestone in README.md gets one here: write the test first, then make it pass.

They start skipped. Remove the `skip` line as you work on each milestone.
"""
import pytest

from app.core import tokenize, count_ngrams, mle_probability


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
@pytest.mark.skip(reason="remove this line when you start milestone 3")
def test_milestone_3():
    raise NotImplementedError("write the test for milestone 3")


# Milestone 4: Develop a function to generate text by sampling from the model.
@pytest.mark.skip(reason="remove this line when you start milestone 4")
def test_milestone_4():
    raise NotImplementedError("write the test for milestone 4")


# Milestone 5: Create a CLI interface for users to input text and get suggestions.
@pytest.mark.skip(reason="remove this line when you start milestone 5")
def test_milestone_5():
    raise NotImplementedError("write the test for milestone 5")