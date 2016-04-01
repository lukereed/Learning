#!/usr/bin/python

# Luke Reed
# ex33.py
# 01/21/2016
# While Loops

# A while loop will keep executing the code block as long as the boolean expression
# is it using is true

# you must be very careful not to create an infinite loop

i = 0
numbers = []

while i < 6: 	# declare boolean stopping criteria
	print "At the top i is %d" % i
	numbers.append(i)	# add the i'th element to 'numbers'

	# increase the index by 1
	i += 1

	print "Numbers now:", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

# now use a for loop to print the elements of the list one by one
for num in numbers:
	print num
