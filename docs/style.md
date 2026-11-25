# Styling

The extension emits badge spans with classes such as `badge-fix` and
`badge-version`. Copy [the stylesheet](css/style.css) into your documentation
site's docs directory, then add its path to the site's extra CSS setting. The
stylesheet defines the default colors and spacing. Set `inline_style=True` if
your site cannot load a separate stylesheet; custom color options apply to
inline styles.

## Release timeline

The stylesheet also includes an optional layout for release notes. Each release
has a version badge, a date, and a list of entries:

```html
<div class="changelog-timeline">
  <section class="changelog-release">
    <div class="changelog-release-header">
      <span class="badge badge-version">v1.2.3</span>
      <time datetime="2026-11-19">November 19, 2026</time>
    </div>
    <ul class="changelog-entries">
      <li><span class="badge badge-new">New</span><span>Add support for multiple projects.</span></li>
      <li><span class="badge badge-fix">Fix</span><span>Keep long release notes aligned when they wrap.</span></li>
    </ul>
  </section>
</div>
```

Here is the rendered layout:

<div class="changelog-timeline">
  <section class="changelog-release">
    <div class="changelog-release-header">
      <span class="badge badge-version">v1.2.3</span>
      <time datetime="2026-11-19">November 19, 2026</time>
    </div>
    <ul class="changelog-entries">
      <li><span class="badge badge-new">New</span><span>Add support for multiple projects.</span></li>
      <li><span class="badge badge-fix">Fix</span><span>Keep long release notes aligned when they wrap.</span></li>
    </ul>
  </section>
</div>

The layout inherits text and link colors from the site theme and stacks entries
on narrow screens. The HTML uses explicit spans because Markdown processors
generally do not parse the marker syntax inside raw HTML blocks.
