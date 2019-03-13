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
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"



def listeverything(s='', articles=[]):
    for i in articles:
        s += '<p><a href=/articles/'
        s += str(i[1])
        s += '>'
        s += i[0]
        s += '</a> </p>'
    return s


def sortsecond(val):
    return val[1]


def level(password):
    return str(min(len(password), 9))


def sortfirst(val):
    return val[0]


@app.route('/')
def index():
    with shelve.open('write') as d:
            articles = d['comments123456']
    articles.sort(key=sortsecond)
    listarticles = listeverything(articles=articles)
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
    if 'username' in session:
        username = session['username']
        return flask.render_template('add_article_main_page.html', data=str(username))
    else:
        return "You are not allowed to access to this site if you aren't signed in. " \
               "Please go home, sign in, to get acces to this page." + """<a href='/'> <h2>GO HOME</h2></a>"""


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
    with shelve.open('write') as d:
        if 'comments123456' in d:
            articles = d['comments123456']
        else:
            articles = []
    if flask.request.form["list"] != "Sort":
        if flask.request.method == "POST":
            articles.sort(key=sortsecond)
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
        with shelve.open('write') as d:
                articles = d['comments123456']
        if flask.request.method == "POST":
            data = 0
            value = flask.request.form['rating']
            if value == "date1":
                articles.sort(key=sortsecond)
            if value == "date2":
                articles.sort(key=sortsecond, reverse=True)
            if value == "name":
                articles.sort(key=sortfirst)
            listarticles = listeverything(articles=articles)
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


@app.route('/add', methods=["GET", "POST"])
def add_article():
    if 'username' in session:
        if flask.request.method == "POST":
            title = flask.request.form["title"]
            text = flask.request.form["text"]
            username = session['username']
            with shelve.open('write') as d:
                a = ['', 0, text, username, 0, """"""]
                a[0] = title
                a[1] = len(d['comments123456']) + 1
                d['comments123456'] += [a]

        return "Your article has successfully added "+"""<a href ='/'> GO HOME</a>"""
    else:
        return "You are not allowed to access to this site if you aren't signed in. " \
               "Please go home, sign in, to get acces to this page." + """<a href='/'> <h2>GO HOME</h2></a>"""


@app.errorhandler(404)
def page_not_found(error=None):
    return flask.render_template('page_not_found.html'), 404


def number(st):
    s = ''
    i = 1
    while (i <= len(st)) and (st[-i] != '/'):
        s += st[-i]
        i += 1

    return s[::-1]


@app.route('/articles/')
@app.route('/articles/<title>')
def hello(title=None, text=None, rating=None, author=None, comment=None):
    numb = number(flask.request.base_url)
   # return hello(articles[0][0], articles[0][2], articles[0][4], articles[0][3])
    with shelve.open('write') as d:
        for article in d['comments123456']:
            if article[1] != int(numb):
                continue
            title = article[0]
            text = article[2]
            rating = article[4]
            author = article[3]
            comment = article[5]
            print(comment)
            return flask.render_template('first_article.html', title=title, rating=rating, author=author) + text\
                + comment + flask.render_template('Comment_section.html', name=numb)
        return "There is no such articles, please type article name correctly"


@app.route('/articles/<name>', methods=["GET", "POST"])
def comments(name=None):
    numb = number(flask.request.base_url)
    username = session['username']
    comment = flask.request.form['comment']
    if flask.request.method == "POST":
        with shelve.open('write') as d:
            for article in d['comments123456']:
                if article[1] != int(numb):
                    continue
                print(article[5])
                l=[article[5], str(username + ":" + comment + "<br/>")]
                print(l)
                article[5] = ''.join(l)
                print(article[5])
                title = article[0]
                text = article[2]
                rating = article[4]
                author = article[3]
                comment2 = article[5]
                print(article[5])
    return "Your comment has successfully added " + flask.render_template('first_article.html', title=title, rating=rating, author=author) + text\
                + comment2 + flask.render_template('Comment_section.html', name=numb)



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5015)
