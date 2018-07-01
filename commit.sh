#!/bin/bash
source .vnev/bin/activate
pwd
cp web/settings.py web/settings-sample.py
python manage.py collectstatic
git add .
git commit -m "$1"
git push

