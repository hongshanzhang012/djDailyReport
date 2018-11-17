"""
WSGI config for djDailyReport project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djDailyReport.settings")

application = get_wsgi_application()

"""
web applications should run as system users with limited privileges
in my case, I use sgroup 'webapps2' and user 'djDailyReport'
$ sudo groupadd --system webapps2
$ sudo useradd --system --gid webapps2 --shell /bin/bash --home /var/www/djDailyReport djDailyReport
#owner djDailyReport and group owner 'nick' has full access to folder djDailyReport
sudo chown -R djDailyReport:nick /var/www/djDailyReport/
sudo chmod -R 775 /var/www/djDailyReport
"""

"""
#install virtualenv on specified python version, mine is python 2.7.11
cd /var/www/djDailyReport
virtualenv -p /usr/local/lib/python2.7.11/bin/python env

sudo su - djDailyReport
source env/bin/activate #use deactivate to exit virtualenv
#may need sudo apt-get install python-pip first 
#no need to install django/gunicorn if git clone 
pip install django
pip install psycopg2 #django interface to postgre db 
pip install gunicorn

#using the following command to start gunicorn
#navigate to src folder
gunicorn djWeb365.wsgi #use virtual env
#to stop service: ctrl+c

#call gunicorn in background
gunicorn djWeb365.wsgi &
to stop service: use process manager
gunicorn -b 127.0.0.1:8000 -b [::1]:8000 djDailyReport.wsgi &
#list gunicorn process and kill it
ps -a
sudo kill "any-id-with gunicorn"


#to start gunicorn when linux reboots
sudo nano /etc/init/gunicorn.conf
#type
description "Gunicorn application server handling myproject"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid djDailyReport
setgid webapps2
chdir /var/www/djDailyReport
start on startup
task
exec env/bin/gunicorn --workers 3 -b 127.0.0.1:8000 -b [::1]:8000 djDailyReport.wsgi

"""

"""
virtualenv on eclipse
create new interpreter: Window->Preferences... > PyDev > Interpreters > Python Interpreter
set your project to use this new interpreter
If you later install additional libraries, you will need to go back to the interpreter definitions,
 click "Apply", and tell Pydev which interpreters it should scan again. Until you do that, 
 PyDev might not notice your new libraries

"""

"""
git
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
#install git
sudo apt-get install git

git init #create git folder under project folder
git status -s (long or short) 

#stage change: git add, so git knows about the changes but they are not commited, you can still reset the changes

git add . #add project tree index. call it everytime the project tree changed,
git commit -m "commit message" # m stands for commit message
git commit -a # omit git add .
git reset HEAD -- hello.py #unstage the file
git reset --soft HEAD~ #undo last commit and them back on stage
git reset --hard HEAD #discard all changes since last commit
gihttp://marketplace.eclipse.org/marketplace-client-intro?mpc_install=979t rm file #remove file from index
git stash file #save changes in somewhere, not commit the changes for now.

git checkout -b iss53 #Switched to a new branch "iss53"
git checkout master
git merge hotfix
git branch -d hotfix #Deleted branch hotfix (3a0874c).

# on windows git config --global user.name "hongshanzhang012", 
# git config --global user.email "hongshanzhang012@gmail.com"

#remote link named as "origin", usr/pass: gmail, g2
git remote add origin https://github.com/hongshanzhang012/djDailyReport.git
#this brganch will be our master branch 
#master is only a parameter stored in .git/config
git push -u origin master

#clone a copy on deploy server
#Don't create the folder djWeb365, no need
git clone https://github.com/hongshanzhang012/djDailyReport.git djDailyReport

#/etc/nginx/sites-enabled/default
server {
    server_name 10.1.1.82;
    listen       8080; #80 is occupied by ipsw already
    server_name  url365.com www.url365.com;
    root         /var/www/djDailyReport/;

    access_log off;

    location /static/ {
        alias /var/www/djDailyReport/env/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
    }
}

"""





