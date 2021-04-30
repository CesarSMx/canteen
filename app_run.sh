#!/bin/bash

#execute this file with source app_run.sh

source venv/bin/activate
export FLASK_APP=main.py #This create a enviroment variable needed to run flask
export FLASK_DEBUG=1 #this enable the debug mode

flask run #this command starts the application