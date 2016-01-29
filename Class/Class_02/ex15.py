#!/usr/bin/python

# Luke Reed
# ex15.py
# 01/14/2016
# Reading Files

from sys import argv

script, filename = argv

# the command 'open' will load your file
txt = open(filename)

# print the filename
print "Here's your file %r:" % filename
# 'filename'.read() will read the text document
print txt.read()

# repeat the process again using 'raw_input()'
print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)

print txt_again.read()
