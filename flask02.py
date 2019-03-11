import flask
import flask_shelve
import shelve
from flask_mail import Mail, Message
import random
from passlib.hash import sha256_crypt
from flask import session
# password for khachdallak - $CND!bmoJr1ZQpO6w0Ux
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
with shelve.open('write') as d:
    #d['comments123456'] = [('Algorithms to Live By (Book Review)', 1, """'first_article'"""),
                     #      ('AAHhaaha Python', 2, """'second_article'"""),
                       #    ('Благотворительный фонд принца Чарльза оказался связан с российской сетью офшоров',
                      #      3, """'third_article'""")]
    if 'comments123' in d:
        comments = d['comments123']
    else:
        comments = {}
    if 'comments1234' in d:
        comments2 = d['comments1234']
    else:
        comments2 = {}
    if 'comments12345' in d:
        comments3 = d['comments12345']
    else:
        comments3 = {}
    if 'comments123456' in d:
        articles = d['comments123456']
    else:
        articles = []


def listeverything(s=''):
    for i in articles:
        s += '<p><a href='

        s += i[2]
        s += '>'
        s += i[0]
        s += '</a> </p>'
    return s


def sortSecond(val):
    return val[1]


def level(password):
    return str(min(len(password), 9))


def sortFirst(val):
    return val[0]


@app.route('/')
def index():
    articles.sort(key=sortSecond)
    listarticles = listeverything()
    if 'username' in session:
        username = session['username']
        with shelve.open('write') as d:
            data = level(d[username])
        return \
            "Welcome back  " + username + ' !!!' + flask.render_template('page.html', data=data) + \
            """<a href='all_comments'> All my comments</a><br/> 
            <h1> Articles </h1>
            """ + listarticles + flask.render_template('ADD_article.html')
    return "You are not logged in." + "You can still read other's articles and comments." + \
                                      "However you can't writes new articles or comments" + \
                                      "please log in or create a new account to write articles and comment." + \
           flask.render_template('index.html') +\
                    """<h1> Articles </h1>""" + listarticles + flask.render_template('skizb.html')


@app.route('/add')
def add():
    username = session['username']
    return flask.render_template('add_article_main_page.html', data=str(username))


@app.route('/first_article')
def first_article():
    a = list(comments.items())
    qanak = 0
    qanak += sum(len(i[1]) for i in a)
    all_comments = str(qanak) + ' Comments' + '<br/>'
    for i in a:
        for individual in i[1]:
            all_comments += str(str(i[0]) + ' : ' + str(individual) + '<br/>')
    return flask.render_template('first_article.html') + all_comments + flask.render_template('Comment_section.html')


@app.route('/second_article')
def second_article():
    a = list(comments2.items())
    qanak = 0
    qanak += sum(len(i[1]) for i in a)
    all_comments = str(qanak) + ' Comments' + '<br/>'
    for i in a:
        for individual in i[1]:
            all_comments += str(str(i[0]) + ' : ' + str(individual) + '<br/>')
    return flask.render_template('second_article.html') + all_comments + flask.render_template('Comment_section.html')


@app.route('/third_article')
def third_article():
    a = list(comments3.items())
    qanak = 0
    qanak += sum(len(i[1]) for i in a)
    all_comments = str(qanak) + ' Comments' + '<br/>'
    for i in a:
        for individual in i[1]:
            all_comments += str(str(i[0]) + ' : ' + str(individual) + '<br/>')
    return flask.render_template('third_article.html') + all_comments + flask.render_template('Comment_section.html')


@app.route('/all_comments')
def all_comments():
    username = session['username']
    a = list(comments.items())
    all_comments = ''
    qaunt = 1
    for i in a:
        for individual in i[1]:
            if str(i[0]) == username:
                all_comments += str(str(qaunt) + ' : ' + str(individual) + '<br/>')
                qaunt += 1
    return "Here are listed all the comments of " + username + ' : ' + '<br/><br/><br/><br/>' + all_comments


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
    if flask.request.form["list"] != "Sort":
        if flask.request.method == "POST":
            articles.sort(key=sortSecond)
            listarticles = listeverything()
            username = flask.request.form['username']
            password = flask.request.form['password']
            data = level(password)
            with shelve.open('write') as d:
                flag = username in d
                if flag:

                    if bool(sha256_crypt.verify(password, d[username])):
                        session['username'] = username
                        return "Hello " + username + flask.render_template('page.html', data=data) + \
                               """<a href='all_comments'> All my comments</a><br/> 
                                           <h1> Articles </h1>
                                           """ + listarticles + \
                               flask.render_template('ADD_article.html')
                    else:
                        return "Wrong username or password. Please try again " + flask.render_template('index.html')
                else:
                    return "Wrong username or password. Please try again. " + flask.render_template('index.html')
    else:
        if flask.request.method == "POST":
            data = 0
            value = flask.request.form['rating']
            if value == "date1":
                articles.sort(key=sortSecond)
            if value == "date2":
                articles.sort(key=sortSecond, reverse=True)
            if value == "name":
                articles.sort(key=sortFirst)
            listarticles = listeverything()
            if 'username' in session:
                username = session['username']
                with shelve.open('write') as d:
                    data = level(d[username])
            if 'username' in session:
                return \
                           flask.render_template('page.html', data=data) + \
                            """<a href='all_comments'> All my comments</a><br/> 
                            <h1> Articles </h1>
                """ + listarticles + flask.render_template('ADD_article.html')
            else:
                return \
                    """ <h1> Articles </h1>
        """ + listarticles + flask.render_template('skizb.html')


@app.route('/first_article', methods=["GET", "POST"])
def first_comment():
    if flask.request.method == "POST":
        if 'username' in session:
            username = session['username']

            text = flask.request.form['comment']
            if username in comments:
                comments[username].append(text)
            else:
                comments[username] = [text]
            with shelve.open('write') as d:
                d['comments123'] = comments
            return """<meta http-equiv=refresh content=0; 'first_article' />"""
        else:
            return "You need to be loged in, if you want to comment on this article   " + """<a href='/'>Login</a>""" +\
                flask.render_template('first_article.html') + flask.render_template('Comment_section.html') + \
                   "You need to be loged in, if you want to comment on this article   " + """<a href='/'>Login</a>"""

        
@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('page_not_found.html'), 404


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return flask.render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5015)
