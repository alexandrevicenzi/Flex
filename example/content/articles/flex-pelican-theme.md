Title: Flex: Responsive Pelican theme
Date: 2015-07-22 08:00
Modified: 2015-07-22 08:00
Category: News
Tags: pelican, python, theme
Slug: flex-pelican-theme
Cover: images/flex-screenshot.png

I just start a new fresh blog using [Pelican](http://getpelican.com). Sometimes choosing a theme for a new site is something difficult that takes time.

In the Pelican [theme gallery](http://www.pelicanthemes.com/), I couldn't find anything that I really liked to feet all my needs. So in the first time of the history, I choose to create my own theme. I never did this before.

Creating a theme for Pelican is quite easy, unlike Wordpress. You can take a look in the [Source Code of Flex](https://github.com/alexandrevicenzi/Flex).

But how Flex looks like? Well, you can see [this screenshot](images/flex-screenshot.png), but you already know how it looks like, you're looking at it. :D

I really care about SEO and integrations with Facebook, Google Plus and other social networks, so this theme offers some features:

- Mobile First
- Responsive
- Semantic
- SEO Best Practices
- Open Graph
- Rich Snippets (JSON-LD)

Maybe these features are not fully optimized, but I'll improve.

Flex also offers integrations with multiple services.

> **Tip:**

> You can easyly integrate with:

> - AddThis
> - Disqus
> - Google Analytics
> - Google Tag Manager
> - StatusCake

Flex is a theme built by a developer for developers, but of course, you can use for any purpose. In this scenario, Flex is able to create good styles for coding, outputs and samples.

If you need to show some program output you can use `samp` tag to look like this:

<samp>Done: Processed 4 articles, 0 drafts, 2 pages and 0 hidden pages in 0.22 seconds.</samp>

Or if you want multiple lines:

<samp>
             total       used       free     shared    buffers     cached
Mem:          5866       4674       1192        386          0       2404
-/+ buffers/cache:       2269       3596
Swap:        20480       1267      19213
</samp>

If you like to share code snippets, you can take advantage of [Pygments](http://pygments.org/) syntax highlighting:

```js
// Foo
var bar = 0;
```

```python
class Foo(object):
    def __init__(self, bar)
        self.bar = bar
```

```bash
ls *.jpg | xargs -n1 -i cp {} /external-hard-drive/directory
```

**Note:** The code block looks like GitHub’s colors.

You can add tables too:

Item     | Value
-------- | ---
Computer | $1600
Phone    | $12
Pipe     | $1

and how heading looks like?

# This is heading 1
## This is heading 2
### This is heading 3
#### This is heading 4
##### This is heading 5
###### This is heading 6

This examples are in Markdown. I'm not sure how it will look using reStructuredText. Keep in mind that Markdown allows you to add HTML tags. If you can create the same HTML syntax produced by Markdown using reStructuredText it will work.

You can take a look in the [source code of this page](https://raw.githubusercontent.com/alexandrevicenzi/blog/master/content/News/flex-pelican-theme.md) to know how to create rich examples.

Flex is my first attempt creating themes and there's no IE testing yet. You can check the [sources here](https://github.com/alexandrevicenzi/flex).

As soon as possible I will add this project to Pelican gallery.

Drop a comment if you like this theme, or [open an issue](https://github.com/alexandrevicenzi/Flex/issues) if you need a feature or found a bug.
