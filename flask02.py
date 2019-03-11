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
with shelve.open('write') as d:
    d['comments123456'] = [('Algorithms to Live By (Book Review)', 1, """'first_article'""", 'khachdallak', 0),
                           ('AAHhaaha Python', 2, """'second_article'""", 'khachdallak', 0),
                           ('Благотворительный фонд принца Чарльза оказался связан с российской сетью офшоров',
                           3, """'third_article'""",'khachdallak', 0)]
    d['naxord123456'] = len(d['comments123456'])
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
        if len(articles) > d['naxord123456']:
            email = d['male{name}'.format(name=articles[-1][3])]
            str1 = 'Congrats {0}, your article has proved '.format(articles[-1][3])
            msg = Message(str1,
                          sender=("POWERFUL COMPANY", 'asalaanonymous@gmail.com'), recipients=[email], )
            msg.body = 'Congrats {0}, your article has proved '.format(articles[-1][3])
            submit_name = 'Information_Security_Laws_&_Regulations.txt'
            assert msg.sender == "POWERFUL COMPANY <asalaanonymous@gmail.com>"
            mail.send(msg)
    else:
        articles = []
    d['naxord123456'] = len(d['comments123456'])


def listeverything(s=''):
    for i in articles:
        s += '<p><a href='
        s += i[2]
        s += '>'
        s += i[0]
        s += '</a> </p>'
    return s


def reject(sad_username):
    email = d['male{name}'.format(name=sad_username)]
    str1 = 'Sorry, {0}, ' \
           'we have to reject your article, because its content was inappropriate with our site '.format(sad_username)
    msg = Message(str1,
                  sender=("POWERFUL COMPANY", 'asalaanonymous@gmail.com'), recipients=[email], )
    msg.body = str1
    assert msg.sender == "POWERFUL COMPANY <asalaanonymous@gmail.com>"
    mail.send(msg)
    return None


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
    if 'username' in session:
        username = session['username']
        return flask.render_template('add_article_main_page.html', data=str(username))
    else:
        return "You are not allowed to access to this site if you aren't signed in. " \
               "Please go home, sign in, to get acces to this page." + """<a href='/'> <h2>GO HOME</h2></a>"""


@app.route('/first_article')
def first_article():
    a = list(comments.items())
    qanak = 0
    qanak += sum(len(i[1]) for i in a)
    all_comments = str(qanak) + ' Comments' + '<br/>'
    for i in a:
        for individual in i[1]:
            all_comments += str(str(i[0]) + ' : ' + str(individual) + '<br/>')
    return flask.render_template('first_article.html', rating=articles[0][4]) + all_comments + flask.render_template('Comment_section.html')


@app.route('/second_article')
def second_article():
    a = list(comments2.items())
    qanak = 0
    qanak += sum(len(i[1]) for i in a)
    all_comments = str(qanak) + ' Comments' + '<br/>'
    for i in a:
        for individual in i[1]:
            all_comments += str(str(i[0]) + ' : ' + str(individual) + '<br/>')
    return flask.render_template('second_article.html', rating=articles[1][4]) + \
           all_comments + flask.render_template('Comment_section.html')


@app.route('/third_article')
def third_article():
    a = list(comments3.items())
    qanak = 0
    qanak += sum(len(i[1]) for i in a)
    all_comments = str(qanak) + ' Comments' + '<br/>'
    for i in a:
        for individual in i[1]:
            all_comments += str(str(i[0]) + ' : ' + str(individual) + '<br/>')
    return flask.render_template('third_article.html', rating=articles[2][4]) + \
           all_comments + flask.render_template('Comment_section.html')


@app.route('/all_comments')
def all_comments():
    if 'username' in session:
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


@app.route('/add', methods=["GET", "POST"])
def add_article():
    if flask.request.method == "POST":
        title = flask.request.form["title"]
        text = flask.request.form["text"]
        with shelve.open('write') as d:
            if 'index123456' in d:
                indexa = d['index123456']
            else:
                indexa = 0
            f = open(r"templates\approve{name}.html".format(name=s[indexa]), "w+")
            indexa += 1
            d['index123456'] = indexa
        f.write(title+'<br/>' + text)
        return "Your article has sent to administration.<br/> If you want to be aware of your article's destiny" \
               "(whether we " \
               "reject or approve it), write hear your email. We will send you email as soon as we know the result." \
               "<br/>  " \
                + """<br/> <form action="/inform" method = "POST">
                        <div>
                            <input type="text" placeholder="Email" required=""  name = "email"/>
                        </div><br />
                        <div>
                            <input type="submit" value="Submit" />
                            <br />
                        </div>
                    </form>"""


@app.route('/inform', methods=["GET", "POST"])
def inform():
    if flask.request.method == "POST":
        with shelve.open('write') as d:
            if 'index123456' in d:
                indexa = d['index123456']
            else:
                indexa = 0
            d['mail{name}'.format(name=session['username'])] = flask.request.form['email']
        print(flask.request.form['email'])
    return "We will have a look on you article asap" + """<br/> <a href = '/'> Go back home</a>"""


@app.errorhandler(404)
def page_not_found(error=None):
    return flask.render_template('page_not_found.html'), 404


@app.route('/articles/')
@app.route('/articles/<name>')
def hello(title=None, text=None, rating=None, author=None):
    return flask.render_template('first_article.html', title=title, text=text, rating=rating, author=author)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5015)
    sad_username = input()
    reject(sad_username)
