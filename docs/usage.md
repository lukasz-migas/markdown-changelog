# Usage

## Registration

You can register the extension using any of the following methods:

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
```

## Badges

By default, a number of commonly used badges are available including `new, fix, improvement, change, remove, docs, efficiency`. 
All of them are available by using the `;;TAG;;` syntax. 

```python
import markdown

md = markdown.Markdown(extensions=["changelog"])

# `New` badge
md.convert(""";;new;;""")
'<p><span class="badge badge-new">New</span></p>'

# `Fix` badge
md.convert(""";;fix;;""")
'<p><span class="badge badge-fix">Fix</span></p>'

# `Improvement` badge
md.convert(""";;improvement;;""")
'<p><span class="badge badge-improvement">Improvement</span></p>'

# `Change` badge
md.convert(""";;change;;""")
'<p><span class="badge badge-change">Change</span></p>'

# `Remove` badge
md.convert(""";;remove;;""")
'<p><span class="badge badge-remove">Remove</span></p>'

# `Docs` badge
md.convert(""";;docs;;""")
'<p><span class="badge badge-docs">Docs</span></p>'

# `Efficiency` badge
md.convert(""";;efficiency;;""")
'<p><span class="badge badge-efficiency">Efficiency</span></p>'
```
<p><span class="badge badge-new">New</span>
<span class="badge badge-fix">Fix</span>
<span class="badge badge-improvement">Improvement</span>
<span class="badge badge-change">Change</span>
<span class="badge badge-remove">Remove</span>
<span class="badge badge-docs">Docs</span>
<span class="badge badge-efficiency">Efficiency</span>
</p>

You can specify version in the changelog by using the `;;VERvX.Y.Z;;`:

```python
import markdown

md = markdown.Markdown(extensions=["changelog"])
md.convert(""";;VERv1.2.3;;""")
'<p><span class="badge badge-version">v1.2.3</span></p>'
```
<p><span class="badge badge-version">v1.2.3</span></p>

## Options

A number of config parameters are available to better control the way badges are displayed in your documentation.

### `auto_capitalize`

If `True`, the first letter of the `tag` will be capitalized.

```python
import markdown

md = markdown.Markdown(extensions=["changelog"], extension_configs={"changelog": {"auto_capitalize": False}})
md.convert(""";;docs;; ;;new;;""")
'<p><span class="badge badge-docs">docs</span> <span class="badge badge-new">new</span></p>'
```
<p><span class="badge badge-docs">docs</span> <span class="badge badge-new">new</span></p>

### `rounded_corners`

If `True`, the badge corners will be rounded.

```python
import markdown

md = markdown.Markdown(extensions=["changelog"], extension_configs={"changelog": {"rounded_corners": False}})
md.convert(""";;fix;; ;;change;;""")
'<p><span class="badge badge-fix badge-square">Fix</span> <span class="badge badge-change badge-square">Change</span>'
```
<p><span class="badge badge-fix badge-square">Fix</span> <span class="badge badge-change badge-square">Change</span></p>

### `inline_style`

You can use the `inline_style` keyword parameter to force inclusion of all CSS style parameters on each `span` object.
This should only be used when you cannot include the `style.css` file.

```python
import markdown

md = markdown.Markdown(extensions=["changelog"], extension_configs={"changelog": {"inline_style": True}})
md.convert(""";;fix;;""")
'<p><span style="display: inline-block; padding: 2px 9px; font-size: 14px; line-height: 16px; vertical-align: baseline; white-space: nowrap; background-color: #dc3545; color: #ffffff; border-radius: 9px; ">Fix</span></p>'
```
<p><span style="display: inline-block; padding: 2px 9px; font-size: 14px; line-height: 16px; vertical-align: baseline; white-space: nowrap; background-color: #dc3545; color: #ffffff; border-radius: 9px; ">Fix</span></p>

### Specify color

If you are using the `inline_style` option, you can alter any of the text and background colors by simply modifying
the config file.

```python
import markdown

md = markdown.Markdown(extensions=["changelog"], extension_configs={"changelog": {"inline_style": True, "fix_color":"#FF00FF"}})
md.convert(""";;fix;;""")
'<p><span style="display: inline-block; padding: 2px 9px; font-size: 14px; line-height: 16px; vertical-align: baseline; white-space: nowrap; background-color: #FF00FF; color: #ffffff; border-radius: 9px; ">Fix</span></p>'```
```
<p><span style="display: inline-block; padding: 2px 9px; font-size: 14px; line-height: 16px; vertical-align: baseline; white-space: nowrap; background-color: #FF00FF; color: #ffffff; border-radius: 9px; ">Fix</span></p>