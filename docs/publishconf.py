import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = 'http://flex.alxd.me/blog'

RELATIVE_URLS = False

USE_LESS = False

GOOGLE_ANALYTICS = "UA-55543164-6"

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
