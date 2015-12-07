#Exercise 2#


##Requirements:

####AMI   
__ucbw205_complete_plus_postgres_PY2.7__ 
__IMPORTANT__: If you use this AMI, see the architecture.pdf for gotchas!

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

__Install dependencies__    
You will be prompted to confirm whether or not postgres is set up on /data/pgsql (if you attached a brand new volume, the answer is no)    You will also be prompted to enter your twitter credentials.


`. /data/ucb205/exercise_2/install-dependencies.sh`

__Create the Database and tables__    
`. /data/ucb205/exercise_2/make-db.sh`

__Start the application__
```
cd /data/ucb205/exercise_2/EX2Tweetwordcount/
sparse quickstart EX2Tweetwordcount
sparse run
```

Open a new shell, source the virtualenv, and run applications:
```
source  ~/27env/bin/activate   

python /data/ucb205/exercise_2/histogram.py 50 100
python /data/ucb205/exercise_2/finalresults.py -w mother
python /data/ucb205/exercise_2/plot.py

```

Use scp to view the generated plot.png bar graph:   
`scp -i your_key.pem root@xx.xxx.xx.xx:/data/ucb205/exercise_2/plot.png /path/to/local/dir`



