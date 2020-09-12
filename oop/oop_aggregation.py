# OOP Aggregation

class Salary:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus

	def annual_salary(self):
		return (self.pay * 12) + self.bonus


# Instantiating the salary class in the Employee class so 
# salary class is the content and Employee class is container

class Employee:
	def __init__(self, name, age, salary): 
		self.name = name
		self.age = age
		self.obj_salary = salary 

	def total_salary(self):
		return self.obj_salary.annual_salary()

salary = Salary(90000, 10000)

emp = Employee('Aditya', 21, salary)

print(emp.total_salary())