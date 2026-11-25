# Zensical

This repository builds its documentation with Zensical. The site configuration
lives in `zensical.toml`, and the GitHub Actions workflow publishes the built
site to GitHub Pages when changes reach the `main` or `master` branch.

To use Markdown Changelog in another Zensical site, install both packages in
the environment used to build the site:

```sh
uv add --dev zensical markdown-changelog
```

Set the stylesheet path and register the extension in `zensical.toml`:

```toml
[project]
site_name = "Project documentation"
extra_css = ["css/style.css"]

[project.markdown_extensions]
changelog = {}
```

Copy this repository's `docs/css/style.css` into the site's `docs/css/` folder.
Pages can then use markers such as `;;new;;` and `;;VERv1.2.3;;`. Run
`uv run zensical serve` to preview changes and `uv run zensical build` to
create the static site.

Zensical supports Python-Markdown extensions through its Markdown
compatibility layer. Configure this package as a Markdown extension. Zensical's
MkDocs plugin support follows a separate compatibility list. See the
[Zensical compatibility guide](https://zensical.org/docs/compatibility/markdown/python-markdown/)
for the supported extension model.
