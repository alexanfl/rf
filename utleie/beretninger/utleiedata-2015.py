# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import matplotlib.pyplot as plt
import matplotlib.colors as c
import numpy as np
from matplotlib import cm


infile = codecs.open("utleiedata.dat", "r", "utf-8")

persons = {}

mean = 0

for line in infile:
    a = line.split("\t")
    if a[0] in persons:
        persons[a[0]] += float(a[1])
    else:
        persons[a[0]] = float(a[1])
    mean += float(a[1])

N = len(persons)
persons['Gjennomsnitt'] = mean/N

N+=1

plt.figure(1, figsize=(10,10))

hours = []
explode = []
names = []

for name in persons:
    hours.append(persons[name])
    names.append(name)
    explode.append(0.05)

sortedhours = np.argsort(hours)
newhours = np.sort(hours)
newnames = range(N)


i=0
for index in sortedhours:
    newnames[i] = names[index]
    i += 1

y_pos = range(N)

plt.barh(y_pos, newhours, align='center', color='lightcoral')
for a,b in zip(newhours,y_pos):
    plt.text(a+0.5, b-0.2, str(a))


plt.yticks(y_pos, newnames)
plt.title('Timer jobbet på utleie i 2015', bbox={'facecolor':'lightcoral', 'pad':10})
plt.tight_layout()
plt.savefig('utleiebar.png')
plt.show()
