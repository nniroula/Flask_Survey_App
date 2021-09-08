from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "OH NO KEY"
debug = DebugToolbarExtension(app)

@app.route("/")
def test_flask_working():
    return "Flask is working"
