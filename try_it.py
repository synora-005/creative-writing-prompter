from app.core import load_text, tokenize

tokens = tokenize(load_text("data/corpus.txt"))
print(len(tokens))
print(tokens[:30])