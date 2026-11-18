from app.core import load_text, tokenize, count_ngrams, get_vocab, generate_text

tokens = tokenize(load_text("data/corpus.txt"))
vocab = get_vocab(tokens)

for n in [2, 3]:
    ngram_counts, context_counts = count_ngrams(tokens, n)
    for k in [0.01, 0.001, 0.0001]:
        print(f"--- {n}-gram model, k={k} ---")
        for seed in range(2):
            print(generate_text(ngram_counts, context_counts, vocab, n=n, k=k, seed=seed))
        print()