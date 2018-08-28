#!/bin/bash
source .vnev/bin/activate
cp web/settings.py web/settings-sample.py
python manage.py collectstatic
pip freeze > requirements.txt
git checkout developement
git add .
git commit -m "$1"
git push origin developement

