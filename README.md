# Markdown Changelog

Markdown Changelog is a Python-Markdown extension that turns short markers into
styled badges. It works in documentation pages and release notes wherever
Python-Markdown extensions are supported.

## Install

```sh
python -m pip install markdown-changelog
```

For a project managed with uv:

```sh
uv add markdown-changelog
```

The package supports Python 3.11 and newer.

## Use

Register the installed extension with Python-Markdown and wrap a tag in two
semicolons on each side:

```python
import markdown

md = markdown.Markdown(extensions=["changelog"])
html = md.convert(";;fix;; The parser now keeps empty sections.")
print(html)
```

The rendered badge looks like this:

<p><span class="badge badge-fix">Fix</span> The parser now keeps empty sections.</p>

Common tags include `new`, `fix`, `improvement`, `change`, `remove`, `docs`, and
`efficiency`. Add a version badge with `;;VERv1.2.3;;`.

The generated spans use CSS classes by default. Copy
[`docs/css/style.css`](docs/css/style.css) into your documentation site and
load it there. Set `inline_style=True` when you cannot add a stylesheet.

See the [usage guide](docs/usage.md) for configuration examples and the
[Zensical guide](docs/zensical.md) for this project's documentation setup.
