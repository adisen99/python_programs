# Class Attributes

class Person:

	number_of_people = 0 # This is a Class Attribute which is same for all people and hence it is
						 # common to all instances of the class

	def __init__(self, name):
		self.name = name
		Person.number_of_people += 1

p1 = Person("Aditya")
print(p1.number_of_people)

p2 = Person("Sophie")
print(p2.number_of_people)

# Class Methods

class Person:

	number_of_people = 0 # This is a Class Attribute which is same for all people and hence it is
						 # common to all instances of the class

	def __init__(self, name):
		self.name = name
		Person.add_person()

	@classmethod		
	def number_of_people_(cls):
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1

p1 = Person("Aditya")
p2 = Person("Sophie")

print(Person.number_of_people_())