import numpy as np
import matplotlib.pyplot as plt

Zkm = np.array([0.0, 0.1, 0.3, 0.5, 1.0, 2.0, 3.0,
                4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
RH100 = np.array([60.0, 70.0, 80.0, 75.0, 60.0, 50.0, 80.0,
                  90.0, 60.0, 40.0, 20.0, 5.0, 2.0, 1.0])


RH = RH100*0.01
Z = Zkm*1000.0

A = 2.53e11
B = 5420
g = 9.806
Cp = 1005
R = 287
L = 2.5006e6
v0 = 100
Ps = 1e5
Ts = 30
Zs = R*(Ts + 273.15) / g

Tk = np.zeros(len(Zkm))
T = np.array(Tk)
P = np.array(T)
es = np.array(T)
e = np.array(T)
q = np.array(T)
r = np.array(T)
w = np.array(T)
h = np.array(T)
MSE = np.array(T)
v = np.array(T)
TE = np.array(T)

for i in range(0, len(Zkm)):
    Tk[i] = (Ts+273.15) - (g*Z[i]/Cp)
    T[i] = Tk[i] - 273.15
    P[i] = np.exp(-g*Z[i]/(R*Tk[i]))
    es[i] = A*np.exp(-B/Tk[i])
    e[i] = RH[i] * es[i]
    r[i] = P[i]/(R*Tk[i])
    q[i] = 0.622*(e[i]/P[i])
    w[i] = q[i] * r[i]
    h[i] = L*q[i] + Cp*Tk[i]
    MSE[i] = h[i] + g*Z[i]
    v[i] = v0*(np.exp(Z[i]/Zs)-1)
    TE[i] = MSE[i] + 0.5*(v[i]**2)

plt.plot(RH, Z, label="RH")
plt.plot(Tk, Z, label="Tk")
plt.plot(P, Z, label="P")
plt.plot(es, Z, label="es")
plt.plot(e, Z, label="e")
plt.plot(q, Z, label="q")
plt.plot(r, Z, label="r")
plt.plot(w, Z, label="w")
plt.plot(h, Z, label="h")
plt.plot(MSE, Z, label="MSE")
plt.plot(TE, Z, label="TE")
plt.plot(v, Z, label="v")
plt.ylabel("Altitude")
plt.title("Vert. Profiles")
plt.axis()
plt.legend()
plt.grid(True)
plt.show()
