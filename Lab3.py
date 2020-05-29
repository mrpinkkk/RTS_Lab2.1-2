import math
import matplotlib.pyplot as plt

from random import *
import time
from numpy import fft
import numpy as np

n = 10 
Wmax = 1200 
N = 64 

x = [0 for i in range(N)] 

start = time.time()
for i in range(n):
    A = uniform(0, 1)
    F = uniform(0, 1)
    for j in range(0, N):
        x[j] += A * math.sin(Wmax / n * j * i + F)

end = time.time()
print("t генерації сигналів",end - start)
Fr = []
Fi = []
def dpf(signals, N):

    for i in range(N):
        Fr.append(0)
        Fi.append(0)
        for j in range(N):
            Fr[i] += x[j]*math.cos(-2*math.pi*i*j/N)
            Fi[i] += x[j]*math.sin(-2*math.pi*i*j/N)

start = time.time()
dpf(x, N)
end = time.time()
print("t ДПФ", end - start)
F = np.array([Fr[i] + 1j*Fi[i] for i in range(N)])
Fl = fft.fft(x)


fig = plt.figure()


g1 = fig.add_subplot(2, 2, 1)
g2 = fig.add_subplot(2, 2, 2)
g3 = fig.add_subplot(2, 2, 3)
g4 = fig.add_subplot(2, 2, 4)

g1.plot(range(N), Fr)
g2.plot(range(N), Fi)
g3.plot(range(N), Fl.real)
g4.plot(range(N), Fl.imag)

g1.set(title="Fr")
g2.set(title="Fi")
g3.set(title="Fl_real")
g4.set(title="Fl_imaginative")


plt.show()

