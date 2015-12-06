
STR=$'If you are using the ucbw205_complete_plus_postgres_virtual2.7 AMI (recommended), press 1. If yo are using the ucbw205_complete_plus_postgres_PY2.7
 AMI, press 2: '
echo "$STR"
read answer

if [[ "$answer" != "1" ]]; then
	wget --directory-prefix=/usr/local/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
	chmod a+x /usr/local/bin/lein
	sudo /usr/local/bin/lein

#	pip install matplotlib
	pip install streamparse
	pip install psycopg2
	pip install argparse
	pip install numpy
	pip install tweepy
else
	sudo yum install python27-devel –y
	mv /usr/bin/python /usr/bin/python266
	ln -s /usr/bin/python2.7 /usr/bin/python
	sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
	sudo python ez_setup.py
	sudo /usr/bin/easy_install-2.7 pip
	sudo pip install virtualenv

	wget --directory-prefix=/usr/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
	chmod a+x /usr/bin/lein
	sudo /usr/bin/lein

	mkdir /usr/local/lib/tmp_h/
	mv /usr/local/lib/libpython2.7.a /usr/local/lib/tmp_h/
	pip install --no-cache-dir matplotlib
	mv /usr/local/lib/tmp_h/libpython2.7.a /usr/local/lib/


	pip install streamparse
	pip install psycopg2
	pip install argparse
	pip install numpy
	pip install tweepy	
fi


