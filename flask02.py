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
    d['comments123456'] = [('Algorithms to Live By (Book Review)', 1, """ <p name="ef3d" id="ef3d" class="graf graf--p graf-after--figure">
    Whether you’re a computer science veteran, or just want to dip your toes into the fantastic world of algorithms,
    this book is for you. Being able to explain complex ideas in simple words is the hallmark of mastery of a subject,
    and Brian Christian and Tom Griffiths prove every bit of theirs in this book.</p>
<p name="ae26" id="ae26" class="graf graf--p graf-after--p">
    <em class="markup--em markup--p-em">Algorithms to Live By</em>
    takes you on a journey of eleven ideas from computer science, that we, knowingly or not, use in our lives every day.
    I enjoyed this book a lot, so this review is going to be a long one.</p>
<h4 name="c0d0" id="c0d0" class="graf graf--h4 graf-after--p">1. Optimal Stopping</h4>
<p name="cd61" id="cd61" class="graf graf--p graf-after--h4">Imagine the following scenario:
    you have to hire a secretary from a pool of fixed applicants. You have to interview the candidates one by one and
    make a hire/no-hire decision right after each interview. If you pass on someone, you cannot come back to them.
    If you hire someone, the process stops and they are your new secretary. How do you maximize your chances to find the
    best secretary in the group? This is the famous S<em class="markup--em markup--p-em">ecretary Problem, </em>and
    it forms the basis for the discussion in this chapter.</p>
<p name="4226" id="4226" class="graf graf--p graf-after--p">You probably don’t want to hire the first person you
    interview, since you don’t know what the baseline is. You don’t want to hire the last person either: you almost
    certainly have passed on your best candidate at this point. So the optimal strategy involves interviewing and
    rejecting the first few candidates no matter how good they are: just to set up the baseline first and then hiring
    the best you’ve seen so far after. This <em class="markup--em markup--p-em">optimal</em> point turns out to be
    <code class="markup--code markup--p-code">1/e</code> or about 37%. Reject 37% of the applicants, and then hire
    the next one better than anyone you’ve seen so far. Variants of this <em class="markup--em markup--p-em">Secretary
        Problem </em>and the accompanying <em class="markup--em markup--p-em">37% Rule </em>apply to vast areas of real
    life too — from dating to parking your car to selling/buying a house: knowing when to stop looking is crucial.
    Before you get too excited, here’s the sobering bit: this optimal strategy fails 63% of the time.</p>
<h4 name="70f0" id="70f0" class="graf graf--h4 graf-after--p">2. Explore/Exploit</h4>
<p name="69db" id="69db" class="graf graf--p graf-after--h4">It’s Saturday and it’s your cheat day. Do you open Yelp
    and explore a new restaurant, or do you go back to the sandwich place you’ve been craving all week? Do you put on
    Spotify’s Daily Mix, or do you just go back to listening to your favorite albums? In other words, do you
    <em class="markup--em markup--p-em">explore</em>, or do you <em class="markup--em markup--p-em">exploit</em>?
    From A/B Testing websites to A/B Testing human drugs via clinical trials, software engineers and pharmaceutical
    companies alike are trying to figure out where the balance lies. In addition to discussing a number of strategies
    like “<em class="markup--em markup--p-em">Win-Stay, Lose-Shift”</em> to win the slot machines on a casino floor
    (formally known as the
    <a href="https://en.wikipedia.org/wiki/Multi-armed_bandit" data-href="https://en.wikipedia.org/wiki/Multi-armed_bandit" class="markup--anchor markup--p-anchor" rel="noopener" target="_blank"><em class="markup--em markup--p-em">multi-armed bandit problem</em></a>), this chapter will help you think better next time you have to pick between the latest or the greatest.</p><h4 name="7cb2" id="7cb2" class="graf graf--h4 graf-after--p">3. Sorting</h4><p name="937b" id="937b" class="graf graf--p graf-after--h4">Sorting algorithms are usually the first ones that any introductory Computer Science course covers. Topics discussed here go from the <em class="markup--em markup--p-em">Big O notation</em> that serves as a yardstick for measuring the performance of algorithms, to the bouquet of sorting algorithms themselves: the <em class="markup--em markup--p-em">bubble</em>, <em class="markup--em markup--p-em">insertion</em>, <em class="markup--em markup--p-em">merge</em> and <em class="markup--em markup--p-em">quick</em> sorts. Moreover, sorting is prophylaxis for search: if you have your collection sorted, searching becomes a whole lot easier. The chapter ends with a discussion on tournaments of various types:<em class="markup--em markup--p-em"> round-robin</em>, <em class="markup--em markup--p-em">ladder</em>, <em class="markup--em markup--p-em">single-elimination</em> and so on. After all, tournaments are just another sorting problem, and so are the pecking orders and dominance hierarchies in the animal (and human) kingdom. Keeping things sorted just makes life easier.</p><h4 name="7fd8" id="7fd8" class="graf graf--h4 graf-after--p">4. Caching</h4><p name="6e14" id="6e14" class="graf graf--p graf-after--h4">Or, the memory hierarchy — and what to keep on top of your mind, and what to delegate to pen and paper or a Notes app. Any discussion on caching necessitates a look into various strategies for deciding what stays in a cache — strategies like <em class="markup--em markup--p-em">Random Eviction</em>, <em class="markup--em markup--p-em">First-In-First-Out</em>, <em class="markup--em markup--p-em">Least Recently Used</em> and so on help. One thing I really liked here was how the <em class="markup--em markup--p-em">Least Recently Used</em> can be effectively applied to a physical library: instead of putting the returned books back on the shelves, libraries could use them to create a cache section — after all, the books that were most recently borrowed are most likely to get borrowed again!</p><h4 name="7149" id="7149" class="graf graf--h4 graf-after--p">5. Scheduling</h4><p name="b25d" id="b25d" class="graf graf--p graf-after--h4">How do you get things done? How do you schedule your day? How do you arrange the tasks so that the most gets done in the least amount of time? Moreover, how do you handle a situation where a low priority task is blocking a higher priority task, and you’re just stuck in a <em class="markup--em markup--p-em">priority inversion</em>? This chapter was almost like revisiting a bunch of old friends from undergrad: you don’t think about <em class="markup--em markup--p-em">Preemption</em> or <em class="markup--em markup--p-em">Thrashing</em> in your day-to-day work much.</p><h4 name="f916" id="f916" class="graf graf--h4 graf-after--p">6. Bayes’s Rule</h4><p name="9cf0" id="9cf0" class="graf graf--p graf-after--h4">I’m assuming you already know Bayes’s Rule, but if you don’t, it’s just a simple way to determine how probable something <code class="markup--code markup--p-code">A</code>is given something else <code class="markup--code markup--p-code">B</code>has happened, usually denoted as <code class="markup--code markup--p-code">P(A|B)</code>. It’s assumed you have good information about the <em class="markup--em markup--p-em">priors</em>: how likely those two things are to happen independently, and you know how likely things are things to occur the other way: <code class="markup--code markup--p-code">B|A</code> I’ll just write it out. To get <code class="markup--code markup--p-code">P(A|B)</code>, multiply <code class="markup--code markup--p-code">P(B|A)</code>with <code class="markup--code markup--p-code">P(A)</code>and divide by <code class="markup--code markup--p-code">P(B)</code>. It’s really that simple. Just make sure your priors are good: a good reminder in this chapter was that exposure to just news and not much else serves to contaminate them, making us worse predictors of events.</p><p name="0ab2" id="0ab2" class="graf graf--p graf-after--p">The <em class="markup--em markup--p-em">Copernican Principle</em>, which dictates that a good prediction for how long something will last is to see how long it has already lasted, resurfaced in this chapter: it was also a key topic in <a href="https://anantja.in/antifragile-things-that-gain-from-disorder-8a0e86257edb" data-href="https://anantja.in/antifragile-things-that-gain-from-disorder-8a0e86257edb" class="markup--anchor markup--p-anchor" rel="noopener" target="_blank">Antifragile</a> that I reviewed last month: it applies to things that are antifragile (like books) and not to those that are not (like human lifespans).</p><p name="6b1f" id="6b1f" class="graf graf--p graf-after--p">On that note, the three basic probability distributions: Additive rule (<em class="markup--em markup--p-em">Erlang prior</em>), Multiplicative rule (<em class="markup--em markup--p-em">Power Law prior</em>), and Average rule (<em class="markup--em markup--p-em">Normal prior</em>) are explained in this chapter in a very elegant and easy-to-read prose. <a href="https://anantja.in/writing-to-learn-9ed157c4fe4a" data-href="https://anantja.in/writing-to-learn-9ed157c4fe4a" class="markup--anchor markup--p-anchor" rel="noopener" target="_blank"><em class="markup--em markup--p-em">Writing across curriculum</em></a> should really be mandated, and I was impressed to read about these ideas without a single mathematical equation or graph.</p><h4 name="cb4c" id="cb4c" class="graf graf--h4 graf-after--p">7. Overfitting</h4><p name="70df" id="70df" class="graf graf--p graf-after--h4">This chapter is focussed on the case against complexity, and on keeping your models as simple as possible: not only they work better, but one can argue that simplicity should be a goal in itself. Folks in Machine Learning would love the discussion of ideas around <em class="markup--em markup--p-em">cross-validation</em> (hold some of your data back to test later that your learned model <em class="markup--em markup--p-em">generalizes</em> well, that it doesn’t just <em class="markup--em markup--p-em">overfit</em> your training data), <em class="markup--em markup--p-em">regularization</em> (penalize your models for complexity: so that simplicity is a part of the goal), <em class="markup--em markup--p-em">early stopping</em> and so on.</p><h4 name="d2c7" id="d2c7" class="graf graf--h4 graf-after--p">8. Relaxation</h4><p name="97ee" id="97ee" class="graf graf--p graf-after--h4">The perfect is the enemy of the good, so it’s okay to just relax and let it slide once in a while. A large class of problems in Computer Science, known as <em class="markup--em markup--p-em">NP-Hard Problems, </em>are intractable. For any realistic dataset, we have no way to compute a perfect solution in any reasonable amount of time. The most famous example of this is the <em class="markup--em markup--p-em">Travelling Salesman Problem</em>: figure out a route that a salesman should travel to visit all his stops with the least distance covered: the possibilities here are way too many to consider one by one. Relaxing the constraints and solving a similar, but an easier problem seems to be the solution. Any optimization problem has two parts — the rules and the scorekeeping. It may be worth violating the rules sometimes and take a hit on the score as long as it keeps you moving ( this is actually called <em class="markup--em markup--p-em">Lagrangian Relaxation</em>).</p><h4 name="c7c8" id="c7c8" class="graf graf--h4 graf-after--p">9. Randomness</h4><p name="916a" id="916a" class="graf graf--p graf-after--h4">Randomness is another thing that works when nothing else works. Starting with the <em class="markup--em markup--p-em">Monte Carlo Method</em>, this chapter talks about <em class="markup--em markup--p-em">Randomized Algorithms</em> — and you have to love this part of Computer Science since this is where things stop being so exact. Not only that, <em class="markup--em markup--p-em">Randomness</em> can save you in <em class="markup--em markup--p-em">Optimization</em>, making sure you don’t get trapped in a<em class="markup--em markup--p-em"> local minimum </em>while<em class="markup--em markup--p-em"> hill climbing </em>your way. I really loved how this chapter ended with a discussion on randomness, evolution, and creativity. After all, you can make a case that all art stems out of some form of randomness.</p><h4 name="ee8d" id="ee8d" class="graf graf--h4 graf-after--p">10. Networking</h4><p name="219b" id="219b" class="graf graf--p graf-after--h4"><em class="markup--em markup--p-em">Packet Switching, ACKnowledgements, triple handshakes, exponential backoff</em> and the algorithms of forgiveness: networking is another topic full of gems. Connecting people is one of the most fundamental and impactful areas of Computer Science — we’re talking about the internet here. How to control the flow, how to avoid congestions (<em class="markup--em markup--p-em">Additive Increase, Multiplicative Decrease</em>), how to establish Backchannels (and the role of white noise and little acknowledgments in everyday real-life conversations!), and how to avoid <em class="markup--em markup--p-em">bufferbloats</em>: these are some of the topics that are part of any Computer Networking class, but it was great to see them in a new light.</p><h4 name="2f9d" id="2f9d" class="graf graf--h4 graf-after--p">11. Game Theory</h4><p name="2dc5" id="2dc5" class="graf graf--p graf-after--h4"><em class="markup--em markup--p-em">The Prisoners Dilemma</em>: the paradox where two individuals acting in their own self-interest does not result in the optimal outcome. Succinctly, think of two prisoners being interrogated by a detective: if they rat each other out, they both have to serve time in the prison, but if only one rats the other out, he gets to walk away free while the other one goes behind the bars. If they both stay loyal to each other, both of them walk away free: but this optimal outcome will never be reached if both the prisoners act in their self-interest — which is something you would expect them to do.</p><p name="f790" id="f790" class="graf graf--p graf-after--p graf--trailing">This is the core problem used to introduce anyone to Game Theory: the beautiful field of Nash Equilibria, Dominant Strategies, Tragedy of the Commons and infinite recursions of getting into each other’s minds. The panacea: if you’re trapped in a game that lends itself to paradoxical incentives, change the game: set the rules so that there’s no incentive to act any other way. Have the mafia waiting outside the prison so that the one who rats his comrade is found getting eaten by the fish at the bottom of the local lake the next day. From poker to auctions, especially ad auctions that form the basis of the internet economy today (think Google and Facebook), Game Theory is another field of computer science/math that you cannot miss to explore!</p></div></div></section><section name="34b1" class="section section--body section--last"><div class="section-divider"><hr class="section-divider"></div><div class="section-content"><div class="section-inner sectionLayout--insetColumn"><p name="f13e" id="f13e" class="graf graf--p graf--leading">Overall, I was left marveling at the authors’ ability to boil ideas from Computer Science down to their very core. This book is the perfect first introduction to this vast and beautiful field, and should be a required reading for any CS101 course. In some sense, it was a mini re-education for me too, and taught me a lot about how to talk about and teach Computer Science.</p>""",
                            'khachdallak', 0),
                           ('AAHhaaha Python', 2, """<img src="/static/python.jpg"> <br/><br/>""", 'khachdallak', 0),
                           ('Благотворительный фонд принца Чарльза оказался связан с российской сетью офшоров',
                           3, """<br/> <img src="/static/rv.jpg" align="right"><br/>Российский инвестбанк, глава которого встречался с принцем Чарльзом, управлял сетью офшорных компаний, через которые из<br />России были выведены миллиарды долларов.<br /><br />Международное расследование выявило, как сеть офшоров получала деньги от компаний, связанных с масштабной аферой.<br /><br />Олигарх, о котором идет речь, - Рубен Варданян, бывший глава инвестиционного банка "Тройка Диалог".<br /><br />"Европейский офшор": как россияне могли отмывать деньги в Шотландии<br />Друзья Путина с 24 млрд долларов: главное в расследовании OCCRP<br />Как Европа пытается покончить с отмыванием российских денег и что ей мешает<br />Сам он говорит, что не был вовлечен в повседневные операции банка.<br /><br />Деньги, поступавшие из офшорной сети, направлялись в числе прочего в Благотворительный фонд принца Уэльского на<br />реставрацию исторического поместья XVIII века Дамфрис-Хаус в Шотландии.<br />В фонде заявили, что подвергали пожертвования Варданяна тщательной юридической проверке,<br />которая не выявила поводов для опасений.<br />Сеть из более чем 70 офшорных компаний была выявлена в результате утечки базы 1,3 млн банковских транзакций,<br />доступ к которой получил Центр по исследованию коррупции и организованной преступности (OCCRP).<br />Организация предоставила доступ к документам журналистам Би-би-си и газеты Guardian.<br /><br />В период между 2009 и 2011 годами Благотворительный фонд принца Уэльского получил три платежа на общую сумму 202 тысячи<br />долларов через литовский банк Ukio, который был закрыт в 2013 году.<br /><br />Платежи отправляла компания Quantus Division Ltd, которая, как следует из опубликованных документов,<br />была частью сети офшоров, использовавшихся для вывода миллиардов долларов из России.<br /><br />Сетью управлял московский инвестиционный банк "Тройка Диалог", генеральным директором которого был Варданян.<br /><br />На протяжении ряда лет Варданян поддерживал филантропические и деловые отношения с принцем Чарльзом.<br /><br />В 2010 году банкир посетил мероприятие в Виндзорском замке, посвященное армянской культуре.<br />Там выступал принц Чарльз, говоривший о планах реставрации Дамфрис-Хауса.<br /><br />Сеть "Тройки"<br />Большинство транзакций, фигурирующих в базе, прошло через литовский банк Ukio Bancas,<br />закрытый властями страны в 2013 году.<br /><br />В период между 2005 и 2011 годами более 3,35 млрд евро было направлено в сеть офшорных компаний,<br />управлявшуюся "Тройкой"; выведено было 3,5 млрд евро. Компании, по всей видимости,<br />использовались для анонимного перемещения денег.<br />Десятки миллионов<br />Из документов также следует, что десятки миллионов долларов поступали в компании,<br />входившие в сеть, от других компаний, которые были связаны с тяжкими преступлениями.<br /><br />В их числе одна из крупнейших в России афер, раскрытая юристом Сергеем Магнитским:<br />мошенничество с налогами на сумму в 230 млн долларов.<br /><br />В итоге российские власти обвинили самого Магнитского в уклонении от уплаты налогов.<br />В 2009 году он скончался при подозрительных обстоятельствах в следственном изоляторе "Матросская тишина".<br /><br />Утечка банковских данных из Ukio Bancas показывает, что компании, заработавшие на той афере, провели через схему<br />"Тройки" 123 млн долларов.<br /><br />Би-би-си не обнаружила никаких свидетельств того, что лично Варданян был вовлечен в какую-либо незаконную деятельность.<br /><br />Его юристы сообщили нам, что он не занимался оперативным управлением "Тройкой" и его деятельность всегда носила<br />открытый характер.<br /><br />Пресс-секретарь Кларенс-Хауса собщил, что благотворительные фонды принца Уэльского действуют независимо от самого<br />принца касательно любых решений по вопросу сбора пожертвований.<br /><br />"Благотворительные организации придерживаются строгих процедур проверки юридической чистоты.<br />В описываемых примерах проверка не выявила каких-либо факторов риска", - заявил Би-би-си представитель <br />Благотворительного фонда принца Уэльского.<br /><br />Сеть этих компаний была создана "Тройкой" для обслуживания клиентов, многие из которых относятся к российской элите.<br />Они использовались для перемещения средств по всему миру, как в бизнес-целях, так и для личного пользования.<br /><br />Эти деньги шли на самые разные нужды - от покупки недвижимости в Великобритании, <br />яхт и произведений искусства до билетов на чемпионат мира по футболу.<br /><br />Рубен Варданян и его партнеры в 2011 году заработали 1 млрд долларов, продав "Тройку" государственному Сбербанку.<br /><br />Из документов, с которыми ознакомилась Би-би-си, следует, что в назначении платежей, <br />поступавших в адрес Quantus Division Ltd и других задействованных в офшорной сети компаний, указывалось, <br />что они идут в оплату продуктов питания, электроники, стройматериалов и даже сантехники.<br /><br />Все эти "закупки", однако, осуществлялись компаниями, у которых не было офисов и сотрудников, <br />и в отношении которых нет свидетельств реального ведения торговой деятельности. Это может говорить о том, <br />что в действительности никакие из этих поставок не осуществлялись.<br /><br />Комментарий пресс-службы Рубена Варданяна<br /><br />За всю историю существования группа компаний "Тройка Диалог" действовала в полном соответствии с принципами <br />прозрачности и международными стандартами финансовой отчетности. Более того,<br />она активно участвовала в формировании цивилизованного финансового рынка России.<br /><br />После продажи группы компаний "Тройка Диалог" Сбербанку в 2012 году господин Варданян посвятил много времени и ресурсов<br />филантропической деятельности. А обязательства инвестировать большую часть своего состояния на благотворительные <br />проекты семья господина Варданяна взяла на себя еще в середине 2000-х годов.<br /><br />Более подробные комментарии будут даны после тщательного изучения фактов, упомянутых в публикациях.<br /><br />Комментарий пресс-службы Сбербанка России<br /><br />"Факты, изложенные в статье, не имели и не имеют отношения к Сбербанку.<br />Упомянутые операции совершались со счетов компаний, которые никогда не входили в периметр сделки по покупке <br />Сбербанком компании "Тройка Диалог".<br /><br />Структуры Сбербанка не участвовали в сопровождении операций".<br/></br>""",
                             'khachdallak', 0)]
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
        s += '<p><a href=/articles/'
        s += str(i[1])
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
    return hello(articles[0][0], articles[0][2], articles[0][4], articles[0][3])
        #flask.render_template('first_article.html', rating=articles[0][4]) + all_comments + flask.render_template('Comment_section.html')


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


@app.errorhandler(404)
def page_not_found(error=None):
    return flask.render_template('page_not_found.html'), 404


@app.route('/articles/')
@app.route('/articles/<title>')
def hello(title=None, text=None, rating=None, author=None):
    n = flask.request.base_url
   # return hello(articles[0][0], articles[0][2], articles[0][4], articles[0][3])
    for article in articles:
        if article[1] != int(n[-1]):
            continuess
        title = article[0]
        text = article[2]
        rating = article[4]
        author = article[3]
        return flask.render_template('first_article.html', title=title, rating=rating, author=author) + text
    return "There is no such articles, please type article name correctly"


@app.route('/articles/<name>', methods=["GET", "POST"])
def comments():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5015)
