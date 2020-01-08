from pylab import *

def finn_primtall(n):
    tall = list(linspace(2,n,n-1))
    i = 0
    p = tall[i]
    while p**2 <= n:
        for element in tall:
            if element%p == 0 and element >= p**2:
                tall.remove(element)
        i = i + 1
        p = tall[i]
    return tall

primtall = finn_primtall(100)
print(primtall)