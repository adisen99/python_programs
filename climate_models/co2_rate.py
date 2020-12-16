#  A climate model dealing with the 3D radiation values but simple model

import numpy as np
import matplotlib.pyplot as plt

plt.figure()
plt.xlabel("time (year)")
plt.ylabel("percentage co2 in atmosphere")
plt.title("Co2 Earth")
plt.ion()

pco2 = 100
start_year = 1900
end_year = 2000
A = 0.0225
dt = 1
rfco2 = 0

time = start_year

while time <= end_year:
    pco2 = 280 + (pco2 - 280)*(1 + A*dt)
    rfco2 = 4*(np.log(pco2/280)/np.log(2))
    time += dt
    print(time, pco2)
    plt.scatter(time, pco2, color="blue")
    plt.pause(0.01)

# for i in range(start_year:dt:end_year):
#     pco2_next = 280 + (pco2 - 280)*(1 + A*dt)
