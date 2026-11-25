# Markdown-changelog

Markdown extension to enable easy addition of changelog badges to your documentation

[![Documentation Status](https://readthedocs.org/projects/markdown-changelog/badge/?version=latest)](https://markdown-changelog.readthedocs.io/en/latest/?badge=latest)
![Tests](https://github.com/lukasz-migas/markdown-changelog/workflows/Tests/badge.svg)
[![codecov](https://codecov.io/gh/lukasz-migas/markdown-changelog/branch/master/graph/badge.svg?token=82OYPER5DP)](https://codecov.io/gh/lukasz-migas/markdown-changelog)

## Installation

The easiest way to install `markdown-changelog` is to use pip

```bash
pip install markdown-changelog
```

## Usage

Changelog adds the ability to insert styled `<span>TAG</span>` tags that with appropriate CSS are rendered as 
changelog badges in your documentation. The syntax requires the text to be surrounded by double semi-colon (;) signs.

To add a badge to your documentation simply surround the appropriate tag with double `;`.

```python
import markdown

text = """;;fix;;"""
md = markdown.Markdown(extensions=["changelog"])
md.convert(text)
'<p><span class="badge badge-fix">Fix</span></p>'

# or
md = markdown.Markdown(extensions=["markdown_changelog.changelog"])
md.convert(text)
'<p><span class="badge badge-fix">Fix</span></p>'

# or 
from markdown_changelog import ChangelogExtension
md = markdown.Markdown(extensions=[ChangelogExtension()])

md.convert(text)
'<p><span class="badge badge-fix">Fix</span></p>'

# you can also specify version
text = """;;VERv1.2.3;;"""
md.convert(text)
'<p><span class="badge badge-version">v1.2.3</span></p>'
```

## Options

- `inline_style` - if `True`, the CSS style will be set inline rather so no additional CSS file(s) are required
- `auto_capitalize` - if `True`, the tag will be automatically capitalized
- `rounded_corners` - if `False`, the edges of the badge will be square-ish
- `text_color` - color of the text (use HEX with # e.g. #FFFFFF)
- `fix_color` - color of the `Fix` tag
- `change_color` - color of the `Change` tag
- `improvement_color` - color of the `Improvement` tag
- `new_color` - color of the `New` tag
- `docs_color` - color of the `Docs` tag
- `efficiency_color` - color of the `Efficency` tag
- `version_color` - color of the `Version` tag
- `remove_color` - color of the `Remove` tag

## Supported tags

The following tags are supported by default:

- fix
- change (or changes changed)
- improvement (or improvements, enhancement, enhancements)
- new (or feature)
- efficiency
- docs (or documentation)
- remove (or removed, delete, deleted)

All must be wrapped in double `;`

## Styling and Zensical

Copy [docs/css/style.css](docs/css/style.css) into your documentation site and
include it as an extra stylesheet. It contains badge styles and an optional
release timeline. See the [styling guide](docs/style.md) for an example and
[Zensical setup](docs/zensical.md) for integration instructions. Alternatively,
set `inline_style=True` to add badge styling directly to the generated HTML.
