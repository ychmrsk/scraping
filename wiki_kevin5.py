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
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries though!')
        
    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('------------------------------\n' + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")

