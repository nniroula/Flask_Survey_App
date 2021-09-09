from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "OH NO KEY"
debug = DebugToolbarExtension(app)

# @app.route("/hello")
# def test_flask_working():
#     return "Flask is working"

# step 2
response = []

title = satisfaction_survey.title
instructions = satisfaction_survey.instructions
@app.route("/")
def show_survey_start_page():
    return render_template("starter_page.html", survey_title = title, survey_instructions = instructions)


