import matplotlib.pyplot as plt  # lib for graphs
import random
import numpy as np
import math

n = 10
N = 256
W0 = 150
Wmax = 1500
W = np.arange(W0, Wmax + W0, W0)


def generator(n, N, W):
    signals = np.zeros(N)
    for i in range(n):
        A = random.random()
        phi = random.random()
        for t in range(N):
            signals[t] += A * math.sin(W[i] * t + phi)

    return signals


def corelvalue(signal1, signal2):
    size = len(signal1)
    assert size == len(signal2)

    Mx1 = np.average(signal1)
    Mx2 = np.average(signal2)

    result = []
    for i in range(size):
        result.append((signal1[i] - Mx1) * (signal2[i] + Mx2))

    return sum(result)/(size - 1)


def autocorel(signal):
    size = round(len(signal)/2)

    result = []
    for i in range(size):
        result.append(corelvalue(signal[0:size], signal[i:size+i]))

    return result
   
def crosscorel(signal1,signal2):
    size = round(len(signal1)/2)

    result = []
    for i in range(size):
        result.append(corelvalue(signal1[0:size], signal2[i:size+i]))

    return result




signal_first = generator(n,N,W)
signal_second = generator(n,N,W)
print(crosscorel(signal_first,signal_second))
print('Mx:', np.average(signal_first)) 
print('Dx:', np.var(signal_second))  

plt.plot(signal_first)
plt.plot(signal_second)
plt.xlabel('time')
plt.ylabel('x')
plt.title('Random generated signals 1, 2')
plt.figure()


#cross-correlation
plt.plot(crosscorel(signal_first, signal_second)) 
plt.xlabel('time')
plt.ylabel('correlation')
plt.title('cross-correlation')
plt.figure()

# autocorrelation
plt.plot(autocorel(signal_first))  
plt.xlabel('time')
plt.ylabel('correlation')
plt.title('autocorrelation')
plt.show()

