ECHO is on.
### Project Setup ###

### Pkg Installation ###

Install Python and pip

sudo apt-get install -y tcl-dev -y

sudo apt install postgresql -y

sudo apt install libpq-dev python3-dev -y

sudo apt install apache2 -y

sudo apt install libapache2-mod-wsgi-py3 -y


### Installing Redis on Linux ###

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04

wget http://download.redis.io/redis-stable.tar.gz

tar xvzf redis-stable.tar.gz

cd redis-stable

sudo make

sudo make test

sudo make install

#Upgrade pip

sudo apt install python3-pip

python -m pip install --upgrade pip

#Virtual Env

sudo pip3 install virtualenv

virtualenv venv

source venv/bin/activate

Clone the repo

git clone https://github.com/divyanshrajeshjain/practice-mgmt.git

### Run the following command: ###

  python product/mysite/setup.py


### Setup the postgresql database ###

sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib -y

sudo -u postgres psql

CREATE DATABASE acws;

CREATE USER acws_user WITH PASSWORD 'password';

ALTER ROLE acws_user SET client_encoding TO 'utf8';

ALTER ROLE acws_user SET default_transaction_isolation TO 'read committed';

ALTER ROLE acws_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE acws TO acws_user;

ALTER USER acws_user CREATEDB;

\q

### DELETE DATABASE and REINIT ###

DROP DATABASE acws;

CREATE DATABASE acws;

GRANT ALL PRIVILEGES ON DATABASE acws TO acws_user;

\q

  
### Go to directory practice-mgmt/product/mysite and run: ###

python manage.py makemigrations

python manage.py migrate

To run server run:

python manage.py runserver

Test commit

Test commit
