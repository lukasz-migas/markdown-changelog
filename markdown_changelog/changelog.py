"""
Changelog

markdown_changelog.changelog
Markdown extension to easily display changelog badges in the document

The extension works by creating a span object and applying modifying its appearance to look like a badge with
labels such as `Fix`, `Change`, etc and a background color. You can create a badge by simply specifying it as such:

;;fix;;

Pre-defined keys include: fix, change, improvement, new, efficiency and docs

You can also specify the version by using the following syntax:

;;VERv1.2.3;;

for `v1.2.3`. The badge will be slightly larger with bold text.

Styling is available in docs/css/style.css. Set ``inline_style=True`` to
include badge styles directly in the generated HTML.

MIT license.
Copyright (c) 2020 Lukasz Migas <lukas.migas@yahoo.com>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import Tuple
from xml.etree.ElementTree import Element

import markdown
from markdown.inlinepatterns import SimpleTagInlineProcessor

# ;;changelog;;
CONTENT = r"((?:[^;]|(?<!={2});)+?)"
CHANGELOG = r"(;{2})(?!\s)%s(?<!\s)\1" % CONTENT

# colors
TEXT_COLOR = "#ffffff"  # white
FIX_COLOR = "#1f62c9"
CHANGE_COLOR = "#8a4b08"
IMPROVEMENT_COLOR = "#1f62c9"
NEW_COLOR = "#21843b"
EFFICIENCY_COLOR = "#087079"
DOCS_COLOR = "#663ab5"
REMOVED_COLOR = "#aa2933"
VERSION_COLOR = "#6f42c1"

# tag specification
# these are the pre-defined names that can be used
NORMAL_NAMES = ["fix", "change", "improvement", "new", "efficiency", "docs", "version", "remove"]
# these are the alternative names that can be used and will be auto-converted to the ones defined in `NORMAL_NAMES`
ALTERNATIVE_NAMES = {
    "changes": "change",
    "changed": "change",
    "improved": "improvement",
    "improvements": "improvement",
    "enhancement": "improvement",
    "enhanced": "improvement",
    "enhancements": "improvement",
    "documentation": "docs",
    "doc": "docs",
    "feature": "new",
    "removed": "remove",
    "delete": "remove",
    "deleted": "remove",
}


def _get_inline_style(text_color: str, bg_color: str, is_version: bool, round_corners: bool) -> str:
    """Get inline style"""
    style = {
        "display": "inline-block",
        "padding": "2px 9px",
        "font-size": "16px" if is_version else "14px",
        "line-height": "18px" if is_version else "16px",
        "vertical-align": "baseline",
        "white-space": "nowrap",
        "text-align": "center",
        "background-color": f"{bg_color}",
        "color": f"{text_color}",
        "border-radius": "4px" if round_corners else "2px",
        "font-weight": "600",
    }
    if is_version:
        style.update({"min-width": "75px"})

    _style = []
    for key, value in style.items():
        _style.append(f"{key}: {value}; ")
    return "".join(_style)


def _set_inline_style(el: Element, text_color: str, bg_color: str, is_version: bool, round_corners: bool):
    """Set inline style"""
    el.set("style", _get_inline_style(text_color, bg_color, is_version, round_corners))


def _parse_tag(tag: str) -> Tuple[str, str, bool]:
    """Parse tag name to ensure it matches the registered names"""
    is_version = False
    text = tag
    if tag.startswith("VER"):
        text = tag[3:]
        text = text.strip()
        is_version, tag = True, "version"

    tag = tag.lower()
    _tag = ALTERNATIVE_NAMES.get(tag, tag)
    if not is_version and tag not in NORMAL_NAMES:
        text = _tag

    return _tag, text, is_version


class ChangelogProcessor(SimpleTagInlineProcessor):
    """Handle mark patterns."""

    def __init__(self, config, pattern, tag, md):
        """Initialize."""

        self.config = config
        super(ChangelogProcessor, self).__init__(pattern, tag)
        self.md = md

        # settings
        self._auto_capitalize = bool(self.config.get("auto_capitalize", True))
        self._inline_style = bool(config.get("inline_style", False))
        self._rounded_corners = bool(config.get("rounded_corners", True))
        self._colors = {
            "text": config.get("text_color", TEXT_COLOR),
            "fix": config.get("fix_color", FIX_COLOR),
            "change": config.get("change_color", CHANGE_COLOR),
            "improvement": config.get("improvement_color", IMPROVEMENT_COLOR),
            "efficiency": config.get("efficiency_color", EFFICIENCY_COLOR),
            "new": config.get("new_color", NEW_COLOR),
            "docs": config.get("docs_color", DOCS_COLOR),
            "version": config.get("version_color", VERSION_COLOR),
            "remove": config.get("remove_color", REMOVED_COLOR),
        }

    def _get_colors(self, tag: str):
        """Get text and background color based on tags"""
        return self._colors["text"], self._colors.get(tag.lower(), NEW_COLOR)

    def _get_class(self, tag: str):
        """Get text representing the classes set on the span object"""
        klass = f"badge badge-{tag}"
        if not self._rounded_corners:
            klass += " badge-square"
        return klass

    def handleMatch(self, m, data):
        """Parse patterns"""
        el, start, end = super(ChangelogProcessor, self).handleMatch(m, data)
        if hasattr(el, "text"):
            tag, text, is_version = _parse_tag(el.text)
            el.text = text
            # set style
            if self._inline_style:
                _set_inline_style(
                    el, *self._get_colors(tag), is_version=is_version, round_corners=self._rounded_corners
                )
            else:
                el.set("class", self._get_class(tag))

            # auto-capitalize the tag
            if self._auto_capitalize and not is_version:
                el.text = text.capitalize()

        return el, start, end


class ChangelogExtension(markdown.Extension):
    """Add the mark extension to Markdown class."""

    def __init__(self, **kwargs):
        """Initialize."""

        # instantiate config
        self.config = {
            "inline_style": [False, "Set CSS style inline rather than requiring separate CSS file - Default: False"],
            "auto_capitalize": [True, "Capitalize the tag name - Default: True"],
            "rounded_corners": [True, "Round badge corners - Default: True"],
            "text_color": [TEXT_COLOR, f"Color of the text - Default: {TEXT_COLOR}"],
            "fix_color": [FIX_COLOR, f"Background of the `Fix` tag - Default: {FIX_COLOR}"],
            "change_color": [CHANGE_COLOR, f"Background of the `Change` tag - Default: {CHANGE_COLOR}"],
            "improvement_color": [
                IMPROVEMENT_COLOR,
                f"Background of the `Improvement` tag - Default: {IMPROVEMENT_COLOR}",
            ],
            "new_color": [NEW_COLOR, f"Background of the `New` tag - Default: {NEW_COLOR}"],
            "docs_color": [DOCS_COLOR, f"Background of the `Docs` tag - Default: {DOCS_COLOR}"],
            "efficiency_color": [EFFICIENCY_COLOR, f"Background of the `Efficiency` tag - Default: {EFFICIENCY_COLOR}"],
            "version_color": [VERSION_COLOR, f"Background of the `Version` tag - Default: {VERSION_COLOR}"],
            "remove_color": [REMOVED_COLOR, f"Background of the `Remove` tag - Default: {REMOVED_COLOR}"],
        }

        # override defaults with user settings
        for key, value in kwargs.items():
            self.setConfig(key, str(value))

        markdown.Extension.__init__(self, **kwargs)

    def extendMarkdown(self, md):
        """Insert `<mark>test</mark>` tags as `==test==`."""
        md.registerExtension(self)

        config = self.getConfigs()
        changelog = ChangelogProcessor(config, CHANGELOG, "span", md)
        md.inlinePatterns.register(changelog, "changelog", 65)


# noinspection PyPep8Naming
def makeExtension(**kwargs):
    """Return extension."""
    return ChangelogExtension(**kwargs)
