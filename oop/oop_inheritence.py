# Introduction to Inheritance

# Upper Level Class and all other classes borrow from it
# generalisation

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def speak(self):
		print("I don't know what to say")

class Cat(Pet):

	def __init__(self, name, age, color):
		super().__init__(name, age)
		self.color = color

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old and I am {self.color} in color")

	def speak(self):
		print("Meow")

class Dog(Pet):

	def speak(self):
		print("Bark")

class Fish(Pet):
	pass

p = Pet("Aditya", 21)
p.show()
p.speak()

c = Cat("Ishita", 22, "Violet")
c.show()
c.speak()

d = Dog("Sanan", 23)
d.show()
d.speak()

f = Fish("Saransh", 25)
f.show()
f.speak()