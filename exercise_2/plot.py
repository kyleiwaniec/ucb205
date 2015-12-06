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

common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", 
"on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", 
"her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", 
"out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", 
"just", "him", "know", "take", "person", "into", "year", "your", "good", "some", "could", "them", 
"see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", 
"after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", 
"any", "these", "give", "day", "most", "us"]

tupleX = tuple(x for x in response if x[0] not in common_words)

tupleX = tupleX[1:21]

wordsList_x = [x[0] for x in tupleX]
wordsList_y = [y[1] for y in tupleX]


conn.commit()

conn.close()

N = 20
wordCounts = (wordsList_y)

ind = np.arange(N)  # the x locations for the groups
width = 0.5       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, wordCounts, width, color='deeppink', edgecolor = "none")

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

