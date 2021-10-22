import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def f(x): return -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2


def t(x): return 0.2*x
def g(x): return 0.2-2.1*(x-1)
def h(x): return 0.2-2.1*(x-1) -3.1*((x-1)**2)/(factorial(2))
def w(x): return 0.2-2.1*(x-1) -3.1*((x-1)**2)/(factorial(2)) -3.3*((x-1)**3)/(factorial(3))
def z(x): return 0.2-2.1*(x-1) -3.1*((x-1)**2)/(factorial(2)) -3.3*((x-1)**3)/(factorial(3)) -2.4*((x-1)**4)/(factorial(4))
x = np.linspace(1,3,100)

aa = f(x)
bb = g(x)
cc = h(x)
tt = t(x)
vv = w(x)
zz = z(x)

plt.plot(x, aa ,color="red",label="función real")
plt.plot(x, tt ,color="purple",label="orden 0")
plt.plot(x, bb ,color="blue",label="primer orden")
plt.plot(x, cc ,color="yellow",label="segundo orden")
plt.plot(x, vv ,color="green",label="tercer ordern")
plt.plot(x, zz ,color="black",label="cuarto orden")

plt.title("Grafica de la función")
plt.legend()
plt.ylabel("y")
plt.xlabel("x")
plt.show()


