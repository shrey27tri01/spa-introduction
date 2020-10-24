# set up the flask application
from flask import Flask, render_template

app = Flask(__name__)

votes = 0

# default route, gets rendered when user goes to http://127.0.0.1:5000/ in a browser
@app.route("/")
def index():
    return render_template("index.html", votes=votes)

# POST request to this endpoint(route) results in the number of votes after upvoting
@app.route("/up", methods=["POST"])
def upvote():
    global votes
    votes = votes + 1
    return str(votes)

# POST request to this endpoint(route) results in the number of votes after downvoting
@app.route("/down", methods=["POST"])
def downvote():
    global votes
    if votes >= 1:
        votes = votes - 1
    return str(votes)
