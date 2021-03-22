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


def generator(n, N, W):
    signals = np.zeros(N)
    for w in W :
        A = random.random()
        phi = random.random()
        for t in range(N):
            signals[t] += A * math.sin(w * t + phi)

    return signals


def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    res = np.dot(M,x)
    return res 

print(DFT_slow(generator(n,N,W)))

def FFT(signal):
    size = len(signal)
    if size % 2 > 0:
        raise ValueError("Value must be power of 2")
        
    elif size <= 32:
       return DFT_slow(signal)

    else:
        X_even = FFT(signal[::2])
        X_odd = FFT(signal[1::2])    
        factor = np.exp(-2j * np.pi * np.arange(size) / size)
        res =  np.concatenate([X_even + factor[:int(size / 2)] * X_odd,
                               X_even + factor[int(size / 2):] * X_odd]) 
        
    return res

fft = FFT(generator(n,N,W))
res = [abs(f) for f in fft]


# l = [1,2,3,4,5,6,7,8,9,10,11]
# print(l[1::2])
# res = [abs(f) for f in fft]
# print(res)
plt.plot(res)
plt.xlabel('t')
plt.ylabel('F(t)')
plt.show()

# print(type(FFT(generator(n,N,W))))

# print(FFT(generator(n,N,W)))