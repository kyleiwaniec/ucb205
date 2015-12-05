#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r')

ax.set_title('Top 20 words')
ax.set_xticks(ind + width)


ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))


plt.savefig('plot.png')
plt.show()

