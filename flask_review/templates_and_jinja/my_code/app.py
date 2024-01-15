from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SupDog1'

debug = DebugToolbarExtension(app)

# -----------------------------------------------            ---------------------------------------------------------------
#                                                Jinja routes
# -----------------------------------------------            ---------------------------------------------------------------

COMPLIMENTS = [
    'a bad ass mofo!',
    "the cat's pajamas!",
    "the bee's knees!",
    'too cool for school!',
    'the end-all be-all of bad-ass-ed-ness!',
    'fucking amazing!',
    'really swell!!'
]

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



# -----------------------------------------------            ---------------------------------------------------------------
#                                                flask_intro routes
# -----------------------------------------------            ---------------------------------------------------------------

# @app.route('/')
# def home_page():
#     html = """
#     <html>
#         <body>
#             <h1>This is the home page, dog!</h1>
#             <p>Welcome to my simple app, dedicated to all the sup dogs out there!</p>
#             <a href='/hello'>Go to hello page</a>
#             <br>
#             <a href='/goodbye'>Go to goodbye page</a>
#             <br>
#             <a href='/'>Go to home page</a>
#             <br>
#             <a href='/add-comment'>Go back to comment page</a>
#         </body>
#     </html>
#     """
#     return html

# @app.route('/goodbye')
# def say_goodbye():
#     html = """
#     <html>
#         <body>
#             <h1>Later Dog!</h1>
#             <p>This is the goodbye page!</p>
#             <a href='/hello'>Go to hello page</a>
#             <br>
#             <a href='/goodbye'>Go to goodbye page</a>
#             <br>
#             <a href='/'>Go to home page</a>
#             <br>
#             <a href='/add-comment'>Go back to comment page</a>
#         </body>
#     </html>
#     """
#     return html

# @app.route('/search')
# def search():
#     term = request.args['term']
#     sort = request.args['sort']
#     return f'<h1>Search results for: {term}</h1> <p>Sorting by: {sort}</p>'
    
# @app.route('/add-comment')
# def add_comment_form():
#     return """
#     <h1>Add Comment, dog!</h1>
#     <form method="POST">
#         <input type='text' placeholder='username' name='username'/>
#         <input type='text' placeholder='comment' name='comment'/>
#         <button>Submit</button>
#     </form>
# """

# @app.route('/add-comment', methods=["POST"])
# def save_comment():
#     username = request.form['username']
#     comment = request.form["comment"]
#     return f"""
#     <h1>This comment was saved to the database, dog!</h1>
#     <ul>
#         <li>Username: {username}</li>
#         <li>Comment: {comment}</li>
#     </ul>
#         <a href='/hello'>Go to hello page</a>
#         <br>
#         <a href='/goodbye'>Go to goodbye page</a>
#         <br>
#         <a href='/'>Go to home page</a>
#         <br>
#         <a href='/add-comment'>Go back to comment page</a>
#     """
    
# @app.route('/r/<subreddit>')
# def show_subreddit(subreddit):
#     return f'<h1>Browsing the "{subreddit}" subreddit</h1>'

# @app.route('/r/<subreddit>/comments/<int:post_id>')
# def show_comments(subreddit, post_id):
#     return f'<h1>Viewing comments for post with id: {post_id} from the {subreddit} subreddit</h1>'
    

# POSTS = {
#     1: 'Sup dog!?',
#     2: "What's up, my dog?",
#     3: 'Sup?',
#     4: 'Dog!'
# }

# @app.route('/posts/<int:id>')
# def find_post(id):
#     post = POSTS.get(id, 'Post not found, dog!')
#     return f'<p>{post}</p>'