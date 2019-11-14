from pylab import *

data = loadtxt('testdata.txt',skiprows=1,delimiter=',')

nr = data[:,0]
hoyde = data[:,1]

plot(nr, hoyde)

snitt = mean(hoyde)
avvik = std(hoyde)

print("Snitt:", snitt, "Standardavvik:", avvik)