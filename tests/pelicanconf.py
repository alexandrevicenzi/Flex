#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

PLUGIN_PATHS = ['../plugins']
PLUGINS = ['i18n_subsites']

JINJA_EXTENSIONS = ['jinja2.ext.i18n', 'jinja2.ext.autoescape', 'jinja2.ext.with_']

AUTHOR = u'Test'
SITEURL = u'http://localhost:8000'
SITENAME = u"Test Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Test'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = u'https://www.example.com/img/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'
BROWSER_COLOR = '#333'

ROBOTS = u'index, follow'

THEME = u'../'
PATH = u'content'
TIMEZONE = u'America/Sao_Paulo'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

LINKS = (('Portfolio', '//alexandrevicenzi.com'),)

SOCIAL = (('linkedin', 'https://br.linkedin.com/in/test'),
          ('github', 'https://github.com/test'),
          ('google', 'https://google.com/+Test'),
          ('rss', '//www.example.com/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

STATUSCAKE = {
    'trackid': 'test-test',
    'days': 7,
    'rumid': 1234,
}

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 150

DISQUS_SITENAME = "test-test"
GOOGLE_ANALYTICS = "UA-XXXXXX-X"
ADD_THIS_ID = 'ra-XX3242XX'

USE_LESS = True
