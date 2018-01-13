# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = 'Alexandre Vicenzi'
SITEURL = 'http://localhost:8000'
SITENAME = 'Flex'
SITETITLE = 'Flex'
SITESUBTITLE = 'The minimalist Pelican theme'
SITEDESCRIPTION = 'Flex - The minimalist Pelican theme.'
# SITELOGO = ''
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = '../'
PATH = 'content'
OUTPUT_PATH = 'blog/'
TIMEZONE = 'America/New_York'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
    ('github', 'https://github.com/alexandrevicenzi/Flex'),
    ('rss', '/blog/feeds/all.atom.xml'),
)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "flex-pelican"
ADD_THIS_ID = 'ra-55adbb025d4f7e55'

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-6625957038449899',
    'page_level_ads': True,
    'ads': {
        'aside': '8752710348',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '1124188687',
        'article_top': '',
        'article_bottom': '4843941849',
    }
}
