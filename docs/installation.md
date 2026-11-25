# Installation

Markdown Changelog is published as `markdown-changelog` and supports Python
3.11 or newer. It depends on Python-Markdown.

Install it with pip:

```sh
python -m pip install markdown-changelog
```

For a project using uv, add it to the project dependencies:

```sh
uv add markdown-changelog
```

To install the current repository checkout for development, clone the GitHub
repository and sync its development and documentation tools:

```sh
git clone https://github.com/lukasz-migas/markdown-changelog.git
cd markdown-changelog
uv sync --all-groups
```

Use `uv run pytest` to run the test suite. Use `uv run zensical serve` to
preview the documentation site locally.
