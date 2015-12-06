#Exercise 2#


Requirements:

AMI:
`ucbw205_complete_plus_postgres_PY2.7`

Volume
`m3.large`

```
Postgres
Python 2.7
```



sudo yum install python27-devel –y
mv /usr/bin/python /usr/bin/python266
ln -s /usr/bin/python2.7 /usr/bin/python
sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
sudo python ez_setup.py
sudo /usr/bin/easy_install-2.7 pip
sudo pip install virtualenv


wget --directory-prefix=/usr/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein

ls -l /usr/bin/lein
chmod a+x /usr/bin/lein
ls -l /usr/bin/lein


# running lein, will install it
sudo /usr/bin/lein
lein version


mkdir /usr/local/lib/tmp_h/
mv /usr/local/lib/libpython2.7.a /usr/local/lib/tmp_h/
pip install --no-cache-dir matplotlib
mv /usr/local/lib/tmp_h/libpython2.7.a /usr/local/lib/


pip install streamparse
pip install psycopg2
pip install argparse
pip install numpy
pip install tweepy

sparse quickstart EX2Tweetwordcount

——————————————————————————————————

Creating your EX2Tweetwordcount streamparse project...
    create    EX2Tweetwordcount
    create    EX2Tweetwordcount/.gitignore
    create    EX2Tweetwordcount/config.json
    create    EX2Tweetwordcount/fabfile.py
    create    EX2Tweetwordcount/project.clj
    create    EX2Tweetwordcount/README.md
    create    EX2Tweetwordcount/src
    create    EX2Tweetwordcount/src/bolts
    create    EX2Tweetwordcount/src/bolts/__init__.py
    create    EX2Tweetwordcount/src/bolts/wordcount.py
    create    EX2Tweetwordcount/src/spouts
    create    EX2Tweetwordcount/src/spouts/__init__.py
    create    EX2Tweetwordcount/src/spouts/words.py
    create    EX2Tweetwordcount/tasks.py
    create    EX2Tweetwordcount/topologies
    create    EX2Tweetwordcount/topologies/wordcount.clj
    create    EX2Tweetwordcount/virtualenvs
    create    EX2Tweetwordcount/virtualenvs/wordcount.txt
Done.

Try running your topology locally with:

	cd EX2Tweetwordcount
	sparse run

——————————————————————————————————

rm EX2Tweetwordcount/src/spouts/words.py
cp tweetwordcount/src/spouts/tweets.py EX2Tweetwordcount/src/spouts/


rm EX2Tweetwordcount/src/bolts/wordcount.py
cp tweetwordcount/src/bolts/parse.py EX2Tweetwordcount/src/bolts
cp tweetwordcount/src/bolts/wordcount.py EX2Tweetwordcount/src/bolts

rm EX2Tweetwordcount/topologies/wordcount.clj
cp tweetwordcount/topologies/tweetwordcount.clj EX2Tweetwordcount/topologies/




# add keys to Twittercredentials.py

python hello-stream-twitter.py

# make the postgres database
sudo -u postgres psql -f twitter.sql


# check that the DB was created:
psql -U postgres

# connect to database tcount
\c tcount

# describe the Tweetwordcount table
\d+ Tweetwordcount

# quit
\q


python histogram.py 50 100
python finalresults.py -w mother
python plot.py



