# WortexWeb
This is a simple CMS im working on in my freetime (flask and mongodb)

## features 
* register / login :heavy_check_mark:
* registration activation email :heavy_check_mark:
* stupid egg dashboard :heavy_check_mark:
* user messaging :soon::clock1:
* placeholder for broken feature :x:

## development setup steps:
1 git clone
2 see config for dev settings
3 to run: flask run 
4 for debugging start app.py in IDE (eg. pycharm)


## prod setup steps: (or script also in my repos)
1 git clone
2 apt install gunicorn
3 pip3 install gunicorn
4 gunicorn 'wsgi:app'
