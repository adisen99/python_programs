import turtle

my_turtle=turtle.Turtle()
my_turtle.speed(500)
my_turtle.shape('arrow')

def square(length,angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)
  
for i in range(50):
    
    my_turtle.color('orange')
    square(100,90)
    my_turtle.right(11)
    
for i in range(50):
    my_turtle.color('red')
    square(100,90)
    my_turtle.right(11)

for i in range(50):
    my_turtle.color('blue')
    square(100,90)
    my_turtle.right(11)

for i in range(50):
    my_turtle.color('green')
    square(100,90)
    my_turtle.right(11)

my_turtle.penup()
my_turtle.goto(0,-200)
my_turtle.pendown()
my_turtle.color('black')
my_turtle.write("That Was COOL!")
my_turtle.penup()
my_turtle.goto(0,-400)

    


