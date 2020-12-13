# Climate model assuming earth to have no atmosphere but emmisivity > 0

import matplotlib.pyplot as plt

insolation = 1300  # approx value in W/m^2
time = 0
earth_temp = 0  # now we want to understand in terms of temperature
heat_capacity = 1000
dt = 60  # time step of 60s

plt.figure(figsize=(10, 10))
plt.xlabel("time (s)")
plt.ylabel("Earth Temperature (K)")
plt.title("Naked Earth")
plt.ion()


def black_body(temp):
    sigma = 5.67E-8
    return sigma*(temp**4)


while True:
    earth_temp += (insolation - black_body(earth_temp))*dt / heat_capacity
    time += dt
    print(time, earth_temp)
    plt.scatter(time, earth_temp, color='black')
    plt.pause(0.01)
