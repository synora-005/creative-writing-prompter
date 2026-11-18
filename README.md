# Creative Writing Prompter

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/mhahk5dj62/badge.svg)](https://ask.thili.ai/b/mhahk5dj62)

This Creative Writing Prompter is a CLI tool designed for aspiring writers to overcome writer's block. It offers context-aware next-word suggestions by sampling from a genre corpus of short stories. The tool's core is a next-word prediction engine, analyzing text to provide contextually relevant word choices.

## What you are building

**Goal.** You will build a command-line interface (CLI) tool that provides context-aware next-word suggestions to help aspiring writers. This tool will use a next-word prediction engine to generate text by sampling based on computed n-gram probabilities from a genre corpus.

**Done when.** The project is done when you have successfully prepared a text corpus, implemented n-gram counting with maximum-likelihood probabilities and add-k smoothing, developed a function to generate text by sampling from your model, and created a functional CLI interface for users to get suggestions.

## Milestones

Tick these off as you go, and commit after each one.

- [ ] **1. Prepare a text corpus of short stories.**  
      Hint: Use text preprocessing and tokenization.
- [ ] **2. Implement n-gram counting and maximum-likelihood probabilities.**  
      Hint: Apply n-gram model and frequency counting.
- [ ] **3. Add add-k smoothing to handle unseen n-grams.**  
      Hint: Implement add-k smoothing.
- [ ] **4. Develop a function to generate text by sampling from the model.**  
      Hint: Utilize probability distribution sampling.
- [ ] **5. Create a CLI interface for users to input text and get suggestions.**  
      Hint: Build a command-line interface for user interaction.

## Run it

You need Python 3.12 and git.

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then choose a model; see the comments inside
python -m app.cli hello
pytest
```

Your work goes in `app/core.py` (one stub per milestone) and `tests/test_core.py`. The first tests pass already; they
check the plumbing.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Stretch ideas

- (none)
