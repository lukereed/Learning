# Luke Reed
# Python Class 04

# When using python 2.7 we can write it slightly differently to
# allow for use with python 3.0

# import needed libraries
import time

'''
Class Overview

Lists
Tuples
Dictionaries
'''

# Lists
# two ways to create a list
li = []
li_alt = list()
type(li)	#<type 'list'>
# We can append items to lists
li.append('banana')
li.append('cherry')
li.append('apple')
li 		#['banana', 'cherry', 'apple']

li_alt = ['date', 'guava', 'apple', 'kiwi']
li_alt	#['date', 'guava', 'apple', 'kiwi']

# we can also sort lists
# this will sort alphabetically or numerically depending on type
sorted(li)		#['apple', 'banana', 'cherry']
li.sort()		#['apple', 'banana', 'cherry']


# we can also list out all the directory options
dir(li)
'''['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
 '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
 '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
 '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
 '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
 'remove', 'reverse', 'sort']
'''

# we can also count
li.count('apple')		#1
li.count('elephant')	#0

li.append('apple')		#['apple', 'banana', 'cherry', 'apple']
li.sort()
li 						#['apple', 'apple', 'banana', 'cherry']
len(li)					#4

# we can add in elements of various types
li.append(42)
li 						#['apple', 'apple', 'banana', 'cherry', 42]
li.append(2.718281)
# we can also insert a list within another list
li.append(li_alt)
li 						#['apple', 'apple', 'banana', 'cherry', 42, 2.718281, ['date', 'guava', 'apple', 'kiwi']]
len(li)					#7

li_new = []
li_new.extend(li_alt)	#['date', 'guava', 'apple', 'kiwi']
# we can now use 'pop' to remove and store an element of a list
item = li_new.pop()
item 					#kiwi'
li_new					#['date', 'guava', 'apple']
item = li_new.pop()
item 					#'apple'
li_new 					#['date', 'guava']

# now lets redefine our li_alt list
li_alt = ['date','guava','apple','kiwi']
li_alt.insert(2,'banana')	# inserts before elment 2
li_alt 					#['date', 'guava', 'banana', 'apple', 'kiwi']

# now we can play with numbers
li_num = [0,1,2,3,4,5,6,7,8,9]
li_num 					#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# re do li_num
for el in range(0,100):		# el is short for 'element'
	li_num.append(el)	# we now have a list from 0 to 99

# now lets only get the odd numbers
li_num = []
for el in range(0,100):
	if el % 2 == 1:
		li_num.append(el)	# we now have a list of the odd numbers from 0 to 99

# now lets get the square of the even numbers
li_num  = []
for el in range(0,100):
	if el % 2 == 0:
		li_num.append(el*el)


# Everything we have done up until this point has been the old way
# No we will do it with list comprehension
# Note: There are also Set comprehensions, Tuple comprehensions, and
# 		dicitionary comprehensions

# let's do this with a single line approach
#          operation    loop                   condition
li_ev_sq  = [el * el for el in range(0,100) if el % 2 == 0]
li_odd_sq = [el * el for el in range(0,100) if el % 2 == 1]
li_all    = [el for el in range(0,100)]

# now we will test which way is faster
# let's write a function for timing
code = '[el * el for el in range(0,100)]'
exec(code)
def time_code(code):
	then = time.clock()
	exec(code)
	now = time.clock()
	return (now - then)

# now we want to know all odd numbers that are divisible by 7
li_odd_divbyseven = [el for el in range(0,100) if el % 2 == 1 and el % 7 == 0]
li_odd_divbyseven		#[7, 21, 35, 49, 63, 77, 91]

# lets make a function to return the sum of a list
def sum_list(li):
	return sum(li)
sum(li_odd_divbyseven)		#343
# now we can do this the hard way
def sum_list_harder(li):
	total = 0
	for el in li:
		total += el
	return total
sum_list_harder(li_odd_divbyseven)		#343


# Lists are mutable as they can be changed
# A list is a bad candidate for a dictionary key
#		We want dictionary keys to be static and remain the same
# Strings are unmutable
# 		You cannot change a string
#		You can make a new string from an old string, though
# NEVER USE 'list' or other keywords as variables

#############################################################################

# Tuples
tu = ()
tu = tuple()
type(tu)		#<type 'tuple'>

# now we can see all the different directory options
dir(tu)

# write a function that returns ONLY the public functions of a type
def dirpub(atype):
	return [el for el in dir(atype) if not el.startswith('_') and not el.endswith('_init__')]
# now look at the public functions of different types
dirpub(tu)	#['count', 'index']
dirpub(li)	#['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dirpub(str)	#['_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# if you make a utility file called utils.py
#	and if you put dirpub in that file
#	and if you say import utils
#	then you use it like this:	utils.dirpub(atype)
# but
# if you say from utils import dirpub
#	then you can use it like this: dirpub(atype)

tu = (1,2,3)		#(1, 2, 3)
# length of this tuple ?
len(tu)				#3
tu[2]				#3
# index of the element whose value is 1
tu.index(1)			#0
tu.index(7)			# this will throw an error

# we can make our own value error
raise ValueError("I'm just doing this for fun!")


# create a tuple
# get the length of the tuple
# get the value at an index
# get the index for a given value (if not found, a ValueError will be raised)
tu_mult = (1,2,1,3,1,4,1,5)
tu_mult.index(1)		#0
tu_mult.index(3,1)

li = [ el for el in range(20,100,10)]
li 				#[20, 30, 40, 50, 60, 70, 80, 90]
def min_max(li):
	small = min(li)
	big = max(li)
	return (small, big)
min_max(li)		#(20, 90)

min_li, max_li = min_max(li)
min_li		#20
max_li		#90

