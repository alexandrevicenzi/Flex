Title: Flex 1.1.0
Date: 2015-10-07 08:00
Modified: 2015-10-07 08:00
Category: News
Tags: pelican, python, theme
Slug: flex-pelican-theme-update-1-1
Cover: images/flex-screenshot.png

I've made the [Flex theme](https://github.com/alexandrevicenzi/Flex) a time ago. For my surprise, many people are using it. I feel thankful for this.

So, after some new blogs with this theme, I got issues and PRs on GitHub from these new users. This weekend I had some free time and I release the [second version](https://github.com/alexandrevicenzi/Flex/releases/tag/v1.1) of Flex (aka v1.1).

This new version doesn't include nothing so special, just some bug fix and a new setting to allow custom CSS stylesheets.

The new custom setting can be used like this:

```python
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'
```

I would like to thank all who helped in this new version.
