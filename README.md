# WortexWeb
This is webapp with flask and mongodb


development setup:
git clone
see config for dev settings
to run: flask run 
for debugging start app.py in IDE (eg. pycharm)


prod setup:
git clone
apt install gunicorn
pip3 install gunicorn
gunicorn 'wsgi:app'
