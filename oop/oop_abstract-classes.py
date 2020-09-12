# abstract classes	

from abc import ABC, abstractmethod 

class Shape(ABC):
	
	@abstractmethod
	def area(self) : pass

	@abstractmethod
	def perimeter(self) : pass

class Square(Shape) :
	def __init__(self, side):
		self.__side = side

	def area(self):
		return self.__side**2

	def perimeter(self):
		return self.__side * 4

square = Square(5)
print(f"The area is {square.area()}")
print(f"The perimeter is {square.perimeter()}")