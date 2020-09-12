from turtle import*

def sierpinski (l,n) :
     if n==0 :
         begin_fill()
         forward(1)
         left(120)
         forward(1)
         left(120)
         forward(1)
         left(120)
         end_fill()

     else:
        sierpinski(1/2,n-1)
        forward(1/2)
        sierpinski(1/2,n-1)
        left(120)
        forward(1/2)
        right(120)
        sierpinski(1/2,n-1)
        right(120)
        forward(1/2)
        left(120)

speed(0)
rang= input ("choose a range:")
rang= int(rang)
sierpinski(200, rang)
ht()
        
