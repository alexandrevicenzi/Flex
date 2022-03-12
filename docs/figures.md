# Figures and captions

Reflex has support for figures and captions in two formats:

`figure` and `figcaption` HTML elements:

``` html
<figure>
    <img src="img.jpg" />
    <figcaption>Caption</figcaption>
</figure>
```

A `div` with `figure` class and `p` with `caption` class:
``` html
<div class="figure">
    <img src="img.jpg">
    <p class="caption">Caption</p>
</div>
```

## Alignment

Add `align-left`, `align-center` or `align-right` class to align figures to left, center and right respectively.

## Border

Add `border` class to add a border around the figure and caption.

## Markdown

[markdown-captions](https://github.com/evidlo/markdown_captions) is recommended as it generates semantic `figure` and `figcaption` HTML elements, with support for tooltips and HTML classes.

An example of a center-aligned figure with caption, tooltip and border using *markdown-captions*:

``` markdown
![Caption](img.jpg "Tooltip on hover"){: .align-center .border}
```
