#! /usr/bin/env python
# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(articleURL):
    global pages
    baseURL = 'http://en.wikipedia.org'
    html = urlopen(baseURL + articleURL)
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")

