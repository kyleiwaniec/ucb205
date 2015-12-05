# fetch the word provided as argument, else, fetch everything, and display counts
import psycopg2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w", help="enter a word you want to find")
args = parser.parse_args()

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if args.w:
	cur.execute("SELECT word, count FROM Tweetwordcount WHERE word='%s';" %(args.w))
	response = cur.fetchall()
	if response:
		print "Total number of occurences of '", response[0][0] ,"':", response[0][1]
	else:
		print "There are no occurances of '",args.w,"' in the database."
else:
	cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY word ASC;")
	response = cur.fetchall()
	for i in response:
		print i[0]," : ",i[1]

conn.commit()

conn.close()

