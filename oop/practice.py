# Practicing OOP

class MyTrasports:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def change_brand(self, brand):
        self.brand = brand

    def change_color(self, color):
        self.color = color


class Car(MyTrasports):
    def __repr__(self):
        return f'This car is {self.color} and was produced by {self.brand}'

    def repairs(self):
        """
        prints what part of the car is repaired that user can define
        """
        repair = ''
        print(f'{self.repair} is fixed now.')


class Train(MyTrasports):
    def __repr__(self):
        return f'This train is {self.color} and was made by {self.brand}'

    def journey(self):
        """
        Prints the source and destination of the train that user can define
        """
        departure = ''
        arrival = ''
        print(f'This train goes from {self.departure} to {self.arrival}')

    def changeDestination(self, arrival):
        """
        Changes the destination or arrival of the train and tells the user.
        """
        self.arrival = arrival
        print(f"The destination has been changed to {self.arrival}")


my_car = Car('Tiago', 'brown')
my_car.change_brand('TATA')
my_train = Train('Rajdhani', 'red')
print(my_car)
print(my_train)

my_car.repair = 'door'
my_car.repairs()

my_train.departure = 'Delhi'
my_train.arrival = 'Kolkata'
my_train.journey()

my_train.changeDestination('Rourkela')
my_train.journey()

help(my_car.repairs)
help(my_train.journey)
