#!/bin/sh

##################################################################
# Script for starting application
##################################################################/

# migrate
echo '';
echo 'Start migrate:';
cd app
export FLASK_APP=application.py
flask db upgrade
cd ../

# application
echo '';
echo 'Start app:';
python app/main.py