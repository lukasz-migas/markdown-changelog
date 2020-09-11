# Welcome to Markdown Changelog's documentation

This Python package is an extension to the [Python Markdown](https://pypi.org/project/Markdown/) project which provides
the means to add `changelog` badges to your documentation. To do so, wrap the desired tag in double `;` tag so when its
processed by the markdown processor it can be turned into a `span` tag.

For example, the extension transforms the text directly below

```markdown
;;fix;; ;;change;; ;;improvement;; ;;efficiency;; ;;new;; ;;docs;; ;;remove;;
```

into:

```html
<p>
    <span class="badge badge-fix">Fix</span>
    <span class="badge badge-change">Change</span>
    <span class="badge badge-improvement">Improvement</span>
    <span class="badge badge-efficiency">Efficiency</span>
    <span class="badge badge-new">New</span>
    <span class="badge badge-docs">Docs</span>
    <span class="badge badge-remove">Remove</span>
</p>
```

which will be rendered as:

<p>
    <span class="badge badge-fix">Fix</span>
    <span class="badge badge-change">Change</span>
    <span class="badge badge-improvement">Improvement</span>
    <span class="badge badge-efficiency">Efficiency</span>
    <span class="badge badge-new">New</span>
    <span class="badge badge-docs">Docs</span>
    <span class="badge badge-remove">Remove</span>
</p>