# DO NOT DO THE FOLLOWING!!!!!
a_tuple = min_max(li)
min_li = a_tuple[0]
max_li = a_tuple[1]

# LAB EXERCISE
# Fibonacci numbers:  1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# fibo_n = fibo_n-1 + fibo_n-2, fibo_0 = 1, fibo_1 = 1

# write a function that returns the nth fibonacci term
def fibo_n(n):
	a,b = 1,1 	#made a tuple (1,1) and unpacked it, tu[0] -> a and tu[1] -> b
	while n > 0:
		a,b = b,a+b
		n -= 1
	return b
fibo_n(5)		#13 		--> This is correct!

# now we can use the function to create a series list
fibo_series = [fibo_n(el) for el in range(15)]
fibo_series 	#[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]


# What is a generator??
# it's like a list comprehension, but it is LAZY no eager
gen_fibo = (fibo_n(el) for el in range(15))
type(gen_fibo)		#<type 'generator'>
next(gen_fibo)		#1
next(gen_fibo)		#2
next(gen_fibo)		#3
next(gen_fibo)		#5

# we must recreate the generator each time we use it
gen_fibo = (fibo_n(el) for el in range(15))
li = list(gen_fibo)


#############################################################################

# before we talk about dictionaries
# let's talk about SETS
li = [1,2,1,3,1,4,1,5,1,6]
se = set(li)		#set([1, 2, 3, 4, 5, 6])  --> A set removes duplicates

lise = list(se)
lise 				#[1, 2, 3, 4, 5, 6]

dirpub(se)			#['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# let's make a new set
senew = set()
senew.add('one')
senew.add('two')
senew.add('three')
senew.add('four')
senew.add('five')
senew				#set(['four', 'three', 'five', 'two', 'one'])  UNORDERED

senew_sub = ('three-fifths')
dirpub(set)			#['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

senew.add(senew_sub)
senew 				#set(['three', 'two', 'four', 'five', 'three_fifths', 'one'])


#############################################################################

# Now we can move on to dictionaries
di = {}
type(di)		#<type 'dict'>

dir(di)			#['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
dirpub(di)		#['clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']

# we can return the keys and the values separately
di.key()		#['john', 'joe', 'jack', 'jenny']
di.values()		#['123', '234', '456', '345']

# now we can sort them
sorted(di.keys())		#['jack', 'jenny', 'joe', 'john']
sorted(di.values())		#['123', '234', '345', '456']

from __future__ import print_function # python 2 code will print like python 3 code
print("one is {0} and two is {1}".format(1,2))

# now we want to print out all the values in alphabetical order
for k in sorted(di.keys()):
	print("{0} --- {1}".format(k,di[k]))
'''		CODE OUTPUT
jack --- 456
jenny --- 345
joe --- 234
john --- 123
'''

# To make the formatting nicer:
for k in sorted(di.keys()):
	print("{0:>5} --- {1}".format(k,di[k]))
'''
 jack --- 456
jenny --- 345
  joe --- 234
 john --- 123
'''

# what if I want to know the key and the value every time?
for k,v in di.iteritems():
	print("{0:>5} --- {1}", format(k,v))

# LAB:
# We want to convert numbers to Roman numerals
# 1920 --> MVM

# List 7   TUPLE ?    DICTIONARY ?
# a list would require every element to be input
# instead let's use a dictionary
di = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
def to_roman(year):		# year is 1999
	result = ""
	# but we actually want the keys in reverse order
	keys = sorted(di.keys())
	keys.reverse()
	idx = 0
	while (year > 0):
		if (keys[idx] >= year):
			result += di[keys[idx]]
			year -= keys[idx]
		else:
			idx += 1
	return result
to_roman(1999)


def to_roman(year):
	result = ""

# lists and splitting
li = 'apple banana cherry date'.split()
li 		#['apple', 'banana', 'cherry', 'date']

arabic_to_roman = 
roman = dict([(int(k),v) for k,v in [e.split(':') for e in arabic_to_roman.split(',')]])
arabic = dict([v,int(k)) for k,v in [e.split(':') for e in arabic_to_roman.split(',')]])


# SLICING
# A powerful way to get portions of a list
li.append('elephant')
li.append('jaguar')
li.extend('one two three'.split())
li 			#['apple', 'banana', 'cherry', 'date', 'elephant', 'jaguar', 'one', 'two', 'three']
li[1:4] 	#['banana', 'cherry', 'date']
li[:4] 		#['apple', 'banana', 'cherry', 'date']		--> Takes first four
li[-1]		#'three'					--> Takes last one
li[-3:] 	#['one', 'two', 'three']	--> Takes last three
li[::2]		#['apple', 'cherry', 'elephant', 'one', 'three']	--> Up to the last two
li[1::2]	#['banana', 'date', 'jaguar', 'two']
li[::-1]	#['three', 'two', 'one', 'jaguar', 'elephant', 'date', 'cherry', 'banana', 'apple']		--> Reverses the list

def slice_list(li,start=None,stop=None,step=None):
	return li[start:stop:step]
slice_list(li,step=-1)			#['three', 'two', 'one', 'jaguar', 'elephant', 'date', 'cherry', 'banana', 'apple']
slice_list(li,step=2)			#['apple', 'cherry', 'elephant', 'one', 'three']
slice_list(li,start=1,step=2)	#['banana', 'date', 'jaguar', 'two']

#############################################################################

# HOMEWORK
# Write a game to play Battleship
# Challenging Lab to put it all together

# Then, take some scripts you have (BASH) and convert it to Python
# Next Week we're doing OOP (Object Oriented Programming)
# classes, methods, variables, inheritance, composition, design patterns, abstract classes

# Head First Design Patters (great book with bad cover)
