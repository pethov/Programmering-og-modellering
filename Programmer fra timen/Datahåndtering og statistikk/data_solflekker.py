from pylab import *

T = [0,20,40,60,80,100]
sol_NH3 = [88.5, 56.0, 34.0, 20.0, 11.0, 7.0]
sol_NaCl = [35.7, 35.9, 36.4, 37.1, 38.0, 39.2]

# Regresjon
grad = 2
reg_NaCl = polyfit(T,sol_NaCl,grad)

x = linspace(0,150,100000)
a = reg_NaCl[0]
b = reg_NaCl[1]
c = reg_NaCl[2]
y = a*x**2 + b*x + c

scatter(T,sol_NaCl)
plot(x,y,color='red')





