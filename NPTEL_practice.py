import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10000,10000)
y1 = np.linspace(-100,100,10)
y2 = np.linspace(-100,100,10)

y1 = x**(1/3)
y2 = np.log10(x)

idx=np.argwhere(np.diff(np.sign(y1 - y2 )) != 0).reshape(-1) + 0

plt.plot(x,y1,y2)

plt.show()
