#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask
import DAO as dao
import PasswordHasher
import flask_login
import WortexLogger
import Register as reg
from flask import g
import datetime
import config
import EmailService


import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename


#img
from flask import send_from_directory
import os, sys
from PIL import Image

app = flask.Flask(__name__)
app.secret_key = '123123sdas123123sada'  # Change this!!!!!!!!!!!!!!!
# app.debug = config.settings['DEBUG']
# app.port = config.settings['PORT']
app.config['UPLOAD_FOLDER'] = config.settings['UPLOAD_FOLDER']
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

class User(flask_login.UserMixin):
    pass


@app.route("/")
def index():
    return flask.render_template("index.html")


@login_manager.user_loader
def user_loader(email):
    if email not in dao.get_users():
        return

    user = User()
    user.id = email
    g.user = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')

    if email not in dao.get_users():
        return

    user = User()
    user.id = email
    #flask.session['email'] = email
    g.user = email

    password_input = flask.request.form['password']
    password_in_db = dao.get_password_for_user(email)
    user.is_authenticated = PasswordHasher.check_hashed_passwords(password_input, password_in_db)

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template("login.html")

    email = flask.request.form['email']
    password_input = flask.request.form['password']
    password_in_db = dao.get_password_for_user(email)
    if PasswordHasher.check_hashed_passwords(password_input,password_in_db):
        user = User()
        user.id = email
        #flask.session['email'] = email
        g.user = email
        flask_login.login_user(user)
        flask.flash('You successfully logged in!')
        WortexLogger.logging.info("someone logged in! (main)")
        return flask.redirect(flask.url_for('index'))
    WortexLogger.logging.error("Passwords didnt match: {} and {}".format(PasswordHasher.get_hashed_pasword(password_input),password_in_db))
    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('index'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'




@app.route('/profile')
@flask_login.login_required
def profile():
    email = flask_login.current_user.get_id()

    #email = flask.session['email']
    g.user = email
    user = dao.get_user_by_name(email)
    return flask.render_template("profile.html",user=user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = reg.RegistrationForm(flask.request.form)
    if flask.request.method == 'POST' and form.validate():
        user = {}
        #db_session.add(user)
        user['name'] = form.username.data
        user['email'] = form.email.data
        user['password'] = PasswordHasher.get_hashed_pasword(form.password.data)
        user['activation_code'] = PasswordHasher.get_hashed_pasword(user['name'] + "luckyLuck2")
        #EmailService.send_activation_code(user['email'],user['activation_code']) its working 
        success = dao.save_user(user) 
        email = user['email']
        if success: flask.flash('Thanks for registering')
        else: return "error during registration"
        user = User()
        user.id = email
        #flask.session['email'] = email
        g.user = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))
    return flask.render_template('register.html', form=form)

@app.route('/messages', methods=['GET','POST'])
def messages():
    peter = {
        "name":"Peter",
        "email":"peter@parker.com"
    }
    parker = {
        "name":"spuderman",
        "email":"souzderaman@asd.ass"
    }
    users = [
        peter,
        parker
    ]
    return flask.render_template('messages.html', users = users)

@app.route('/messages/<other_user>', methods=['GET','POST'])
def messages2(other_user):
    if dao.other_user_is_valid(other_user):
        print(other_user)
        return flask.render_template('conversation.html')

@app.route('/eggs')
@flask_login.login_required
def eggs():
    last = list(dao.load_eggs(flask_login.current_user.id))
    days_eggs = [item['eggs'] for item in last ]
    days_eggs.reverse()
    days_for_chart = [item['day'] for item in last]
    days_for_chart.reverse()
    return flask.render_template("eggs.html", last_7_days = last, days=days_for_chart, eggs=days_eggs)

@app.route('/eggs/add', methods=['GET',"POST"])
@flask_login.login_required
def eggs_add():
    if flask.request.method == 'POST':
        gyujtes = {}
        gyujtes['day'] = flask.request.form['day']
        gyujtes['time'] = flask.request.form['time']
        gyujtes['person'] = flask.request.form['person']
        gyujtes['eggs'] = flask.request.form['eggs']
        gyujtes['owner_email'] = flask_login.current_user.id
        gyujtes['date'] = datetime.datetime.now()
        dao.save_eggs(gyujtes)
        WortexLogger.logging.info(gyujtes)

        #return flask.render_template("eggs.html")
        return flask.redirect(flask.url_for('eggs'))

    else:
        now = datetime.datetime.now()
        day = now.strftime("%A")
        time = now.strftime('%I:%M:%S %p')
        return flask.render_template("eggs_add.html",day=day, time=time)

@app.route("/activate")
def activate():
    code = flask.request.args.get("code")

    if dao.activate_user(code):
        #siekres
        pass
    #sikertelen
    return "activated"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resize_picture(app.config['UPLOAD_FOLDER']+'/'+filename)
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)





def resize_picture(infile):
    size = 128, 128
    try:
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(infile)
    except IOError:
        WortexLogger.logging.info("cannot create thumbnail for '%s'" % infile)

