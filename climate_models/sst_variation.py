# Climate data plotting and modelling

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.csv', delimiter=',', dtype=None,
                     skip_header=5, names=('date', 'value', 'anomaly'))

plt.title("Global Land and Ocean temperature data")
plt.xlabel("year")
plt.ylabel("degrees +/- from average")
plt.bar(data['date'], data['value'], color="blue")
plt.show()
