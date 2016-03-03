#!/usr/bin/python
# Luke Reed
# 02/12/2016
# shape.py

'''
create a set of classes so that they all inherit from a common, abstract, base class
that class (shape) will define the methods that its subcalsses must define, or they will be abstract too
NOTE: abstract calsses cannot be instantiated"""
    but if the subcalsses define the required methods, they are called concrete classes which can be instantiated
'''

# =========================== class shape ==================================================

# first import required libraries
import math
import abc 			# stands for abstract base class

class shape(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self, center=(0,0)):
		self._center = center

	def __str__(self):
		return 'shape[center=({0},{1})]'.format(self._center[0], self._center[1])
	def center(self):
		return self._center

	# must create abstract classes
	# if a subclass doesn't include these methods, then it is another abstract class
	# WE ARE NOT ALLOWED TO CREATE OUR OWN ABSTRACT CLASS
	@abc.abstractmethod
	def with_center(self, center): pass
	
	@abc.abstractmethod
	def perimeter(self): pass

	@abc.abstractmethod
	def area(self): pass


# =========================== class shape ==================================================
class circle(shape):
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


class rectangle(shape):
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

class square(rectangle):
	def __init__(self, side, center=(0,0)):
		super(square, self).__init__(side, side, center)
	def __str__(self):
		return 'square[side={0},peri={1},area={2},center=({3},{4})]'.\
			   format(self.side(),self.perimeter(),self.area(),self.center()[0],self.center()[1])
	def side(self):					return self.length()
	def with_center(self, center): 	return square(self._side, center)


# now let's test it out!
r = rectangle(3,2)
print(r)

r2 = r.with_center((3,4))
print(r2)

c = circle(2)
