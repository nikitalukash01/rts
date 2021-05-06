import matplotlib.pyplot as plt  # lib for graphs
import random
import numpy as np
import math
import time

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
        result.append((signal1[i] - Mx1) * (signal2[i] - Mx2))

    return sum(result)/(size - 1)


def autocorel(signal):
    size = round(len(signal)/2)

    result = []
    for i in range(size):
        result.append(corelvalue(signal[0:size], signal[i:size+i]))
        print(signal[i:size+i])

    return result
   
def crosscorel(signal1,signal2):
    size = round(len(signal1)/2)

    result = []
    for i in range(size):
        result.append(corelvalue(signal1[0:size], signal2[i:size+i]))

    return result

# signal_third = generator(n,N,W)
# time_start = time.time()
# autocorel(signal_third)
# duration_1 = time.time() - time_start
# # print("%s seconds" %duration_1)
# 
data = [5,1,3,8,4]
data_1 = np.asarray(data)
print(autocorel(data))