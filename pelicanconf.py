#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'zjor'
SITENAME = u'Engineering notes'
# SITEURL = 'https://zjor.gihub.io'
SITEURL = ''
THEME = 'pelican-simplegrey'
STATIC_PATHS = ['static/images']

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/zjor'),)

DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS='UA-72137960-1'
DISQUS_SITENAME='zjor'
TWITTER_USERNAME='zjor'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
