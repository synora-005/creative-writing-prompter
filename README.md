# Creative Writing Prompter

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/mhahk5dj62/badge.svg)](https://ask.thili.ai/b/mhahk5dj62)

This Creative Writing Prompter is a CLI tool designed for aspiring writers to overcome writer's block. It offers context-aware next-word suggestions by sampling from a genre corpus of short stories. The tool's core is a next-word prediction engine, analyzing text to provide contextually relevant word choices.

This version is an n-gram language model written from scratch in plain Python, with no machine-learning libraries. It learns from *The Adventures of Sherlock Holmes* (public domain), so its suggestions sound like Victorian detective fiction.

## What you are building

**Goal.** You will build a command-line interface (CLI) tool that provides context-aware next-word suggestions to help aspiring writers. This tool will use a next-word prediction engine to generate text by sampling based on computed n-gram probabilities from a genre corpus.

**Done when.** The project is done when you have successfully prepared a text corpus, implemented n-gram counting with maximum-likelihood probabilities and add-k smoothing, developed a function to generate text by sampling from your model, and created a functional CLI interface for users to get suggestions.

## Milestones

- [x] **1. Prepare a text corpus of short stories.** `tokenize` lowercases the text, splits it into words and punctuation, and wraps each sentence in `<s>` ... `</s>` markers.
- [x] **2. Implement n-gram counting and maximum-likelihood probabilities.** `count_ngrams` and `mle_probability`: P(word | context) = count(context, word) / count(context).
- [x] **3. Add add-k smoothing to handle unseen n-grams.** `smoothed_probability`: (count(context, word) + k) / (count(context) + k * V), so no word is ever impossible.
- [x] **4. Develop a function to generate text by sampling from the model.** `generate_text` picks each next word at random, weighted by its probability, until the model ends the sentence.
- [x] **5. Create a CLI interface for users to input text and get suggestions.** `python -m app.cli suggest` and `python -m app.cli interactive`.

## Run it

You need Python 3.12 or newer and git.

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

**Mac / Linux**

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then check that everything works:

```
python -m app.cli hello
pytest
```

The `.env` file holds optional model settings from the starter. The n-gram model does not use any of them, so you can leave it as it is.

## Using the tool

The stories the model learns from are in `data/corpus.txt`. Use `--corpus` to point to a different text file.

**Get next-word suggestions**

```
python -m app.cli suggest sherlock
```

```
Next-word suggestions after "sherlock":
  holmes       0.924
  swimmer      0.000
  ...
```

**Also write a continuation**

```
python -m app.cli suggest the detective --generate
```

**Keep typing and get suggestions each time** (press Enter on an empty line to quit)

```
python -m app.cli interactive
```

**Options** (for `suggest` and `interactive`)

| Option | Default | What it does |
| --- | --- | --- |
| `--corpus FILE` | `data/corpus.txt` | text file to learn from |
| `--n N` | 2 | n-gram size: 2 = bigram, 3 = trigram (type 2+ words) |
| `--k K` | 0.001 | add-k smoothing; smaller values follow the stories more closely |
| `--top N` | 5 | how many suggestions to show |
| `--generate` | off | also write a continuation |
| `--words N` | 25 | maximum words in the continuation |
| `--seed N` | random | use the same number to repeat the same continuation |

## How it works

1. **Tokenize.** The stories become a list of lowercase words and punctuation marks, with `<s>` and `<e>` sentence markers (`<s>`, `</s>`).
2. **Count.** For every run of `n` tokens, count how often the run occurs and how often its first `n-1` tokens (the context) occur.
3. **Smooth.** Add `k` to every count so words never seen after a context still get a small, non-zero chance.
4. **Suggest or generate.** Score every word in the vocabulary given the last `n-1` words, then show the best few, or draw one at random and repeat.

## Tests

```
pytest
```

The tests cover tokenizing, counting, probabilities, smoothing, generation, suggestions and the CLI. Each uses a tiny made-up text so the expected answers can be checked by hand.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Limits and ideas

- A bigram model only sees the last word, so suggestions can be vague (after "the detective" most words tie). A trigram model sees two words, but it has seen fewer examples, so it often copies whole phrases from the stories.
- Add-k smoothing is simple but blunt. A large `k` makes the text random, which is why the default is small.
- Ideas to try: top-k or temperature sampling, backoff from trigram to bigram, a horror or fantasy corpus, or capitalizing names such as "Holmes".