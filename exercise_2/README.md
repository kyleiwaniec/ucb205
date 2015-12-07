#Exercise 2#


##Requirements:

####AMI   
__ucbw205_complete_plus_postgres_PY2.7__    
__IMPORTANT__: python 2.7 will be run in a virtualenv. Lein will also be installed in the appropriate location, namely /usr/local/bin/lein. This is important! Do not use the python 2.7 installation instructions in the exercise, as that method breaks the necessary components to install some dependencies.   

####Volume   
A brand new `m3.large`   
(if you are using a pre-exisitng volume and you already have postgres running, you will get the option to skip the postgres setup)

##Dependencies:   
(These will all be installed by following the Steps below)
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

Once you have mounted /data on your volume, and set your github keys:   
```
cd /data
git clone git@github.com:kyleiwaniec/ucb205.git
cd ucb205/
git checkout exercise_2
```

__1. Install dependencies__    
You will be prompted to confirm whether or not postgres is set up on /data/pgsql (if you attached a brand new volume, the answer is no)   You will also be prompted to enter your twitter credentials.


`. /data/ucb205/exercise_2/install-dependencies.sh`


__2. Start the stream__
```
cd /data/ucb205/exercise_2/EX2Tweetwordcount/
sparse quickstart EX2Tweetwordcount
sparse run
```

__3. Open a new shell, source the virtualenv, and run applications:__
```
source  ~/27env/bin/activate   

python /data/ucb205/exercise_2/histogram.py 50 100
python /data/ucb205/exercise_2/finalresults.py -w mother
python /data/ucb205/exercise_2/plot.py

```

You can use scp to view the generated plot.png bar graph:   
`scp -i your_key.pem root@xx.xxx.xx.xx:/data/ucb205/exercise_2/plot.png /path/to/local/dir`



