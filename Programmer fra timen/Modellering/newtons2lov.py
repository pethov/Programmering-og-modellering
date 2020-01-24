from pylab import *

# Konstanter
k = 1   # Luftmotstand
g = 9.81  # Tyngdeakselerasjon i m/s^2
m = 0.001 # Masse i kg
v0 = 0   # Starthastighet i m/s
s0 = 0   # Startposisjon i m

# Tidsvariabler
dt = 0.5 # Tidsintervall i s
tid_start = 0
tid_slutt = 2
N = int((tid_slutt-tid_start)/dt) # Antall intervaller

# Arrayer
t = zeros(N+1)
a = zeros(N+1)
v = zeros(N+1)
s = zeros(N+1)

# Startverdier
t[0] = tid_start
v[0] = v0
s[0] = s0

for i in range(N):
    a[i] = g - k*v[i]**2/m
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = v[i+1]*dt + 0.5*a[i]*dt**2
    t[i+1] = t[i] + dt

plot(t,s,label='strekning')
legend()
show()



