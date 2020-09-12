# Object oriented programming example

class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def change_name(self, name):
		self.name = name

	def set_age(self, age):
		self.age = age

	def bark(self):
		print("bark")

d = Dog("Adi", 21)

print(d.get_name())
print(d.get_age())
d.set_age(25)
d.change_name("Sar")
print(d.get_name())
print(d.get_age())
d.bark()