#!/bin/bash
# setup.sh
# Setup script for Flask Boilerplate only for Mac machines. Look at docs for windows

set -o errexit  # exit on any errors

sudo apt install -y python-pip python3.7 postgresql
sudo pip install pipenv virtualenv
sudo service postgresql restart
pipenv install --python 3.5
pipenv shell
pipenv run pip install -r requiremets.txt

# wait until postgres is started
while ! pg_isready -h "localhost" -p "5432" > /dev/null 2> /dev/null; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 3
done

>&2 echo "Postgres is up - executing command"

createdb || true    # create init database - pass on error
psql -c "create user testusr with password 'password';" || true     # pass on error
psql -c "ALTER USER testusr WITH SUPERUSER;" || true
# psql -c "create database testdb owner testusr encoding 'utf-8';"
# psql -c "GRANT ALL PRIVILEGES ON DATABASE testdb TO testusr;"

python manage.py recreate_db
