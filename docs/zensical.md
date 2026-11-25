# Zensical

Zensical can use this package as a Python-Markdown extension. Install both in
the same environment, and copy this project's `docs/css/style.css` to your
site's `docs/css/style.css`:

```sh
uv add --dev zensical markdown-changelog
```

In `zensical.toml`:

```toml
[project]
site_name = "My documentation"
extra_css = ["css/style.css"]

[project.markdown_extensions]
changelog = {}
```

Add `;;new;;` or `;;VERv1.2.3;;` to a Markdown page, then run
`uv run zensical build`. The stylesheet also includes the optional
[release timeline](style.md).

This integration uses Zensical's Python-Markdown compatibility. A native
Zensical module is a future option: Zensical does not currently expose its
module API or run arbitrary MkDocs plugins. See the
[Zensical plugin compatibility documentation](https://zensical.org/docs/compatibility/mkdocs/plugins/).
