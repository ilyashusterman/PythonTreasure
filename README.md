# PythonTreasure

URL to app link https://protected-crag-23055.herokuapp.com/

List of python django commands to get started : 

django-admin startapp main_app

python manage.py startapp www 
##www-- main page
runs server
python manage.py runserver

python manage.py makemigrations # creates the model into the database

python manage.py migrate # migrate the Model schema to the database

python manage.py sqlmigrate main_app 0001  # show the list of commands of sql

python manage.py migrate # main_app 

python manage.py loaddata www.example.json $$ that django db will load the data into the sqllite database
###########################################################

python manage.py shell # python shell

from main_app.models import MyModel

MyModel.objects.all()

Treasure.objects.filter(location = 'Tel-aviv')

to create super user 
python manage.py createsuperuser

to add model to the admin page 

admin.site.register(Treasure)

##############################################
Django commands 

django-admin startproject MyProjectName



Author :
Ilya Shusterman

