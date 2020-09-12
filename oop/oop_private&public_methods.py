# THis is an example of Private and Public methods

class Polygon:
	__width = None
	__height = None

	def set_values(self, width, height):
		self.__width = width
		self.__height = height

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height	

class Rectangle(Polygon):
	def area(self):
		return self.get_height() * self.get_height()

class Triangle(Polygon):
	def area(self):
		return self.get_height() * self.get_width() / 2

rectangle = Rectangle()
triangle = Triangle()

rectangle.set_values(30, 40)
triangle.set_values(70, 40)

print(rectangle.area())
print(triangle.area())