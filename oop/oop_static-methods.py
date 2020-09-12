# Static Methods

# used to create object which have classes that can be used at any point independent of instances

class Math:

	@staticmethod
	def sum(x,  y):
		return x + y

	@staticmethod
	def product(x, y):
		return x*y

	@staticmethod
	def subtract(x, y):
		return x + (-y)

print(Math.sum(2, 6))

print(Math.product(2,6))

print(Math.subtract(2, 6))