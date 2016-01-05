#! bin/bash

wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
python2.7 ez_setup.py
easy_install-2.7 pip
pip2.7 install virtualenv
virtualenv -p python2.7 api
source api/bin/activate