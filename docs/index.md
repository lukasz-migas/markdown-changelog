# Markdown Changelog

Markdown Changelog adds badges to text processed by Python-Markdown. A marker
such as `;;fix;;` becomes a `<span>` with a badge class. Add the project's
stylesheet to give those classes their colors and spacing.

```markdown
;;new;; Add support for nested release notes.
;;fix;; Preserve the version text in headings.
```

The page renders the markers as badges:

<p><span class="badge badge-new">New</span> Add support for nested release notes.</p>
<p><span class="badge badge-fix">Fix</span> Preserve the version text in headings.</p>

Install the package, then register `changelog` when you create a Markdown
converter. The extension also accepts a `ChangelogExtension` instance when you
need to set options in Python.

See [installation](installation.md), [usage](usage.md), and
[styling](style.md) for examples. This documentation site uses
[Zensical](zensical.md).
