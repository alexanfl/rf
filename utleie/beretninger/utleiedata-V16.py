# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import matplotlib.pyplot as plt
import matplotlib.colors as c
import numpy as np
from matplotlib import cm


infile = codecs.open("utleiedata-V16.dat", "r", "utf-8")

persons = {}

mean = 0.
counter = 0.

for line in infile:
    a = line.split(",")
    if a[0] in persons:
        persons[a[0]] += float(a[1])
    else:
        persons[a[0]] = float(a[1])
    mean += float(a[1])

    for i in a[0]:
        if i == 'æ' or i == 'ø' or i == 'å':
            counter += 1

N = len(persons)
persons['Gjennomsnitt'] = mean/N

print counter/N

N+=1

plt.figure(1, figsize=(10,10))

hours = []
names = []

for name in persons:
    hours.append(persons[name])
    names.append(name)

sortedhours = np.argsort(hours)
newhours = np.sort(hours)
newnames = range(N)

i=0

for index in sortedhours:
    newnames[i] = names[index]
    i += 1

y_pos = range(N)

plt.barh(y_pos, newhours, align='center', color='lightgreen')
for a,b in zip(newhours,y_pos):
    plt.text(a+0.5, b-0.2, str(a))


plt.yticks(y_pos, newnames)
plt.title('Timer jobbet på utleiearrangementer våren 2016', bbox={'facecolor':'lightgreen', 'pad':10})
plt.tight_layout()
plt.savefig('utleiebar-V16.png')
plt.show()
