# Python Operator overloading 

import math

class Circle:
	def __init__(self, radius):
		self.__radius = radius

	def get_radius(self):
		return self.__radius

	def set_radius(self, radius):
		self.__radius = radius

	def area(self):
		return self.__radius**2 * math.pi

	def __add__(self, circle_object):
		return Circle(self.__radius + circle_object.__radius)

	def __lt__(self, circle_object):
		return (self.__radius < circle_object.__radius)		


	def __gt__(self, circle_object):
		return (self.__radius > circle_object.__radius)

	def __str__(self):
		return "circle area is " + str(self.area()) 

c1 = Circle(5)
c2 = Circle(3)
c3 = c1 + c2

print(c1.get_radius())
print(c2.get_radius())
print(c3.get_radius())

print(c1 < c2)
print(c1 > c2)

print(str(c1))
