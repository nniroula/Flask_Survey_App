from flask import Flask

app = Flask(__name__)

@app.route("/")
def test_flask_working():
    return "Flask is working"