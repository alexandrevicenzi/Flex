# Flex

A minimalist [Pelican](http://blog.getpelican.com/) theme.

## Features

- Mobile First
- Responsive
- Semantic
- SEO Best Practices

## Integrations

- Disqus
- Google Analytics
- Google Tag Manager
- StatusCake

## Custom settings

See what you can customize.

Maybe some Pelican settings not work properly.

| Name | What does it do? | Code |
|:----:|------------------|:----:|
| AUTHOR_SHORT_DESC | Short description to show below author name. | `AUTHOR_SHORT_DESC = 'Web Developer` |
| AUTHOR_IMG_URL | Profile picture to show above author name. | `AUTHOR_IMG_URL = '/static/img/me.png'` |
| COPYRIGHT_YEAR | Copyright year to display on footer. | `COPYRIGHT_YEAR = 2015` |
| CC_LICENSE | Creative Commons License to show on footer. | `CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa')` |
| MENUITEMS | A list of tuples (Title, URL) for additional menu items to appear on main menu. | Same as Pelican docs. |
| LINKS | A list of tuples (Title, URL) for links to appear on the sidebar menu. | Same as Pelican docs. |
| SOCIAL | A list of tuples (name, URL) to appear in the "social" section. | See below. |
| MAIN_MENU | Show main menu. | `MAIN_MENU = True` |
| DISQUS_SITENAME | Disqus website's shortname to activate Disqus comment system. | `DISQUS_SITENAME = 'yoursite'` |
| GOOGLE_ANALYTICS | Set to ‘UA-XXXX-YYYY’ to activate Google Analytics. | `GOOGLE_ANALYTICS = 'UA-1234-5678'` |
| GOOGLE_TAG_MANAGER | Set to ‘GTM-XXXXXX’ to activate Google Tag Manager. | `GOOGLE_TAG_MANAGER = GTM-ABCDEF` |
| STATUSCAKE | Show StatusCake Uptime badge on footer. | `STATUSCAKE = { 'trackid': 'your-id', 'days': 7 }` |

### How main menu works?

If `MAIN_MENU = True`, the order is: Home, `MENUITEMS`, Atom and RSS if available.

### How sidebar menu works?

The order is Pages and `LINKS`. `LINKS` are shown in a new page.

### How Social menu works?

All icons are provided by [Font Awesome](http://fortawesome.github.io/Font-Awesome/).

A set of icons have custom background, for this you must follow the names above:

- email
- facebook
- github
- github-alt
- google
- linkedin
- pinterest
- rss
- twitter
- youtube

Example:

```python
SOCIAL = (('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
          ('github', 'https://github.com/alexandrevicenzi'),)
```

If you need more icons, you will need to add a custom background to keep all icons similar.

## Custom File Metadata

| Name | What does it do? | Code |
|:----:|------------------|:----:|
| Summarise | Enable Home summary | `Summarise: True` |

By default, all article content is shown on Home.
If the article has a custom Summary, the custom summary is shown.
If the article has Summarise metadata, the default article summary is shown.

## Live example

You can find a demo [here](http://blog.alexandrevicenzi.com/).

## License

MIT
