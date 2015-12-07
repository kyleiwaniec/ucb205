#Exercise 2#


##Requirements:

####AMI   
The __ucbw205_complete_plus_postgres_virtual2.7__ AMI is recommended. It has the python 2.7 virtual environment already set up and running:      
`ucbw205_complete_plus_postgres_virtual2.7`   
`ami-003f7f6a`

   
But if you insist... you can use the AMI specified in the exercise. If you use this AMI, python 2.7 will be configured exactly as per the instructions in the exercise.     
`ucbw205_complete_plus_postgres_PY2.7`

####Volume   
`m3.large`

##Dependencies:   
(These will be installed by following the Steps below)
```
Postgres
Python 2.7
lein
```
####Python modules
```
matplotlib
streamparse
psycopg2
argparse
numpy
tweepy
```

###Steps to install dependencies and run application

Once you have mounted /data on your volume:   
```
cd /data
git clone git@github.com:kyleiwaniec/ucb205.git
cd ucb205/
git checkout exercise_2
```

Install dependencies. You will be prompted to choose which AMI you are using, and to confirm whether or not postgres is set up on /data:   
`. /data/ucb205/exercise_2/install-dependencies.sh`

Create the Database and tables:   
`. /data/ucb205/exercise_2/make-db.sh`

Start the application
```
cd /data/ucb205/exercise_2/EX2Tweetwordcount/
sparse quickstart EX2Tweetwordcount
sparse run
```

Open a new shell, source the virtualenv, and run applications:
```
source 27env/bin/activate
python /data/ucb205/exercise_2/histogram.py 50 100
python /data/ucb205/exercise_2/finalresults.py -w mother
python /data/ucb205/exercise_2/plot.py

```

Use scp to view the generated plot.png bar graph:   
`scp -i your_key.pem root@xx.xxx.xx.xx:/data/ucb205/exercise_2/plot.png /path/to/local/dir`



