from math import sqrt

def kvadratrot(a,x0,N):
    """
    a: Det vi skal ta kvadratrota av
    x0: Startgjett
    N: antall iterasjoner
    """
    x = x0
    for i in range(N):
        x = 0.5*(x + a/x)
    return x

rot = kvadratrot(12,100,5)
    
print("Numerisk:", rot, "Analytisk:",sqrt(12))
