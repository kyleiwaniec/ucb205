# 
import psycopg2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("min", help="Min number of occurances")
parser.add_argument("max", help="Max number of occurances")
args = parser.parse_args()

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


cur.execute("SELECT word, count FROM Tweetwordcount WHERE count >=%s and count <=%s;" %(args.min, args.max))
response = cur.fetchall()

for i in response:
        print i[0]," : ",i[1]

conn.commit()

conn.close()
