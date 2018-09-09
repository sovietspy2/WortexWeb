# WortexWeb
This is a simple CMS im working on in my freetime (flask and mongodb)

## features 
* theme :heavy_check_mark:
* register / login :heavy_check_mark:
* registration activation email :heavy_check_mark:
* stupid egg dashboard :heavy_check_mark:
* user messaging :soon::clock1:
* placeholder for broken feature :x:
* admin panel for user managment :heavy_exclamation_mark:
* user roles :heavy_exclamation_mark:
* security fixes :heavy_exclamation_mark:
* blog :heavy_exclamation_mark:
* analytics :heavy_exclamation_mark:
* search bar :heavy_exclamation_mark:
* multilingual support :heavy_exclamation_mark:

## development setup steps:
1. git clone
2. see config for dev settings
3. to run: flask run 
4. for debugging start app.py in IDE (eg. pycharm)


## prod setup steps: (or script also in my repos)
1. git clone
2. apt install gunicorn
3. pip3 install gunicorn
4. gunicorn 'wsgi:app'
