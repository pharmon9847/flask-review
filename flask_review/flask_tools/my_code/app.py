from flask import Flask, request, render_template,  redirect, flash,  jsonify, session
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

COMPLIMENTS = [
    'a bad ass mofo!',
    "the cat's pajamas!",
    "the bee's knees!",
    'too cool for school!',
    'the end-all be-all of bad-ass-ed-ness!',
    'fucking amazing!',
    'really swell!!'
]

MOVIES = [
    'Amadeus',
    'Jaws',
    'Interstellar',
    'The Dark Knight',
    'The Holdeovers',
    'Star Wars',
    'Rogue One'
]

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/old-home-page')
def redirect_to_home():
    return redirect('/')

@app.route('/hello')
def say_hello():
    """Shows Hello Page"""
    return render_template('hello.html')

@app.route('/lucky')
def show_lucky_num():
    num = randint(1, 10)
    return render_template('lucky.html', lucky_num=num, msg='You are SO lucky, dog!')

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')

@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)

@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)

@app.route('/movies')
def show_all_movies():
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=['POST'])
def add_movie():
    title = request.form['title']
    # add to pretend DB
    MOVIES.append(title)
    return redirect('/movies')