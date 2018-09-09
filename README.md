# WortexWeb
This is a simple CMS im working on in my freetime (flask and mongodb)

## features 
* register / login :heavy_check_mark:
* registration activation email :heavy_check_mark:
* stupid egg dashboard :heavy_check_mark:
* user messaging :soon::clock1:
* placeholder for broken feature :x:

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
