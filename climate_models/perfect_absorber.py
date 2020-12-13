# Climate model assuming earth to be a perfect absorber

import matplotlib.pyplot as plt

insolation = 1300  # approx value in W/m^2
time = 0
earth_energy = 0
dt = 60  # time step of 60s

plt.figure(figsize=(10, 10))
plt.xlabel("time (s)")
plt.ylabel("Earth Energy")
plt.title("Perfect Absorber")
plt.ion()

while True:
    earth_energy += insolation*dt
    time += dt
    print(time, earth_energy)
    plt.scatter(time, earth_energy, color='black')
    plt.pause(0.01)
