#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# 404. page not found / 500 internal server error
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("It worked!")

