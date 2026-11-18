"""Command-line entry point: `python -m app.cli --help`."""
import argparse


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="creative-writing-prompter", description="Aspiring writers use this CLI tool to get context-aware next-word suggestions, helping them develop stories and overcome writer's block by sampling from a genre corpus.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("hello", help="check that everything is wired up")
    # TODO: add your own commands here as you work through the milestones.
    args = parser.parse_args(argv)
    if args.command == "hello":
        print("Creative Writing Prompter is ready. Open README.md for your milestones.")


if __name__ == "__main__":
    main()
