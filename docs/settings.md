# Settings

Note that some Pelican settings may not work properly.

Most settings were inherited from [Flex theme](https://github.com/alexandrevicenzi/Flex).
Look at [Flex's wiki page for settings](https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings).

## Theme

| Name | What does it do? |
|:----:|------------------|
| SITETITLE            | Site title to show in the sidebar.                                                  |
| SITESUBTITLE         | Short description to show below subtitle.                                           |
| SITELOGO             | Profile picture to show above author name (absolute URL).                           |
| SITEDESCRIPTION      | Site description to use in meta tags.                                               |
| BROWSER_COLOR        | Browser color configuration, based on [google developers reference][1].             |
| OG_LOCALE            | language_TERRITORY for Open Graph. Default is `en_US`.                              |
| COPYRIGHT_NAME       | Copyright name to display on the footer.                                            |
| COPYRIGHT_YEAR       | Copyright year to display on the footer.                                            |
| CC_LICENSE           | Creative Commons License to show on the footer. More details in [[CC License]].     |
| ROBOTS               | Robots meta tag value.                                                              |
| REL_CANONICAL        | If `True` emit canonical links, based on [google developers reference][5].          |
| HOME_HIDE_TAGS       | Hide article tags in Home.                                                          |
| DISABLE_URL_HASH     | If `True` hide URL hash.                                                            |
| PAGES_SORT_ATTRIBUTE | Allows specifying how page links will be sorted. 'title' by default.                |
| MAIN_MENU            | If `True` show the main menu.                                                       |
| MENUITEMS            | A list of tuples (Title, URL) for additional menu items to appear on the main menu. |
| LINKS                | A list of tuples (Title, URL) for links to appear on the sidebar menu.              |
| SOCIAL               | A list of tuples (name, URL) to appear in the "social" section.                     |
| CUSTOM_CSS           | Path to a CSS file. Need to be used with [EXTRA_PATH_METADATA][2].                  |
| USE_LESS             | Use LESS files instead of CSS (avoid on production, it's for testing purpose)       |
| USE_GOOGLE_FONTS     | If `False` disable Google fonts                                                     |
| FAVICON              | Path to favicon.ico                                                                 |
| PYGMENTS_STYLE       | Code Highlight style. [More info][3].                                               |
| ARTICLE_HIDE_TRANSLATION | Hide translation menu.                                                          |
| LINKS_IN_NEW_TAB     | Whether to open `LINKS` in a new window or not. If unset, `True`, `None` or `all` then all `LINKS` will open in a new window. If `external` only `LINKS` to external websites will open in a new window, internal links will open in the same window. With any other value (recommended `False`) all links will open in the same window. |

## Integrations

| Name | What does it do? |
|:----:|------------------|
| ADD_THIS_ID                      | AddThis public id.                                                     |
| DISQUS_SITENAME                  | Disqus website's shortname to activate Disqus.                         |
| DUOSHUO_SITENAME                 | [duoshuo](http://duoshuo.com/) website's shortname to activate.        |
| GOOGLE_ANALYTICS                 | Activate Google Analytics.                                             |
| GUAGES                           | Activate Guag.es analytics.                                            |
| GOOGLE_TAG_MANAGER               | Activate Google Tag Manager.                                           |
| GOOGLE_GLOBAL_SITE_TAG           | Activate Google Analytics 4.                                           |
| STATUSCAKE                       | Show StatusCake Uptime badge on the footer.                            |
| PIWIK_SITE_ID or MATOMO_SITE_ID  | ID for the monitored website.                                          |
| PIWIK_URL or MATOMO_URL          | URL to your Piwik/Matomo server - without ‘https://‘ at the beginning.  |
| ISSO_URL                         | URL of your Isso comment server. See [The Isso Docs](https://posativ.org/isso/docs/configuration/client/#data-isso) for details. |

## Plugins

| Name | What does it do? |
|:----:|------------------|
| GITHUB_CORNER_URL | Link to a Github repo to be displayed in the right top corner (see [Github Corners][4]). |

[1]: https://developers.google.com/web/fundamentals/design-and-ui/browser-customization/theme-color
[2]: http://docs.getpelican.com/en/stable/settings.html#path-metadata
[3]: https://github.com/alexandrevicenzi/Flex/wiki/Code-Highlight
[4]: https://github.com/tholman/github-corners
[5]: https://developers.google.com/search/docs/advanced/crawling/consolidate-duplicate-urls#specify-a-canonical-page
