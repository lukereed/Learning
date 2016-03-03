#!/usr/bin/python
# Luke Reed
# class_05.py
# 02/10/2016
# an introduction to OOP

# five major collection classes used in python
# 1:  list
# 2:  tuple
# 3:  dictionary
# 4:  generator (pseudo collection status -- only generates one by one)
# 5:  set

# how do we create an empty list
#  (a) li = []
#  (b) li = list()			# standard OOP syntax
#  JAVA aside				li = new List()
#  C++ aside:				list li() OR list* pli = new list()
#  JAVA correction list 	li = new List()

#  (b)	li = list() 	# list is a class in Python, li is an instance

# empty tuple?
# tu = () OR tu = tuple()

# empty dictionary
# di = {} OR di = dict()

# empty set
# se = set()


# make a list of sqrt(x) for x = 10 to 30 (not 30)
import math
li = [math.sqrt(el) for el in range(10,30)]

def dirpub(atype):
	return [el for el in dir(atype) if not el.startswith('_') and not el.endswith('_')]

dir(math)		# this will show all modules of math
dirpub(math)	# this will show all but the public modules of math

# pythonic way to create a list is:
# li = [math.sqrt(el) for el in range(01,30)]

li = [1,2,3]
li = ['a',',b','c']

# we can also avoid multiple quotes
li = 'chicago losAngeles sanFrancisco atlanta'.split()		# split by spaces
li = 'chicago,losAngeles,sanFrancisco,atlanta'.split(',')	# split by commas

li = [el.strip() for el in 'chicago, los angeles, san francisco, atlanta'.split(',')]

# don't do it this way!!!!
for el in 'chicago, los angeles, san francisco, atlanta'.split(','):
	li.append(el.strip())

di = {'ORD' : 'chicago o\'hare', 'LAX' : 'los angeles', 'SFO' : 'san francisco', 'ATL' : 'atlanta'}
print di
# {'SFO': 'san francisco', 'ORD': "chicago o'hare", 'LAX': 'los angeles', 'ATL': 'atlanta'}

for k,v in di.items():
	print(k,v)

'''
('SFO', 'san francisco')
('ORD', "chicago o'hare")
('LAX', 'los angeles')
('ATL', 'atlanta')
'''

for k in sorted(di.keys()):
	print (k, di[k])
'''('ATL', 'atlanta')
('LAX', 'los angeles')
('ORD', "chicago o'hare")
('SFO', 'san francisco')
'''

# we can also write error functions
def divide_by(a,b):
	if (b == 0): raise ZeroDivisionError('integer division by zero')
	return(a / b)
'''
>>> divide_by(3,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in divide_by
ZeroDivisionError: integer division by zero
'''

# now let's take a more in depth look at the to_roman.py file
import sys
s = '1:I,4:IV,5:V,9:IX,10:X'
''' >>> s
'1:I,4:IV,5:V,9:IX,10:X' '''

li_an_1 = s.split(',')
''' >>> li_an_1
['1:I', '4:IV', '5:V', '9:IX', '10:X'] '''

# what IS PEP 0008 ??
# it's a Python Enhancement Proposal (somebody has an idea to enhance Python)
# it's a bunch of style guidelines
# have to use ''' type commenting for every function
# can even put test code in ''' comments
# '#' sign commenting shouldn't be necessary as code should be easy to read
# it is a very easy way to exclude portions of code

# PEP 0008 --- your Pycharm code should have no warnings
# doctest  --- your code should document input/output for its functions and use doctest to test them


##########################################################################

# Object Oriented Programming (OOP)!!!
s = 'hello'
x = 10
f = 3.5
li = '1 2 3'.split()
'''
>>> type(s)
<type 'str'>
>>> type(x)
<type 'int'>
>>> type(f)
<type 'float'>
>>> type(li)
<type 'list'>
'''
# All of these are classes in Python
# ALL of these have data!
# also, ALL of these have methods (functions that do things)

tu = tuple(li)

# when we want to write our own classes, then...
#   they have to have data
#   and they have to have methods
#   and, if we want them to work nicely, we have to define some standard methods

# start with a circle class
# circle data?
# circumference, radius, diameter, area, center, outline color, fill color
# radius and center are absolutely necessary
# but let's start with just the center

class circle:
	def __init__(self, radius, center=(0,0)):		# need to define an initialization
		self._radius = radius		# not completely right --- should have "private" data
		self._center = center		# the '_' makes the variable private
	def __str__(self):
		return 'circle[r={0},d={1},circ={2},area={3:.2f},center={4}]'.format(self.radius(),
															 				 self.diameter(),
															 				 self.circumference(),
															 				 self.area(),
															 				 self.center())
	def radius(self):			return self._radius
	def diameter(self):			return self._radius * 2
	def circumference(self):	return self._radius * 2 * math.pi
	def perimeter(self):		return self.circumference()
	def area(self):				return self._radius ** 2 * math.pi
	def center(self):			return self._center

c = circle(4)
'''
>>> type(c)
<type 'instance'>
>>> isinstance(c,float)
False
>>> isinstance(c,circle)
True
>>> c = circle(4)
>>> print(c)
circle[radius=4]

>>> c2 = circle(66)
>>> print(c2)
circle[radius=66]

>>> c6 = circle(6)
>>> print(c6)
circle[r=6,d=12,circ=37.6991118431,area=113.10]
'''

# python is dynamic, but it is strongly typed (we must make sure everything returned is the same type)
# what is the address of circle c ?
id(c)
# 4555436112

# what is the base 16 (hex) address of circle c ?
hex(id(c))
# '0x10f867050'

# what is the address of circle c2 ?
hex(id(c2))
# '0x10f867320'

hex(id(c)) == hex(id(c2))
# False


# next we will do a rectangle class
# data for rectangle?
#		len, wid, perimeter, area, (center, outline color, fill color)

class rectangle:
	def __init__(self, length, width):
		self._length = length
		self._width = width
	def __str__(self):
		return 'rectangle[l={0},w={1},p={2},a={3}]'.format(self.length(),
														self.width(),
														self.perimeter(),
														self.area())
	def length(self):		return self._length
	def width(self):		return self._width
	def perimeter(self):	return (self._length + self._width) * 2
	def area(self):			return self._length * self._width


''' LOOK AT CLASS NOTES TO FIX THIS
# now let's make a square class (child class)
class square(rectangle):		# inherits rectangle parent class
	def __init__(self, side):
		super(square, self).__init__(side,side)
	def __str__(self):
		return 'square[{0}]'.format(super(self, square).__str__())
	def side(self):			return super(self, square).length()
'''

# composition is an alternative to inheritance
#		but it takes more work
#		also known as delegation
class square:
	def __init__(self,side):
		self._rect = rectangle(side,side)
	def __str__(self):
		return 'square[side={0},peri={1},area={2}]'.format(self._rect.length(),
														   self._rect.perimeter(),
														   self._rect.area())
	def side(self):
		return self._rect.length()
	def perimeter(self):
		return self._rect.perimeter()
	def area(self):
		return self._rect.area()
'''
>>> sq = square(3)
>>> print(sq)
square[side=3,peri=12,area=9]
'''

# now we can make a shapes super class
# this is the class that will handle the center location

# use the django project package
