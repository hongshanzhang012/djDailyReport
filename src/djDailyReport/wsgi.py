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

#to start gunicorn when linux reboots
#/etc/init nano djWeb365.conf
#type:
start on startup
task
exec gunicorn /var/www/djWeb365/src/djWeb365.wsgi &



reload app:
ps -xa | grep gunicorn
kill -HUP 23435


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
git add . #add project tree index. call it everytime the project tree changed
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

#remote link named as "origin", usr/pass: gmail, g2
#add this repository from web first, then
git remote add origin https://github.com/hongshanzhang012/djDailyReport.git
#this branch will be our master branch 
#master is only a parameter stored in .git/config
git push -u origin master

#clone a copy on deploy server
#Don't create the folder djWeb365, no need
git clone https://github.com/hongshanzhang012/djWeb365.git djWeb365

"""





