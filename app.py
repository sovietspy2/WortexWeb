import flask
import DAO as dao
import PasswordHasher
import flask_login
import WortexLogger

app = flask.Flask(__name__)
app.secret_key = 'super secret string'  # Change this!


login_manager = flask_login.LoginManager()

login_manager.init_app(app)

# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}



class User(flask_login.UserMixin):
    pass


@app.route("/")
def index():


    #dao.get_password_for_user("qkac")
    return flask.render_template("index.html")


@login_manager.user_loader
def user_loader(email):
    if email not in dao.get_users():
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')

    if email not in dao.get_users():
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    password_input = flask.request.form['password']
    password_in_db = dao.get_password_for_user(email)
    user.is_authenticated = PasswordHasher.check_hashed_passwords(password_input, password_in_db)

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template("index.html")

    email = flask.request.form['email']
    password_input = flask.request.form['password']
    password_in_db = dao.get_password_for_user(email)
    if PasswordHasher.check_hashed_passwords(password_input,password_in_db):
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


if __name__ == '__main__':
    app.run(debug=True)