#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'BrainHack Magdeburg'
SITENAME = u'BrainHack Magdeburg'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

#
# Configure Pelican a bit
#
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'jinja2content']
SITEMAP = { 'format': 'xml' }

THEME = 'theme'
DIRECT_TEMPLATES = [] # unset all templates
STATIC_PATHS = ['css']

PATH_METADATA = 'pages/(?P<path>.*)\..*'

MENUITEMS = (('home', 'index.html'),
             ('projects', 'projects.html'),
             ('details', 'details.html'),
)

FEED_ALL_ATOM = None
AUTHOR_SAVE_AS = False
