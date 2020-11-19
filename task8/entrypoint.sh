#!/bin/sh

##################################################################
# Script for starting application
##################################################################/

# migrate
echo '';
echo 'Start migrate:';
python manage.py makemigrations
python manage.py migrate

# test data
echo '';
echo 'Start init data:';
python manage.py initdata

# application
echo '';
echo 'Start app:';
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:80