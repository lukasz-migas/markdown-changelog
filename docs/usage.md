# Usage

## Register the extension

Python-Markdown discovers the extension through its entry point. Pass
`"changelog"` when creating a converter:

```python
import markdown

md = markdown.Markdown(extensions=["changelog"])
print(md.convert(";;fix;; Keep the parser state between calls."))
```

The converter returns HTML with a badge span:

```html
<p><span class="badge badge-fix">Fix</span> Keep the parser state between calls.</p>
```

You can also import the extension directly when you want to pass options:

```python
import markdown
from markdown_changelog import ChangelogExtension

md = markdown.Markdown(extensions=[ChangelogExtension(auto_capitalize=False)])
print(md.convert(";;docs;;"))
```

## Add badges

Wrap a tag in double semicolons. The default tags are `new`, `fix`,
`improvement`, `change`, `remove`, `docs`, and `efficiency`. Common aliases
include `feature` for `new`, `changed` for `change`, and `documentation` for
`docs`.

```markdown
;;new;; Add a command line option.
;;fix;; Handle an empty input file.
;;VERv1.2.3;;
```

The extension renders the sample as:

<p><span class="badge badge-new">New</span> Add a command line option.</p>
<p><span class="badge badge-fix">Fix</span> Handle an empty input file.</p>
<p><span class="badge badge-version">v1.2.3</span></p>

Unknown tags are kept as badge text. Tag names are capitalized by default.
Version markers start with `VER` and keep their version text as written.

## Configure badge output

Pass options to `ChangelogExtension`. The defaults use CSS classes, capitalize
tag names, and round the badge corners. `inline_style=True` puts the CSS
properties on each generated span, which helps when a site cannot load an
extra stylesheet.

```python
import markdown
from markdown_changelog import ChangelogExtension

extension = ChangelogExtension(
    auto_capitalize=False,
    rounded_corners=False,
    inline_style=True,
    fix_color="#7A1FA2",
)
md = markdown.Markdown(extensions=[extension])
print(md.convert(";;fix;;"))
```

Color options are `text_color`, `fix_color`, `change_color`,
`improvement_color`, `new_color`, `efficiency_color`, `docs_color`,
`version_color`, and `remove_color`. They accept CSS color values. The
stylesheet-based mode uses the default badge colors; custom colors apply to
inline styles.

## Include the stylesheet

In a documentation project, copy `docs/css/style.css` into the site's docs
directory and add its path to the site configuration. See the
[styling guide](style.md) for the Zensical setting and the optional release
timeline layout.
