# Luke Reed
# 01/18/2016
# class_06.py


import abc							# allows us to create abstrat classes
import math
'''
class A(object):	pass			# must start by inherits from object

class B(A): 		pass			# now we can inherit from a superclass

# Now we will revisit the superclass / subclass

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
'''



# ============================== ANIMAL CLASS =================================

# all animals can speak
# make cat, dog, duck classes that are subclasses of Animal
'''

class Animal(object):
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def speak(): pass

class Cat(Animal):
	def speak(self): print('meow meow')

class Dog(Animal):
	def speak(self): print('woof woof')

class Duck(Animal):
	def speak(self): print('quack quack')

c = Cat()
d = Dog()
dk = Duck()

c.speak()		# meow meow
d.speak()		# woof woof
dk.speak()		# quack quack
'''

# In JAVA we can instantiate our classes
# class X extends Number implements Speakable

# Similarly in python:
class Speakable(object):		# this is an interface
	def speak(self): pass
class Animal(object):			# this is an abstract class
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def eat(self): pass
	@abc.abstractmethod
	def reproduce(self): pass

class Cat(Animal, Speakable):
	def eat(self): print('cat is eating')
	def reproduce(self): print('cat is reproducing')
	def speak(self): print('meow meow')

c = Cat()			
c.speak()			# meow mewo
c.eat()				# cat is eating
c.reproduce()		# cat is reproducing

# Python 2 and Python 3 handle search for methods in parents differently

# what about flying animals ?
# there are two ways to do this
# ( if you are not a human )

class FlyingAnimal(Animal, Speakable):
#	def eat(self): super(FlyingAnimal, self).eat()
	def eat(self): print('Flying animal is eating')
#	def reproduce(self): super(FlyingAnimal, self).reproduce()
	def reproduce(self): print('Flying animal is reproducing')
	def fly(self): print('I am flying')
	def speak(self): print('cheep cheep')

fa = FlyingAnimal()
fa.fly()
fa.eat()

class Turkey(FlyingAnimal, Speakable):
	def fly(self): print('Turkeys can\'t really fly')
	def speak(self): print('gobble gobble')

t = Turkey()
t.fly()				# I am flying
t.speak()			# gobble gobble
t.reproduce()		# Flying animal is reproducing

class Eagle(FlyingAnimal, Speakable):
	def speak(self): print('eek eek')

e = Eagle()
e.fly()				# I am flying
e.speak()			# eek eek
e.reproduce()		# Flying animal is reproducing

# Eagle --> Flying Animal --> Animal
#   <-----> Speakble
# (def speak)

# Interface like classes (abstract classes with very few methods -- usually one)
# Abstract classes have at least one abstract method, but frequently have more
# Concrete classes that define all of the abstract methods they inherit
# Concrete classes can override their parents' methods
#		Turkey and Eagle override parent class with the speak() method

# class Animal(metaclass-abc.ABCMeta):		# Python 3 version
#	 @abc.abstractmethod
#	 def eat(self): pass
#	 @abc.abstractmethod
#	 def reproduce(self): pass

# Turkey IS-A FlyingAnimal IS-A Animal and IS-A Speakable
# Eagle  IS-A FlyingAnimal IS-A Animal and IS-A Speakable
# Cat                      IS-A Animal and IS-A Speakable

# OOP: IS-A (inheritance or implementation) vs. HAS-A (composition)
print '\n'

class Animal(object):
	def __init__(self, name):
		self._name = name
	def __str__(self):
		return 'Animal[{0}]'.format(self._name)
	def name(self): return self._name

	@abc.abstractmethod
	def eat(self): pass
	@abc.abstractmethod
	def reproduce(self): pass

class Cat(Animal, Speakable):
	def __init__(self, name='no name'):
		super(Cat, self).__init__(name)
	def __str__(self):
		return 'Cat[{0}]'.format(self.name())
	def eat(self): print('cat is eating')
	def reproduce(self): print('cat is reproducing')
	def speak (self): print('meow meow')

c = Cat('Fran')
print(c)			# Cat[Fran]
c = Cat()
print(c)			# Cat[no name]

# now, Cat IS-A Animal, and Cat IS-A Speakable, and Cat HAS_A name (str)
print type(c.name())		# <type 'str'>



# ========================  FRACTIONS! ================================
# brainstorm a Fraction class
# data? --> numerator and denominator (num, denom)
# methods? --> divide, multiply, add, subtract, num(), denom(), __init__(), __str__()

class Fraction(object):
	def __init__(self, num=0, denom=1):
		self._num, self._denom = num, denom
	def __str__(self):
		return 'Fraction[{0}/{1}]'.format(self._num,self._denom)
		if (self._denom == 0):
			raise ValueError('cannot have a denominator of 0')
	def add(self, other):
		# assume they have the same denominator
		return Fraction(self._num + other._num, self._denom)
	def sub(self, other):
		# assume they have the same denominator
		return Fraction(self._num - other._num, self._denom)
	# ADD IN LCM AND GCD


f1 = Fraction()
f2 = Fraction(1,4)
print(f1)			# Fraction[0/1]
print(f2)			# Fraction[1/4]

f3 = f1.add(f2)
f4 = f1.sub(f2)
print(f3)			# Fraction[1/1]
print(f4)			# Fraction[-1/1]


# 4/4   --  really need gcm(num,denom), divide by num and divide by gcd
# what about 2/3 + 3/4
# we need the lcm of 3 and 4 which is 12
# ---> 8/12 + 10/12 = 20/12
# and then, we need the gcd of (20 and 12), divide by 4 --> 5/3


# NEED TO ADD IN VALUE ERROR TEST FOR A 0 DENOMINATOR!!!




# ================  BEVERAGE DECORATOR  ===============================
# NOTE: Python has decorator objects that are different from the Decorator
# design pattern (e.g., @abc.abstractmethod)

print('\n')

class Beverage(object):
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def name(): pass

class Espresso(Beverage):
	def name(self): return 'Espresso'
	def cost(self): return 0.50

es = Espresso()
print es.name()		# Espresso

# Now we're ready for the BeverageDecorator
class BeverageDecorator(Beverage):
	def __init__(self, beverage):
		self._beverage = beverage
	def beverage():		return self._beverage

class Mocha(BeverageDecorator):
	def __init__(self, beverage):
		super(Mocha, self).__init__(beverage)
	def __str__(self):	return '{0}-${1:.2f}'.format(self.name(),str(self.cost()))
	def name(self):		return 'mocha--' + self.beverage().name()
	def cost(self):		return 0.25 + self.beverage().cost()

mes = Mocha(es)
print(mes)
print(es.cost())

# NEED TO FIX ABOVE CLASS STRUCTURE!!!!




