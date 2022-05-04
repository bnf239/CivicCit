Instructions to run locally
```bash

$ # Get the code
$ git clone https://github.com/bnf239/CivicCit.git
$ cd CivicCit
$
$ # For windows users, download windows subsystem: https://docs.microsoft.com/en-us/windows/wsl/install 
$ 
$ # create virutal environment in the location of the cloned repository
$ virtualenv env
$ source env/bin/activate
$
$ # Install modules
$ pip3 install -r requirements.txt
$ # install postgres and psql client
$ # inside psql client run the following command by replacing the location of your repository
$ \i '{path to repo}/CivicCit/createdb.sql'
$ # In terminal Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application
$ python manage.py runserver 
$ # Access in browser: http://127.0.0.1:8000/