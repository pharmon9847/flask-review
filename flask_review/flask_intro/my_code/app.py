from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>This is the home page, dog!</h1>
            <p>Welcome to my simple app, dedicated to all the sup dogs out there!</p>
            <a href='/hello'>Go to hello page</a>
            <br>
            <a href='/goodbye'>Go to goodbye page</a>
            <br>
            <a href='/'>Go to home page</a>
            <br>
            <a href='/add-comment'>Go back to comment page</a>
        </body>
    </html>
    """
    return html

# using @app.route is a decorator
@app.route('/hello')
def say_hello():
    # return 'Sup Dog?!'
    html = """
    <html>
        <body>
            <h1>Sup Dog?!</h1>
            <p>This is the hello page!</p>
            <a href='/hello'>Go to hello page</a>
            <br>
            <a href='/goodbye'>Go to goodbye page</a>
            <br>
            <a href='/'>Go to home page</a>
            <br>
            <a href='/add-comment'>Go back to comment page</a>
        </body>
    </html>
    """
    return html

@app.route('/goodbye')
def say_goodbye():
    # return 'Later Dog!'
    html = """
    <html>
        <body>
            <h1>Later Dog!</h1>
            <p>This is the goodbye page!</p>
            <a href='/hello'>Go to hello page</a>
            <br>
            <a href='/goodbye'>Go to goodbye page</a>
            <br>
            <a href='/'>Go to home page</a>
            <br>
            <a href='/add-comment'>Go back to comment page</a>
        </body>
    </html>
    """
    return html

@app.route('/search')
def search():
    # print(request.args)
    term = request.args['term']
    sort = request.args['sort']
    # return 'Search Page, dog!'
    return f'<h1>Search results for: {term}</h1> <p>Sorting by: {sort}</p>'
    
# @app.route('/post', methods=["POST"])
# def post_demo():
#     return 'You made a POST request, dog!'

@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment, dog!</h1>
    <form method="POST">
        <input type='text' placeholder='username' name='username'/>
        <input type='text' placeholder='comment' name='comment'/>
        <button>Submit</button>
    </form>
"""

@app.route('/add-comment', methods=["POST"])
def save_comment():
    username = request.form['username']
    comment = request.form["comment"]
    return f"""
    <h1>This comment was saved to the database, dog!</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
    </ul>
        <a href='/hello'>Go to hello page</a>
        <br>
        <a href='/goodbye'>Go to goodbye page</a>
        <br>
        <a href='/'>Go to home page</a>
        <br>
        <a href='/add-comment'>Go back to comment page</a>
    """
    
@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f'<h1>Browsing the "{subreddit}" subreddit</h1>'

@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f'<h1>Viewing comments for post with id: {post_id} from the {subreddit} subreddit</h1>'
    

POSTS = {
    1: 'Sup dog!?',
    2: "What's up, my dog?",
    3: 'Sup?',
    4: 'Dog!'
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, 'Post not found, dog!')
    return f'<p>{post}</p>'