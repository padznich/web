sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart﻿﻿

sudo apt-get install python-dev
sudo apt-get install libmysqlclient-dev

sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "CREATE DATABASE test_db;"
sudo /etc/init.d/mysql restart

sudo /etc/init.d/mysql restart

