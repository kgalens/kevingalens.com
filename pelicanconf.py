#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site Info
AUTHOR = 'Kevin Galens'
SITENAME = 'Kevin Galens'
SITETITLE = "Kevin Galens"
SITESUBTITLE = "Software / Genomics / Data"
SITEURL = ''
THEME = 'theme'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

COPYRIGHT_NAME = "Kevin Galens"
COPYRIGHT_YEAR = "2020"

GITHUB_CORNER_URL = "https://github.com/kgalens"
FAVICON = "../theme/img/favicon.ico"

CC_LICENSE = {
    'slug': 'by',
    'version': '4.0',
    'name': 'Attribution'
}

# Site Configurations
DISPLAY_PAGES_ON_MENU = True
TAGS_SAVE_AS = None
TAG_SAVE_AS = None
USE_LESS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/kevingalens/'),
          ('github', 'https://github.com/kgalens'),
          ('flickr', 'https://www.flickr.com/photos/kevygee'),
          ('500px', 'https://500px.com/kgalens'),
          ('instagram', 'https://www.instagram.com/kevygee/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True