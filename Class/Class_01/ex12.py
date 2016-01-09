# Luke Reed
# ex12.py
# 01/07/2016
# Prompting People

# Basically the same as ex11.py, but more efficient
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall, and %r heavy." % (
	age, height, weight)
