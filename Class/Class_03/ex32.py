# Luke Reed
# ex32.py
# 01/21/2016
# Loops and Lists

'''
some examples of lists
hairs = ['brown','blonde','red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]

start a list with '[' and end with a ']'
'''

# define a couple of lists
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# this first kind of 'for-loop' goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty oranges
# initialize the list
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

# we can also make 2D lists
# this is a list in a list 
two_d_list = [[1,2,3],[4,5,6]]