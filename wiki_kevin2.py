#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/Kevin_Bacon'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

# for link in bsObj.findAll('a'): 
# => 1. in div-tag, id is bodyContent
#    2. URL don't include colon(:)
#    3. URL startswith /wiki/

for link in bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

