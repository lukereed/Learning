#!/usr/bin/python

# Luke Reed
# ex38.py
# 01/21/2016
# Doing Things to Lists

# define an initial string to build a list from
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# split the 'ten_things' string into the list 'stuff' by using spaces
stuff = ten_things.split(' ')
# define a secondary list to add from
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
	# populates the 'next_one' variable with the final value of more_stuff
	# and removes it from 'more_stuff'
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	# add 'next_one' to 'stuff' list
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]		# prints element 1 (the second) in the list
print stuff[-1] 	# this will give you the last element
print "stuff.pop= ", stuff.pop() # populates the last value in the list and removes it
print ' '.join(stuff) 	# joins all values of 'stuff' with a spaces between values
print '#'.join(stuff[3:5]) 	# joins index 3 up to but not including index 5
