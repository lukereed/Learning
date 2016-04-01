#!/usr/bin/python
# Luke Reed
# ex40a.py
# 02/10/2016
# an introduction to OOP

mystuff = {'apple':"I AM APPLES!"}
print mystuff['apple']

# we can also reference mystuff.py:
import mystuff
mystuff.apple()

# we can also access variables in mystuff.py
print mystuff.tangerine

'''
# this is similar to using a dictionary
mystuff['apple']	# get apple from dictionary
mystuff.apple()		# get apple from the module
mystuff.tangerine 	# same thing, it's just a variable this time
'''

# next we can create a class just like the mystuff module
class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print "I AM CLASSY APPLES!"

# now we instantiate (create) a class by calling the class like it's a function
thing = MyStuff()
thing.apple()
print thing.tangerine

'''
# we now have three ways to get things from things
# dictionary style
mystuff['apple']

# module style
mystuff.apples()
print mystuff.tangerine

# class styles
thing = MyStuff()
thing.apples()
print thing.tangerine
'''
