Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # four major collection classes used in Python
>>> # 1:  list
>>> # 2:  tuple
>>> # 3:  dictionary
>>> # 4:  (generator -- pseudo collection status) -- only generates one by one
>>> # 5:  set
>>> 
>>> # how do we create an empty list?
>>> #  (a) li = []
>>> #  (b) li = list()    # standard OOP syntax
>>> #  JAVA aside:  li = new List()
>>> #  C++  aside:  list li  OR  list* pli = new list()
>>> #  JAVA correction List li = new List()
>>> 
>>> #  (b)  li = list()   # list is a class in Python,  li is an instance
>>> 
>>> # empty tuple?
>>> # tu = () OR tu = tuple()
>>> 
>>> # empty dictionary?
>>> # di = {}  OR di = dict()
>>> 
>>> # empty set
>>> # se = set()
>>> 
>>> 
>>> # make a list of sqrt(x) for x = 10 to 30 (not 30)
>>> import math
>>> li = [math.sqrt(el) for el in range(10, 30)]
>>> 
>>> def dirpub(atype):
	return [el for el in dir(atype) if not el.startswith('_') and not el.endswith('_')]

>>> dir(math)
['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> dirpub(math)
['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dirpub(list)
['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> dirpub(tuple)
['count', 'index']
>>> 
>>> dir(dict)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> dirpub(dict)
['clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> 
>>> 
>>> li = [1, 2, 3]
>>> li = ['a', 'b', 'c']
>>> li = 'a b c'.split()
>>> li
['a', 'b', 'c']
>>> li = 'chicago losAngeles sanFrancisco atlanta'.split()
>>> li
['chicago', 'losAngeles', 'sanFrancisco', 'atlanta']
>>> li = 'chicago, los angeles, san francisco, atlanta'.split(',')
>>> li
['chicago', ' los angeles', ' san francisco', ' atlanta']
>>> li = 'chicago, los angeles, san francisco, atlanta'.split(',')

>>> li = [el.strip() for el in 'chicago, los angeles, san francisco, atlanta'.split(',')]
>>> li
['chicago', 'los angeles', 'san francisco', 'atlanta']
>>> 
>>> 
>>> # don't do this -- non-Pythonic
>>> li = []
>>> for el in 'chicago, los angeles, san francisco, atlanta'.split(','):
	li.append(el.strip())

>>> 
>>> di = { 'ORD' : 'chicago o\'hare', 'LAX' : 'los angeles', 'SFO' : 'san francisco', 'ATL' : 'atlanta' }
>>> di
{'SFO': 'san francisco', 'ORD': "chicago o'hare", 'LAX': 'los angeles', 'ATL': 'atlanta'}
>>> di.keys()
['SFO', 'ORD', 'LAX', 'ATL']
>>> di.values()
['san francisco', "chicago o'hare", 'los angeles', 'atlanta']
>>> di.items()
[('SFO', 'san francisco'), ('ORD', "chicago o'hare"), ('LAX', 'los angeles'), ('ATL', 'atlanta')]
>>> for k,v in di.items():
	print(k, v)

	
('SFO', 'san francisco')
('ORD', "chicago o'hare")
('LAX', 'los angeles')
('ATL', 'atlanta')
>>> 
>>> for k in sorted(di.keys()):
	print(k, di[k])

	
('ATL', 'atlanta')
('LAX', 'los angeles')
('ORD', "chicago o'hare")
('SFO', 'san francisco')
>>> 
>>> 
>>> print(3/2)
1
>>> print(3/2.0)
1.5
>>> print(3/0)

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print(3/0)
ZeroDivisionError: integer division or modulo by zero
>>> 
>>> def divide_by(a, b):
	return(a / b)

>>> print(divide_by(3, 2))
1
>>> print(divide_by(3, 2.0))
1.5
>>> print(divide_by(3, 0))

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print(divide_by(3, 0))
  File "<pyshell#90>", line 2, in divide_by
    return(a / b)
ZeroDivisionError: integer division or modulo by zero
>>> 
>>> def divide_by(a, b):
	if (b == 0): raise ZeroDivisionError('integer division by zero')
	return(a / b)

>>> print(divide_by(3, 0))

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print(divide_by(3, 0))
  File "<pyshell#96>", line 2, in divide_by
    if (b == 0): raise ZeroDivisionError('integer division by zero')
ZeroDivisionError: integer division by zero
>>> 
>>> def divide_by(a, b):
	if (b == 0): raise ZeroDivisionError('integer division by zero'
	return(a / b)
KeyboardInterrupt
>>> 
>>> 
>>> type(3)
<type 'int'>
>>> type('hello')
<type 'str'>
>>> type(3.5)
<type 'float'>
>>> 
>>> 
>>> 
>>> s = '1:I,4:IV,5:V,9:IX,10:X'
>>> li1 = s.split(',')
>>> li1
['1:I', '4:IV', '5:V', '9:IX', '10:X']
>>> li2 = [el.split(':') for el in li1]
>>> li2
[['1', 'I'], ['4', 'IV'], ['5', 'V'], ['9', 'IX'], ['10', 'X']]
>>> di = dict( (int(k),v) for k,v in li2)
>>> di
{1: 'I', 10: 'X', 4: 'IV', 5: 'V', 9: 'IX'}
>>> di2 = dict( (v, int(k)) for k,v in li2)
>>> di2
{'I': 1, 'IX': 9, 'V': 5, 'X': 10, 'IV': 4}
>>> 
>>> 
>>> 
>>> # what IS PEP 0008 ?!
>>> # it's a Python Enhancement Proposal (somebody has an idea to enhance Python)
>>> 
>>> 
>>> 
>>> 2 ** 99
633825300114114700748351602688L
>>> 2 ** 9
512
>>> type(2 ** 99)
<type 'long'>
>>> type(2 ** 9)
<type 'int'>
>>> 
KeyboardInterrupt
>>> # PEP 0008  --- your Pycharm code should have no warnings
>>> # doctest   --- your code should document input/output for its functions, and use doctest to test them
>>> 
>>> 
>>> # OOP !
>>> s = 'hello'
>>> x = 10
>>> f = 3.5
>>> li = '1 2 3'.split()
>>> type(s)
<type 'str'>
>>> type(x)
<type 'int'>
>>> type(f)
<type 'float'>
>>> type(li)
<type 'list'>
>>> # ALL of these are classes in Python
>>> # ALL of these have data!
>>> #
>>> # also, ALL of these have methods (functions that do things)
>>> dirpub(s)
['capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> dirpub(x)
['bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> 
>>> dirpub(f)
['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> 
>>> dirpub(li)
['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> tu = tuple(li)
>>> dirpub(tu)
['count', 'index']
>>> 
>>> 
>>> # when we want to write our own classes, then...
>>> #   they have to have data
>>> #   and they have to have methods
>>> #   and, if we want them to work nicely with Python, we have to define some std. methods
>>> 
>>> # start with a circle
>>> # circle data ?
>>> # circumference, radius, diameter, area, center, maybe outline color, maybe fill color, maybe fill pattern
>>> # radius and center are absolutely necessary
>>> # but let's start with just the center
>>> 
>>> class circle:
	def __init__(self, radius):
		self.radius = radius    # not completely right -- should have "private" data
>>> c = circle(5)
>>> type(c)
<type 'instance'>
>>> isinstance(c, int)
False
>>> isinstance(c, float)
False
>>> isinstance(c, circle)
True
>>> print(c)
<__main__.circle instance at 0x105298290>
>>> print(c.radius)
5
>>> 
>>> class circle:
	def __init__(self, radius):
		self._radius = radius
	def __str__(self):
		return 'circle[radius=' + str(self._radius) + ']'

	
>>> c = circle(4)
>>> print(c)
circle[radius=4]
>>> c2 = circle(66)
>>> print(c2)
circle[radius=66]
>>> # what is the address of circle c ?
>>> id(c)
4381573776
>>> # what is the base 16 (hex) address of circle c ?
>>> hex(id(c))
'0x105298290'
>>> # what's the address of circle c2 ?
>>> hex(id(c2))
'0x10528c440'
>>> hex(id(c)) == hex(id(c2))
False
>>> def hexid(x):
	return hex(id(x))

>>> hexid(c)
'0x105298290'
>>> hexid(c2)
'0x10528c440'
>>> class circle:          # rapid prototyping
	def __init__(self, radius):
		self._radius = radius
	def __str__(self):
		return 'circle[radius=' + str(self._radius) + ']'
	def radius(self): pass
	def diameter(self): pass
	def circumference(self): pass
	def area(self): pass

	
>>> import math

>>> class circle:               
	def __init__(self, radius):
		self._radius = radius
	def __str__(self):
		return 'circle[r={0},d={1},circ={2},area={3}]'.format(self.radius(), self.diameter(),
						                     self.circumference(),
								     self.area())
	def radius(self):        return self._radius
	def diameter(self):      return self._radius * 2
	def circumference(self): return self._radius * 2 * math.pi
	def area(self):          return self._radius ** 2 * math.pi

	
>>> c = circle(4)
>>> print(c)
circle[r=4,d=8,circ=25.1327412287,area=50.2654824574]
>>> class circle:
	def __init__(self, radius):
		self._radius = radius
	def __str__(self):
		return 'circle[r={0},d={1},circ={2:.2f},area={3:.2f}'.format(self.radius(), self.diameter(),
						                     self.circumference(),
								     self.area())
	def radius(self):        return self._radius
	def diameter(self):      return self._radius * 2
	def circumference(self): return self._radius * 2 * math.pi
	def area(self):          return self._radius ** 2 * math.pi

	
>>> c = circle(4)
>>> print(c)
circle[r=4,d=8,circ=25.13,area=50.27
>>> c2 = circle(5.2345)
>>> print(c2)
circle[r=5.2345,d=10.469,circ=32.89,area=86.08
>>> 

# === let's add some additional methods to class circle, to allow circles to be superscribed about a square, 
#    or inscribed within a square
 
>>> class circle:
	def __init__(self, radius, center=(0,0)):
		self._radius = radius
		self._center = center
	def __str__(self):
		return \
		       'circle[r={0},d={1},circ={2:.2f},area={3:.2f},ctr=({4},{5})]'.\
		       format(self.radius(), self.diameter(), self.circumference(),
			      self.area(), self.center()[0], self.center()[1])
	def radius(self):           return self._radius
	def diameter(self):         return self._radius * 2
	def circumference(self):    return self._radius * 2 * math.pi
	def area(self):             return self._radius ** 2 * math.pi
	def center(self):           return self._center
	def inscribe(self, square): return circle(square.side()/2.0, square.center())  # immutable class
	def superscribe(self,\
			square):    return circle(square.side()*math.sqrt(2.0)/2.0, square.center())

	
>>> sq = square(4)
>>> print(sq)
square[side=4,peri=16,area=16,center=(0,0)]
>>> r = rectangle(2, 1)
>>> print(r)
rectangle[l=2,w=1,peri=6,area=2,center=(0, 0)]

>>> class rectangle(object):
	def __init__(self, length, width, center=(0,0)):
		self._length = length
		self._width  = width
		self._center = center
	def __str__(self):
		return 'rectangle[l={0},w={1},peri={2},area={3},center=({4},{5})]'.\
		       format(self.length(), self.width(), self.perimeter(), self.area(),
			      self.center()[0], self.center()[1])
	def length(self):       return self._length
	def width(self):        return self._width
	def perimeter(self):    return 2 * (self._length + self._width)
	def area(self):         return self._length * self._width
	def center(self):       return self._center

	
>>> class square(rectangle):
	def __init__(self, side, center=(0,0)):
		super(square, self).__init__(side, side, center)
	def __str__(self):
		return 'square[side={0},peri={1},area={2},center=({3},{4})]'.format(self.side(), self.perimeter(), self.area(), self.center()[0], self.center()[1])
	def side(self): return self.length()

	
>>> sq = square(4)
>>> r = rectangle(2, 1)
>>> c = circle(5)
>>> print(str(sq), str(r), str(c))
('square[side=4,peri=16,area=16,center=(0,0)]', 'rectangle[l=2,w=1,peri=6,area=2,center=(0,0)]', 'circle[r=5,d=10,circ=31.42,area=78.54,ctr=(0,0)]')
>>> 




# let's refactor these classes to all inherit from a common, abstract, base class
# that class (shape) will define the methods that its subclasses must define, or they will be abstract too
# NOTE: abstract classes cannot be instantiated
#    but if the subclasses define the required methods, they are called concrete classes which can be instantiated

# =========================== class shape ==================================================

>>> import abc                      # stands for abstract base class

>>> class shape(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self, center=(0,0)):
		self._center = center

	def __str__(self):
		return 'shape[center=({0},{1})]'.format(self._center[0], self._center[1])
	def center(self):
		return self._center

	@abc.abstractmethod
	def with_center(self, center): pass
	
	@abc.abstractmethod
	def perimeter(self): pass

	@abc.abstractmethod
	def area(self): pass

# =========================== class shape ==================================================


>>> class circle(shape):
	def __init__(self, radius, center=(0,0)):
		super(circle, self).__init__(center)
		self._radius = radius
		self._center = center
	def __str__(self):
		return \
		       'circle[r={0},d={1},circ={2:.2f},area={3:.2f},ctr=({4},{5})]'.\
		       format(self.radius(), self.diameter(), self.circumference(),
			      self.area(), self.center()[0], self.center()[1])
	def radius(self):               return self._radius
	def diameter(self):             return self._radius * 2
	def circumference(self):        return self._radius * 2 * math.pi
	def area(self):                 return self._radius ** 2 * math.pi
	def with_center(self, center):  return circle(self._radius, center)
	def inscribe(self, square):     return circle(square.side()/2.0, square.center())  # immutable class
	def superscribe(self, square):  return circle(square.side()*math.sqrt(2.0)/2.0, square.center())

	
>>> class rectangle(shape):
	def __init__(self, length, width, center=(0,0)):
		super(rectangle, self).__init__(center)
		self._length = length
		self._width  = width
	def __str__(self):
		return 'rectangle[l={0},w={1},peri={2},area={3},center=({4},{5})]'.\
		       format(self.length(), self.width(), self.perimeter(), self.area(),
			      self.center()[0], self.center()[1])
	def length(self):              return self._length
	def width(self):               return self._width
	def with_center(self, center): return rectangle(self._length, self._width, center)
	def perimeter(self):           return 2 * (self._length + self._width)
	def area(self):                return self._length * self._width

	
>>> class square(rectangle):
	def __init__(self, side, center=(0,0)):
		super(square, self).__init__(side, side, center)
	def __str__(self):
		return 'square[side={0},peri={1},area={2},center=({3},{4})]'.format(self.side(), self.perimeter(), self.area(), self.center()[0], self.center()[1])
	def side(self):                return self.length()
	def with_center(self, center): return square(self._side, center)

	
>>> r = rectangle(3, 2)
>>> print(r)
rectangle[l=3,w=2,peri=10,area=6,center=(0,0)]
>>> r2 = r.with_center((3, 4))
>>> print(r2)
rectangle[l=3,w=2,peri=10,area=6,center=(3,4)]
>>> 
>>> 



>>> # what if we were to refactor this code to add a parallelogram class?
>>> # what would have to change
>>> # well, parallelograms have a length and width, but also have an angle
>>> # rectangles are parallelograms with an angle of 90 degrees (or pi/2.0 radians)


# final version of all classes is below...

# =============================  circle class ==========================================

>>> class circle(shape):
	def __init__(self, radius, center=(0,0)):
		super(circle, self).__init__(center)
		self._radius = radius
		self._center = center
	def __str__(self):
		return \
		       'circle[r={0},d={1},circ={2:.2f},area={3:.2f},ctr=({4},{5})]'.\
		       format(self.radius(), self.diameter(), self.circumference(),
			      self.area(), self.center()[0], self.center()[1])
	def radius(self):               return self._radius
	def diameter(self):             return self._radius * 2
	def perimeter(self):            return self.circumference()
	def circumference(self):        return self._radius * 2 * math.pi
	def area(self):                 return self._radius ** 2 * math.pi
	def with_center(self, center):  return circle(self._radius, center)
	def inscribe(self, square):     return circle(square.side()/2.0, square.center())  # immutable class
	def superscribe(self, square):  return circle(square.side()*math.sqrt(2.0)/2.0, square.center())

	
# =============================  circle class ==========================================

  
>>> c = circle(5)
>>> print(c)
circle[r=5,d=10,circ=31.42,area=78.54,ctr=(0,0)]
>>> c2 = c.with_center( (2, 4) )                     # don't say c.with_center(2, 4)
>>> print(c2)
circle[r=5,d=10,circ=31.42,area=78.54,ctr=(2,4)]
>>> 

	
# =============================  parallelogram class ==========================================

>>> class parallelogram(shape):
	def __init__(self, length, width, angle=math.pi/2.0, center=(0,0)):
		super(parallelogram, self).__init__(center)
		self._length = length
		self._width  = width
		self._angle  = angle
	def __str__(self):
		return 'parallelogram[l={0},w={1},angle={2:.2f} radians,peri={3},area={4},center=({5},{6})]'.\
		       format(self.length(), self.width(), self.angle(), self.perimeter(), self.area(),
			      self.center()[0], self.center()[1])
	def length(self):              return self._length
	def width(self):               return self._width
	def angle(self):               return self._angle
	def with_center(self, center): return parallelogram(self._length, self._width, self._angle, center)
	def perimeter(self):           return 2 * (self._length + self._width)
	def area(self):                return self._length * self._width

# =============================  parallelogram class ==========================================


	
>>> p = parallelogram(5, 1, math.pi/4.0)
>>> print(p)
parallelogram[l=5,w=1,angle=0.79 radians,peri=12,area=5,center=(0,0)]


# =============================  rectangle class ==========================================

>>> class rectangle(parallelogram):
	def __init__(self, length, width, center=(0,0)):
		super(rectangle, self).__init__(length, width, math.pi/2.0, center)
	def __str__(self):
		return 'rectangle[l={0},w={1},peri={2},area={3},center=({4},{5})]'.\
		       format(self.length(), self.width(), self.perimeter(), self.area(),
			      self.center()[0], self.center()[1])
	def with_center(self, center): return rectangle(self._length, self._width, math.pi/2.0, center)

# =============================  rectangle  class ==========================================


	
>>> r = rectangle(4, 1)
>>> print(r)
rectangle[l=4,w=1,peri=10,area=4,center=(0,0)]


# =============================  square class ==========================================

>>> class square(rectangle):
	def __init__(self, side, center=(0,0)):
		super(square, self).__init__(side, side, center)
	def __str__(self):
		return 'square[side={0},peri={1},area={2},center=({3},{4})]'.format(self.side(), self.perimeter(), self.area(), 
                                                                        self.center()[0], self.center()[1])
	def side(self):                return self.length()
	def with_center(self, center): return square(self.side(), center)    # make a new square with new center

# =============================  square class ==========================================

	
>>> sq = square(5)
>>> sq2 = sq.with_center( (1, 1))      # create a new square with a different center -- old square not affected
>>> print(sq2)
square[side=5,peri=20,area=25,center=(1,1)]
>>> 
