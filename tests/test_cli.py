import pytest

from app.cli import main


def make_corpus(tmp_path, text="the cat sat. the cat sat. the dog ran."):
    path = tmp_path / "corpus.txt"
    path.write_text(text, encoding="utf-8")
    return str(path)


def test_suggest_prints_likely_next_words(tmp_path, capsys):
    main(["suggest", "the", "--corpus", make_corpus(tmp_path), "--top", "2"])
    out = capsys.readouterr().out
    assert "cat" in out and "dog" in out
    assert out.index("cat") < out.index("dog")  # "cat" is the more likely word


def test_suggest_can_also_generate(tmp_path, capsys):
    # this corpus only ever says "the cat sat.", so the continuation can't vary
    corpus = make_corpus(tmp_path, "the cat sat. the cat sat.")
    main(["suggest", "the", "--corpus", corpus,
          "--k", "1e-9", "--generate", "--seed", "0"])
    assert "Continuation: The cat sat." in capsys.readouterr().out


def test_interactive_quits_on_an_empty_line(tmp_path, capsys, monkeypatch):
    answers = iter(["the", ""])
    monkeypatch.setattr("builtins.input", lambda _="": next(answers))
    main(["interactive", "--corpus", make_corpus(tmp_path)])
    assert "cat" in capsys.readouterr().out


def test_missing_corpus_gives_a_clear_error(tmp_path):
    with pytest.raises(SystemExit):
        main(["suggest", "the", "--corpus", str(tmp_path / "nope.txt")])