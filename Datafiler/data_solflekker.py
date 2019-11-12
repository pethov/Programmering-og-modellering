from pylab import *

data = loadtxt('Datafiler/sunspots.csv', skiprows = 1, delimiter = ',')

year = data[:,0]
spots = data[:,1]

plot(year,spots,color='firebrick')
ylabel('Antall solflekker')
xlabel('År')
grid()
show()