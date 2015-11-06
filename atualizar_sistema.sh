#!/bin/bash
git checkout .
git pull origin master
python manage.py migrate
