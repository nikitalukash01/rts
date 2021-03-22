import matplotlib.pyplot as plt  # lib for graphs
import random
import numpy as np
import math
n = 10
N = 256
W0 = 150
Wmax = 1500
signals = np.zeros(N)
W = np.arange(W0, Wmax + W0, W0)
for w in W :
    A = random.random()
    phi = random.random()
    for t in range(N):
        signals[t] += A * math.sin(w * t + phi)

print('Mx:', np.average(signals))  # Average
print('Dx:', np.var(signals))  # Dispersion
print(signals)
# plt.plot(signals)
# plt.xlabel("t")
# plt.ylabel("X(t)")
# plt.show()
