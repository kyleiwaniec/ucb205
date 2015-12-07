

function AMI {
STR=$'If you are using the ucbw205_complete_plus_postgres_virtual2.7 AMI (RECOMMENDED), enter 1. \nIf you are using the ucbw205_complete_plus_postgres_PY2.7 AMI, enter 2. '
echo "$STR"
read answer

if [[ "$answer" == "1" ]]; then
	wget --directory-prefix=/usr/local/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
	chmod a+x /usr/local/bin/lein
	sudo /usr/local/bin/lein

	pip install matplotlib
	pip install streamparse
	pip install psycopg2
	pip install argparse
	pip install numpy
	pip install tweepy

elif [[ "$answer" == "2" ]]; then

	#########################################
	#   WHAT *NOT* TO DO:
	#########################################
	#
	# sudo yum install python27-devel –y
	# mv /usr/bin/python /usr/bin/python266
	# ln -s /usr/bin/python2.7 /usr/bin/python
	# sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
	# sudo python ez_setup.py
	# sudo /usr/bin/easy_install-2.7 pip
	# sudo pip install virtualenv

	# wget --directory-prefix=/usr/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
	# chmod a+x /usr/bin/lein
	# sudo /usr/bin/lein

	# mkdir /usr/local/lib/tmp_h/
	# mv /usr/local/lib/libpython2.7.a /usr/local/lib/tmp_h/
	# pip install --no-cache-dir matplotlib
	# mv /usr/local/lib/tmp_h/libpython2.7.a /usr/local/lib/
	#
	#########################################

	wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
	python2.7 ez_setup.py
	easy_install-2.7 pip
	pip2.7 install virtualenv
	virtualenv -p python2.7 27env
	source 27env/bin/activate

	wget --directory-prefix=/usr/local/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
	chmod a+x /usr/local/bin/lein
	sudo /usr/local/bin/lein
	
	pip install matplotlib
	pip install streamparse
	pip install psycopg2
	pip install argparse
	pip install numpy
	pip install tweepy	
else
	echo "Please choose an AMI. You must enter either 1, or 2"
	AMI
fi
}
AMI

STR=$'Do you have postgres directories already set up in /data/pgsql? [yes]: '
echo "$STR"
read answer

if [[ "$answer" != "yes" ]]; then
#set up directories for postgres
mkdir /data/pgsql
mkdir /data/pgsql/data
mkdir /data/pgsql/logs
chown -R postgres /data/pgsql
sudo -u postgres initdb -D /data/pgsql/data

#setup pg_hba.conf
sudo -u postgres echo "host    all         all         0.0.0.0         0.0.0.0               md5" >> /data/pgsql/data/pg_hba.conf

#setup postgresql.conf
sudo -u postgres echo "listen_addresses = '*'" >> /data/pgsql/data/postgresql.conf
sudo -u postgres echo "standard_conforming_strings = off" >> /data/pgsql/data/postgresql.conf

#make start postgres file
cat > /data/start_postgres.sh <<EOF
#! /bin/bash
sudo -u postgres pg_ctl -D /data/pgsql/data -l /data/pgsql/logs/pgsql.log start
EOF
chmod +x /data/start_postgres.sh

#make a stop postgres file
cat > /data/stop_postgres.sh <<EOF
#! /bin/bash
sudo -u postgres pg_ctl -D /data/pgsql/data -l /data/pgsql/logs/pgsql.log stop
EOF
chmod +x /data/stop_postgres.sh

fi

#start postgres
/data/start_postgres.sh

# set the twitter keys:
. /data/ucb205/exercise_2/set-twitter-keys.sh




