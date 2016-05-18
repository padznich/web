sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart﻿﻿

sudo apt-get install python-dev
sudo apt-get install libmysqlclient-dev

sudo mysql -u root -e "CREATE DATABASE test_db;"
sudo /etc/init.d/mysql restart

sudo virtualenv env
sudo . env/bin/activate
sudo pip install -r requirements.txt

sudo python ask/manage.py syncdb

sudo /etc/init.d/mysql restart

cd ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
