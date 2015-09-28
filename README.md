# Flex

A minimalist [Pelican](http://blog.getpelican.com/) theme.

## Features

- Mobile First
- Responsive
- Semantic
- SEO Best Practices
- Open Graph
- Rich Snippets (JSON-LD)

## Integrations

- AddThis
- Disqus
- Google Analytics
- Google Tag Manager
- StatusCake

## Custom settings

See what you can customize.

> Maybe some Pelican settings not work properly.

| Name | What does it do? |
|:----:|------------------|
| SITETITLE | Site title to show in sidebar. |
| SITESUBTITLE | Short description to show below subtitle. |
| SITELOGO | Profile picture to show above author name (absolute url). |
| SITEDESCRIPTION | Site description to use in meta tags. |
| OG_LOCALE | language_TERRITORY for Open Graph. Default is `en_US`. |
| COPYRIGHT_YEAR | Copyright year to display on footer. |
| CC_LICENSE | Creative Commons License to show on footer. |
| MENUITEMS | A list of tuples (Title, URL) for additional menu items to appear on main menu. |
| LINKS | A list of tuples (Title, URL) for links to appear on the sidebar menu. |
| SOCIAL | A list of tuples (name, URL) to appear in the "social" section. |
| MAIN_MENU | Show main menu. |
| ROBOTS | Robots meta tag value. |
| ADD_THIS_ID | AddThis public id. |
| DISQUS_SITENAME | Disqus website's shortname to activate Disqus. |
| GOOGLE_ANALYTICS | Activate Google Analytics. |
| GOOGLE_TAG_MANAGER | Activate Google Tag Manager. |
| STATUSCAKE | Show StatusCake Uptime badge on footer. |

### Example

```python
AUTHOR = 'Foo Bar'
SITEURL = 'http://yoursite.com'
SITENAME = 'Foo Bar\'s Blog'
SITETITLE = 'Foo Bar'
SITESUBTITLE = 'Web Developer'
SITEDESCRIPTION = 'Foo Bar\'s Thoughts and Writings'
SITELOGO = 'http://yoursite.com/img/profile.png'

FAVICON = SITEURL + '/images/favicon.ico'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2015
CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa') }

MAIN_MENU = True

ADD_THIS_ID = 'ra-77hh6723hhjd'
DISQUS_SITENAME = 'yoursite'
GOOGLE_ANALYTICS = 'UA-1234-5678'
GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'
STATUSCAKE = { 'trackid': 'your-id', 'days': 7 }
```

If you want a full working example take a look [here](https://github.com/alexandrevicenzi/blog/blob/master/pelicanconf.py).

### How main menu works?

If `MAIN_MENU = True`, the order is: Home, `MENUITEMS`, Atom and RSS if available.

### How sidebar menu works?

The order is Pages and `LINKS`. `LINKS` are shown in a new page.

### How social menu works?

All icons are provided by [Font Awesome](http://fortawesome.github.io/Font-Awesome/).

A set of icons have custom background, for this you must follow the names below:

- envelope-o (for email)
- facebook
- github
- github-alt
- google
- linkedin
- pinterest
- rss
- stack-overflow
- twitter
- youtube

Example:

```python
SOCIAL = (('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
          ('github', 'https://github.com/alexandrevicenzi'),)
```

If you need more icons, you will need to add a custom background to keep all icons similar.

## Custom File Metadata

| Name | What does it do? |
|:----:|------------------|
| Summarize | Enable Home summary. |
| Cover | Cover image for social sharing (absolute url). |
| og_locale | Open graph locale for article. |

By default, all article content is shown on Home.
If the article has a custom Summary, the custom summary is shown.
If the article has `Summarize: True` metadata, the default article summary is shown.

## Code Highlight

If you want to replace Pygments theme (default is GitHub) take a look at [Pygments Docs](http://pygments.org/) and replace `pygments.min.css`.

## Live example

You can see how things looks like [here](https://blog.alexandrevicenzi.com/flex-pelican-theme.html).

I'm using Flex in my [personal blog](http://blog.alexandrevicenzi.com/).

![Screenshot](https://github.com/alexandrevicenzi/Flex/blob/master/screenshot.png)

## License

MIT
