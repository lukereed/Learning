# Luke Reed
# WebScrape.py
# 03/03/2016

import urllib
import re 			# regular expressions

# htmlfile = urllib.urlopen("https://www.google.com")
# htmlfile = urllib.urlopen("http://www.cnn.com")
# htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s=GOOG&ql=0")
htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s=aapl")
	# '?' means you're accessing a variable and '&' means multiple
htmltext = htmlfile.read()

# take the source tag from the element you want and replace the element you want to extract with '(.+?)'
# regex = '<span id="yfs_l84_aapl">100.95</span>'
regex = '<span id="yfs_l84_aapl">(.+?)</span>'
pattern1 = re.compile(regex)		# compile method is not required

# similar procedure to grab the title header
title = '<title>(.+?)</title>'
pattern2 = re.compile(title)

price = re.findall(pattern1, htmltext)
name  = re.findall(pattern2, htmltext)

print price
print name