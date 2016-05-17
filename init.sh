sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart﻿﻿

sudo apt-get install python-dev
sudo apt-get install libmysqlclient-dev

sudo virtualenv env
sudo . env/bin/activate
pip install -r requrements.txt
sudo pip install MySQL-python

mysql -uroot -e "CREATE DATABASE test_db;"
mysql -uroot -e "CREATE USER 'root'@'%' IDENTIFIED BY 'root';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON test_db. * TO 'root'@'%';"
mysql -uroot -e "FLUSH PRIVILEGES;"

