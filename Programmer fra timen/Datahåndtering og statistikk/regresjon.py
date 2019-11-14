from pylab import *
from sklearn.metrics import r2_score

# Data
T = array([0,20,40,60,80,100])
sol_NH3 = array([88.5, 56.0, 34.0, 20.0, 11.0, 7.0])
sol_NaCl = array([35.7, 35.9, 36.4, 37.1, 38.0, 39.2])

# Regresjon
n = 2 # Grad
reg = polyfit(T, sol_NH3, n)

x = linspace(0,150,10000)
y = reg[0]*x**2 + reg[1]*x + reg[2]

# Sjekker om regresjonen er god
y_R2 = reg[0]*T**2 + reg[1]*T + reg[2]
R2 = r2_score(sol_NH3, y_R2)
print(R2)

scatter(T,sol_NH3,label='Datapunkter, NH$_3$')
plot(x, y, color = 'coral',label='Tilpasset kurve, NH$_3$')
legend()
title('Løselighet av salter')
xlabel('Temperatur i $^o$C')
ylabel('Løselighet i g/100 mL')
grid()
show()