from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        self.cur = self.conn.cursor()

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.


        # Increment the local count
        self.counts[word] += 1


        self.cur.execute("UPDATE Tweetwordcount SET count=count+1 WHERE word=%(word)s", {'word': word})
        self.conn.commit()

        self.cur.execute("INSERT INTO Tweetwordcount (count, word) \
           SELECT 1,%s \
           WHERE NOT EXISTS (SELECT 1 FROM Tweetwordcount WHERE word=%s)", (word, word))
        self.conn.commit()



        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
