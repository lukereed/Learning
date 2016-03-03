#!/usr/bin/python
# Luke Reed
# 02/12/2016
# shape_v2.py
# refactor shape.py code to add a parallelogram class



#what would have to change?
#parralellograms have length and width, but also have angles
#rectangles are just parallelograms with angle of 90 or pi/2


# final version of all classes

# =============================  circle class ==========================================
import math
import abc

class shape(object):
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

# now we can define the individual classes


# =============================  circle class ==========================================

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

# =============================  circle class ==========================================

c = circle(5)					# circle[r=5,d=10,circ=31.42,area=78.54,ctr=(0,0)]
print(c)						# circle[r=5,d=10,circ=31.42,area=78.54,ctr=(2,4)]
c2 = c.with_center( (2,4) )
print(c2)


# =============================  parallelogram class ==========================================

class parallelogram(shape):
	def __init__(self, length, width, angle=math.pi/2.0, center=(0,0)):
		super(parallelogram, self).__init__(center)
		self._length = length
		self._width  = width
		self._angle  = angle
	def __str__(self):
		return 'parallelogram[l={0},w={1},angle={2:.2f} radians, peri={3},area={4}, center=({5},{6})]'.\
		       format(self.length(), self.width(), self.angle(), self.perimeter(),self.area(),
		       	  self.center()[0], self.center()[1])
	def length(self):				return self._length
	def width(self):				return self._width
	def angle(self):				return self._angle
	def with_center(self, center):	return parallelogram(self._length, self._width, self._angle, center)
	def perimeter(self):			return 2 * (self._length + self._width)
	def area(self):					return self._length * self._width

# =============================  parallelogram class ==========================================


p = parallelogram(5,1, math.pi/4.0)
print(p)		# parallelogram[l=5,w=1,angle=0.79 radians, peri=12,area=5, center=(0,0)]


# =============================  rectangle class ==========================================

class rectangle(parallelogram):
	def __init__(self, length, width, center=(0,0)):	# specify default value in the initialization
		super(rectangle, self).__init__(length, width, math.pi/2.0, center)
	def __str__(self):
		return 'rectangle[l={0},w={1},peri={2},area={3},center=({4},{5})]'.\
			   format(self.length(), self.width(), self. perimeter(), self.area(),
			   	  self.center()[0], self.center()[1])
	def with_center(self, center): return rectangle(self._length, self._width, math.pi/2.0, center)

# =============================  rectangle class ==========================================

r = rectangle(4,1)
print(r)			# rectangle[l=4,w=1,peri=10,area=4,center=(0,0)]

# =============================  square class ==========================================

class square(rectangle):
	def __init__(self, side, center=(0,0)):
		super(square, self).__init__(side, side, center)
	def __str__(self):
		return 'square[side={0},peri={1},area={2},center=({3},{4})]'.\
			   format(self.side(), self.perimeter(), self.area(), self.center()[0], self.center()[1])
	def side(self):					return self.length()
	def with_center(self, center):	return square(self.side(),center)

# =============================  square class ==========================================

sq = square(5)
sq2 = sq.with_center((1, 1))	# create a new square with a different center -- old square not affected
print(sq)						# square[side=5,peri=20,area=25,center=(0,0)]


