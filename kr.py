import numpy as np

data = [5,1,3,8,4]
def dispersion (arr):
    n = len(arr)
    Mx = np.average(arr)
    res = []
    for el in arr:
       res.append(pow((el - Mx),2))    
    
    return sum(res)/(n - 1)

Dx = dispersion(data)
print("%s" %Dx)

    
