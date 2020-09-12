# A python file to find the Fibonacci sequence up to a user defined no

import numpy as np

n = int(input("Enter the no. Up to which you want the Fibonacci sequence:"))
f = np.zeros(n+1)
a = 0
b = 1

for i in range(1, n+1):
    a, b = b, a+b 
    f[i] = a

phi_est = f/b

print("The Fibonacci sequence up to  the {} terms is:".format(n), f, phi_est)

