#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
print(html.read())
