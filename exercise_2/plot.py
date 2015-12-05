#!/usr/bin/env python
import psycopg2
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-w", help="enter a word you want to find")
args = parser.parse_args()

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY count DESC;")
response = cur.fetchall()

tupleX = tuple(x for x in response if x[0] != 'the')
tupleX = tupleX[1:21]


wordsList_x = [x[0] for x in tupleX]
wordsList_y = [y[1] for y in tupleX]
# for i in tupleX:
# 	wordsList_x.append(i[0])
# 	wordsList_y.append(i[1])

print tupleX
print wordsList_x

conn.commit()

conn.close()

N = 20
menMeans = (wordsList_y)

ind = np.arange(N)  # the x locations for the groups
width = 0.5       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='deeppink', edgecolor = "none")

ax.set_title('Top 20 words')
ax.set_xticks(ind + width)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.set_xticklabels((wordsList_x), rotation=45 )
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    left='off',
    right='off')

plt.savefig('plot.png')
plt.show()

