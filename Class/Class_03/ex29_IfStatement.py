#!/usr/bin/python

# Luke Reed
# ex29.py
# 01/21/2016
# What If

# a script to introduce the 'if-statement'

people = 20
cats = 30
dogs = 15


# first 'if' then a boolean statement followed by a ':'
if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

# the '+=' command will add to the existing variable
# this calls the "increment by" operator
# this can also be used for -= and many other operators
dogs += 5	# this is equivalent to 'dogs = dogs + 5'

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."


if people == dogs:
	print "People are dogs."
