# Table of contents documentation

## Markdown

Markdown has a [toc extension](https://python-markdown.github.io/extensions/toc/) that can be enabled and used directly.
Once enabled just add `[TOC]` in the markdown document where you want the table of contents to appear.

Configure the `toc` extension through `MARKDOWN` setting in `pelicanconf.py`:

``` python
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {
            "title": "Table of Contents"
        },
    },
}
```

Refer to [Markdown's toc extension documentation](https://python-markdown.github.io/extensions/toc/) for full settings.

If you use the [i18n_subsites plugin](https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites) you can override the table of contents" title:

``` python
import copy

I18N_SUBSITES = {
    "es": {
        "MARKDOWN": copy.deepcopy(MARKDOWN),  # copy to override later
    }
}
I18N_SUBSITES["es"]["MARKDOWN"]["extension_configs"]["markdown.extensions.toc"]["title"] = "Índice de contenidos"
```
