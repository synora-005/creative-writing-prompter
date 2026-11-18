from app.core import load_text, tokenize, count_ngrams, mle_probability

tokens = tokenize(load_text("data/corpus.txt"))
ngram_counts, context_counts = count_ngrams(tokens, 2)

print("Most common pairs:", ngram_counts.most_common(10))
print("P(holmes | sherlock) =", mle_probability("holmes", ["sherlock"], ngram_counts, context_counts))
print("P(watson | dr) =", mle_probability("watson", ["dr"], ngram_counts, context_counts))