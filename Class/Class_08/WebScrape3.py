# Luke Reed
# WebScrape3.py
# 03/10/2016

import urllib
import re

symbolslist = ["aapl", "goog", "ibm"]

i = 0
while i < len(symbolslist):
	htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s=" + symbolslist[i] + "&ql=1")
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_' + symbolslist[i] + '">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern, htmltext)
	print "The current stock price of " + str(symbolslist[i]) + " is " + str(price)
	i += 1