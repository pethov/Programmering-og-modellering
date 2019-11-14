from pylab import *

fag = ['R2', 'S2', 'Kjemi 2',
       'Fysikk 2', 'Tekforsk',
       'Matematikk X', 'Biologi 2']

antall = [110, 25, 74, 65, 10,
          20, 45]

pie(antall,labels=fag)
show()