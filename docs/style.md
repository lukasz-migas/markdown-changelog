# Styling

Copy [the stylesheet](css/style.css) into your documentation site's `docs/css`
directory and add `css/style.css` to `extra_css`. The badge colors match the
extension's default inline colors. Set `inline_style=True` when a stylesheet
cannot be included; custom color options apply to inline styles only.

## Optional release timeline

The stylesheet also provides an opt-in layout. It inherits text and link colors
from the surrounding theme and stacks entries on narrow screens. The following
HTML works without any additional Markdown extensions:

```html
<div class="changelog-timeline">
  <section class="changelog-release">
    <div class="changelog-release-header">
      <span class="badge badge-version">v1.2.3</span>
      <time datetime="2026-11-19">November 19, 2026</time>
    </div>
    <ul class="changelog-entries">
      <li><span class="badge badge-new">New</span><span>Add support for multiple projects.</span></li>
      <li><span class="badge badge-fix">Fix</span><span>Keep long release notes aligned when they wrap onto another line.</span></li>
    </ul>
  </section>
</div>
```

<div class="changelog-timeline">
  <section class="changelog-release">
    <div class="changelog-release-header">
      <span class="badge badge-version">v1.2.3</span>
      <time datetime="2026-11-19">November 19, 2026</time>
    </div>
    <ul class="changelog-entries">
      <li><span class="badge badge-new">New</span><span>Add support for multiple projects.</span></li>
      <li><span class="badge badge-fix">Fix</span><span>Keep long release notes aligned when they wrap onto another line.</span></li>
    </ul>
  </section>
</div>

The `;;tag;;` syntax still works in normal Markdown. The HTML above uses spans
explicitly because Markdown processors do not generally process text inside
raw HTML blocks by default.
