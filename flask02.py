import flask
import flask_shelve
import shelve
from flask_mail import Mail, Message
import random
from passlib.hash import sha256_crypt
from flask import session

app = flask.Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
flask_shelve.init_app(app)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
app.secret_key = 'any random string'
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='asalaanonymous@gmail.com',
    MAIL_PASSWORD='TAOTZ72BNGBC',
)
mail = Mail(app)


def level(password):
    return str(min(len(password), 9))


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        with shelve.open('write') as d:
            data = level(d[username])
        return "Welcome back  " + username + ' !!!' + flask.render_template('page.html', data=data) + \
             flask.render_template('ADD_article.html')
    return "You are not logged in." + "You can still read other's articles and comments." + \
                                      "However you can't writes new articles or comments" + \
                                      "please log in or create a new account to write articles and comment." + \
           flask.render_template('index.html') + flask.render_template('skizb.html')


@app.route('/first_article')
def first_article():
    return flask.render_template('first_article.html') + flask.render_template('Comment_section.html')


@app.route('/create')
def create():
    return flask.render_template('create.html')


@app.route('/send')
def send():
    return flask.render_template('send.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return flask.render_template('logout.html')


@app.route('/send', methods=["GET", "POST"])
def send_mail():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    if flask.request.method == "POST":
        username = flask.request.form['username']
        email = flask.request.form['email']
        passlen = random.randrange(5, 32)
        password = "".join(random.sample(s, passlen))
        str1 = "Hello, {0}. This is your new password: {1}".format(username, password)
        msg = Message(str1,
                      sender=("POWERFUL COMPANY", 'asalaanonymous@gmail.com'),  recipients=[email],)
        msg.body = "Hello, {0}. This is your new password: {1}".format(username, password)
        with shelve.open('write') as d:
            d[username] = sha256_crypt.encrypt(password)
        submit_name = 'Information_Security_Laws_&_Regulations.txt'
        with app.open_resource(submit_name) as fp:
            msg.attach(submit_name, "Information_Security_Laws_&_Regulations/txt", fp.read())
        assert msg.sender == "POWERFUL COMPANY <asalaanonymous@gmail.com>"
        mail.send(msg)
    return "Check your email to find out your new password! " + flask.render_template('index.html')


@app.route('/create', methods=["GET", "POST"])
def create_page():
    if flask.request.method == "POST":
        username = flask.request.form['username']
        password = flask.request.form['password']
        with shelve.open('write') as d:
            flag = username in d
            if flag:
                return "Username you tried to use is already being used. \n" + "  Please try another username. "\
                       + flask.render_template('create.html')
            else:
                if len(password) <= 4:
                    return "Password you tired to use was to too short.   " + \
                           "  Please try another one with at least 5 characters" + flask.render_template('create.html')
                else:

                    d[username] = sha256_crypt.encrypt(password)
                    return "Your account have successfully created. " + "\n" + "  Now you can sign in " + \
                        flask.render_template('index.html')


@app.route('/', methods=["GET", "POST"])
def login_page():
    if flask.request.method == "POST":
        username = flask.request.form['username']
        password = flask.request.form['password']
        data = level(password)
        with shelve.open('write') as d:
            flag = username in d
            if flag:

                if bool(sha256_crypt.verify(password, d[username])):
                    session['username'] = username
                    return "Hello " + username + flask.render_template('page.html', data=data) + \
                           flask.render_template('ADD_article.html')
                else:
                    return "Wrong username or password " + flask.render_template('index.html')
            else:
                return "Wrong username or password. Please try again. " + flask.render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5015)
