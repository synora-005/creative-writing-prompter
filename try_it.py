from app.core import (
    load_text, tokenize, count_ngrams,
    mle_probability, get_vocab, smoothed_probability,
)

tokens = tokenize(load_text("data/corpus.txt"))
ngram_counts, context_counts = count_ngrams(tokens, 2)
v = len(get_vocab(tokens))
print("Vocabulary size:", v)

for k in [1.0, 0.1, 0.01]:
    p = smoothed_probability("watson", ["dr"], ngram_counts, context_counts, v, k)
    print(f"k={k}: P(watson | dr) = {p:.6f}")

for k in [1.0, 0.1, 0.01]:
    p = smoothed_probability("holmes", ["sherlock"], ngram_counts, context_counts, v, k)
    print(f"k={k}: P(holmes | sherlock) = {p:.4f}")