# WortexWeb
This is a simple CMS im working on in my freetime (flask and mongodb)

## development setup steps:
* git clone
* see config for dev settings
* to run: flask run 
* for debugging start app.py in IDE (eg. pycharm)


## prod setup steps:
* git clone
* apt install gunicorn
* pip3 install gunicorn
* gunicorn 'wsgi:app'
