#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

#------------------------------------------------------------

url1 = "http://www.pythonscraping.com/pages/warandpeace.html"

html = urlopen(url1)
bsObj = BeautifulSoup(html, 'html.parser')
# <span class="red">NAME</span>
nameList = bsObj.findAll('span', {'class':'green'})
for name in nameList:
    print(name.get_text())

#------------------------------------------------------------

# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

# tag: 'span' in above example
# attributes: {'class':'green'} in above example
# recursive: True or False, default is True
# text: match or not with text contents of tag
# keywords: var=value like bsObj.findAll(id='title', class='text')

#------------------------------------------------------------

url2 = 'http://www.pythonscraping.com/pages/page3.html'
bsObj = BeautifulSoup(html, 'html.parser')

for child in bsObj.find('table', {'id':'giftList'}).children:
    print(child)

for sibling in bsObj.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

# cf. next_siblings <=> previous_siblings
#     next_sibling  <=> previous_sibling

#------------------------------------------------------------

# parent

print(bsObj.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

#------------------------------------------------------------

# regular expression

#------------------------------------------------------------

