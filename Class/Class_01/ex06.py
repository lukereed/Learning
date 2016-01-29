#!/usr/bin/python

# Luke Reed
# ex06.py
# 01/07/2016
# Strings and Text

x = "There are %d types of people." % 10	# alternate variable reference --> %d refers to an integer
binary = "binary"	# setting a variable as a string
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # %s refers to a string

print x
print y

print "I said: %r." % x	# %r converts to string using repr()
print "I also said: '%s'." % y

hilarious = False	# boolean operator
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e	# string concatenation with '+'
