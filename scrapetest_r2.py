#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
# when cannot find the server, html is None,
# and html.read() calls AttributeError.
#    except URLError as e:
#        print("The server could not be found!")
#        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


if __name__ == '__main__':
    title = getTitle("http://www.pythonscraping.com/pages/page1.html")
    if title == None:
        print("Title could not be found.")
    else:
        print(title)

