# Luke Reed
# WebScrape2.py
# 03/10/2016

import urllib
import re

htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s=goog&ql=1")
htmltext = htmlfile.read()

title = '<title>(.+?)</title>'
pattern1 = re.compile(title)

regex = '<span id="yfs_l84_goog">(.+?)</span>'
pattern2 = re.compile(regex)

name = re.findall(pattern1, htmltext)
price = re.findall(pattern2, htmltext)

print name
print price
