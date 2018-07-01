source .vnev/bin/activate
cp web/settings.py web/settings-sample.py
git add .
git commit -m "$1"
git push

