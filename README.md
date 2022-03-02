Instructions
```bash
$ # Get the code
$ git clone https://github.com/bnf239/CivicCit.git
$ cd CivicCit
$
$ 
$ virtualenv env
$ source env/bin/activate
$
$ # Install modules
$ pip3 install -r requirements.txt
$ # inside psql client run the following command
$ \i '{path to repo}/CivicCit/createdb.sql'
$ # In terminal Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application
$ python manage.py runserver 
$ # Access in browser: http://127.0.0.1:8000/