import matplotlib.pyplot as plt  # lib for graphs
import random
import numpy as np
import math
import cmath
import time
n = 10
N = 256
W0 = 150
Wmax = 1500
W = np.arange(W0, Wmax + W0, W0)

data = np.asarray([5,1,3,8])

def generator(n, N, W):
    signals = np.zeros(N)
    for i in range(n):
        A = random.random()
        phi = random.random()
        for t in range(N):
            signals[t] += A * math.sin(W[i] * t + phi)

    return signals

## excecuting with numpy array
def remakeFur(signal):
    size = len(signal)

    F = np.zeros(size)
    for p in range(size):
        for t in range(size):
            F[p] += complex(math.cos(2*math.pi/N * (p*t)), -
                            math.sin(2*math.pi/N * (p*t))) * signal[t]

    return F


def toAbsolute(complexFur):
    l = []
    for el in complexFur:
        l.append(abs(el))

    return l


# signal = generator(n, N, W)
# time_start = time.time()
# remakeFur(signal)
# duration = time.time() - time_start
# print("%s seconds" % duration)


# excecuting using list
def listFur(signal):
    size = len(signal)
    F = []
    for p in range(size):
        for t in range(size):
            F.append(complex(math.cos(2*math.pi/N * (p*t)), -
                         math.sin(2*math.pi/N * (p*t))) * signal[t])

    return F

# print(remakeFur(generator(n,N,W)))

# signal_1 = generator(n, N, W)
# time_start_1 = time.time()
# listFur(signal_1)
# duration_1 = time.time() - time_start_1
# print("%s seconds" % duration_1)

## printing difference in time
# print("%s difference in seconds" % (duration - duration_1))

# print(spectr)

# plotting signal
# plt.plot(signal)
# plt.xlabel('t')
# plt.ylabel('X(t)')
# plt.figure()

# ##plotting spectr
# plt.plot(spectr)
# plt.xlabel('signal')
# plt.ylabel('spectr')
# plt.show()

print(toAbsolute(remakeFur(data)))