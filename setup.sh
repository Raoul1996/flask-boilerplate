#!/bin/bash
# setup.sh
# Setup script for Flask Boilerplate only for Mac machines. Look at docs for windows

set -o errexit  # exit on any errors

sudo apt install -y python3-pip postgresql
sudo pip install virtualenv
virtualenv -p /usr/bin/python3.5 --no-site-packages --no-wheel venv
pip install -r requiremets.txt
python manage.py recreate_db
