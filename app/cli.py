"""Command-line entry point: `python -m app.cli --help`."""
import argparse
import os

from app.core import build_model, generate_text, suggest_next_words

DEFAULT_CORPUS = "data/corpus.txt"


def add_options(parser):
    """Options shared by the `suggest` and `interactive` commands."""
    parser.add_argument("--corpus", default=DEFAULT_CORPUS, help="text file of stories to learn from")
    parser.add_argument("--n", type=int, default=2, help="n-gram size: 2 = bigram, 3 = trigram (needs 2+ words typed)")
    parser.add_argument("--k", type=float, default=0.001, help="add-k smoothing amount (smaller = closer to the stories)")
    parser.add_argument("--top", type=int, default=5, help="how many suggestions to show")
    parser.add_argument("--generate", action="store_true", help="also write a continuation")
    parser.add_argument("--words", type=int, default=25, help="maximum words in the continuation")
    parser.add_argument("--seed", type=int, default=None, help="use the same number to repeat a continuation")


def load_model(args):
    if args.n < 2:
        raise SystemExit("--n must be 2 or more.")
    if not os.path.exists(args.corpus):
        raise SystemExit(f"Corpus file not found: {args.corpus}. Save some stories there first.")
    return build_model(args.corpus, args.n)


def show_suggestions(prompt, model, args):
    ngram_counts, context_counts, vocab = model
    print(f'Next-word suggestions after "{prompt}":')
    suggestions = suggest_next_words(
        prompt, ngram_counts, context_counts, vocab, n=args.n, k=args.k, top=args.top
    )
    for word, probability in suggestions:
        print(f"  {word:<12} {probability:.3f}")
    if args.generate:
        text = generate_text(
            ngram_counts, context_counts, vocab, n=args.n, k=args.k,
            max_words=args.words, prompt=prompt, seed=args.seed,
        )
        print("Continuation:", text)


def run_interactive(args):
    model = load_model(args)
    print("Type a few words and press Enter. Press Enter on an empty line to quit.")
    while True:
        try:
            prompt = input("> ").strip()
        except EOFError:
            break
        if not prompt:
            break
        show_suggestions(prompt, model, args)
        print()


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="creative-writing-prompter", description="Aspiring writers use this CLI tool to get context-aware next-word suggestions, helping them develop stories and overcome writer's block by sampling from a genre corpus.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("hello", help="check that everything is wired up")

    suggest = sub.add_parser("suggest", help="show likely next words for the words you give")
    suggest.add_argument("prompt", nargs="*", help="the words written so far")
    add_options(suggest)

    interactive = sub.add_parser("interactive", help="keep typing words and get suggestions each time")
    add_options(interactive)

    args = parser.parse_args(argv)
    if args.command == "hello":
        print("Creative Writing Prompter is ready. Open README.md for your milestones.")
    elif args.command == "suggest":
        show_suggestions(" ".join(args.prompt), load_model(args), args)
    elif args.command == "interactive":
        run_interactive(args)


if __name__ == "__main__":
    main()