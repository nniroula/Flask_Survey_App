from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "OH NO KEY"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# @app.route("/hello")
# def test_flask_working():
#     return "Flask is working"

responses = []

title = satisfaction_survey.title
instructions = satisfaction_survey.instructions

# question_1 = satisfaction_survey.questions[0].question

questions = [satisfaction_survey.questions[0].question,
            satisfaction_survey.questions[1].question,
            satisfaction_survey.questions[2].question,
            satisfaction_survey.questions[3].question
            ]

@app.route("/")
def show_survey_start_page():
    return render_template("starter_page.html", survey_title = title, survey_instructions = instructions)

#@app.route("/questions/0", methods=["POST"])
@app.route("/firstquestion", methods=["POST"])
def first_question():
        # return render_template("question_0.html", first_question = questions[0])
        # better to send to a route and that route should be looping for different question numbers
    return redirect("/questions/0") #,

# Now define quesiton/0 route
# @app.route("/questions/<int:qnumber>", methods = ["POST"])
@app.route("/questions/<int:qnumber>")
def questions(qnumber):
    # get instance of the survery 
    question = satisfaction_survey.questions[qnumber]
    # question = questions[qnumber]  # questions is list generated above
    return render_template("questions.html", question_number = qnumber, any_question = question)
    
# fucntion that keeps user input and appends to response list
@app.route("/answer", methods=["POST"])
def get_input():
    # ans = request.form.get('Ans')
    ans = request.form['form-data']
    responses.append(ans)
# get the length of the list and then return to the next question

    if len(responses) == len(satisfaction_survey.questions):
        return render_template("thanks.html")
    else:
# return redirect("/questions/<int:qnumber>") # return redirect(f"/questions/{len(responses)}") # first question is index 0 and length of responses list is 1. len(responses) should take to the next question.
        return redirect(f"/questions/{len(responses)}")




