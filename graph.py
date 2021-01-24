import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv
 
from functools import reduce
from operator import add

pricks_file = open('pricks.csv', 'r')

prick_count = {}
reader = csv.reader(pricks_file)
next(reader)

for mp in reader:
    if mp[1] not in prick_count:
        prick_count[mp[1]] = {'Members': 0, 'Pricks': 0}

    prick_count[mp[1]]['Members'] += 1

    if mp[2] == 'True':
        prick_count[mp[1]]['Pricks'] += 1

font = {'family' : 'normal',
        'size'   : 20}

matplotlib.rc('font', **font)

fig, axes = plt.subplots(3, 4)

axes = [j for sub in axes for j in sub]

for i in range(3 * 4 - len(prick_count)):
    fig.delaxes(axes[-1 - i])

print(fig, axes)

for ax in axes:
    print(ax)

for count, party in enumerate(prick_count):
    colors = ['#d33a34', '#27c657']
    #axes[count] = fig.add_axes([0,0,1,1])
    axes[count].axis('equal')
    data = [
        prick_count[party]['Pricks'],
        prick_count[party]['Members'] - prick_count[party]['Pricks']
    ]
    pie, texts = axes[count].pie(data, labels=None, colors=colors, radius=2)
    axes[count].title.set_text(party)
    
leg = fig.legend(pie, ('Is a prick', 'Is not a prick'))
bb = leg.get_bbox_to_anchor().inverse_transformed(axes[0].transAxes)
xOffset = -1
bb.x0 += xOffset
bb.x1 += xOffset
leg.set_bbox_to_anchor(bb, transform = axes[0].transAxes)

fig.suptitle("% of MPs who are pricks by party", fontsize=40)
plt.show()
