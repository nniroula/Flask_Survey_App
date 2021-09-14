from flask import Flask, render_template, request, redirect, flash
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
# create a set to keep track of the question numbers
visited = set()

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
    visited.add(0)
    return redirect("/questions/0") #,
# Now define quesiton/0 route
# @app.route("/questions/<int:qnumber>", methods = ["POST"])
@app.route("/questions/<int:qnumber>")
def questions(qnumber):
    qnumber = qnumber
    # get instance of the survery 
    question = satisfaction_survey.questions[qnumber]

    if len(visited) == 0 and qnumber != 0:
        return redirect('/')

    if len(visited) != 0:
        if(qnumber > max(visited) and max(visited) + 1 != qnumber):
            #return redirect(f"/questions/{max(visited)}")
            flash("Not a valid route")
            return redirect(f"/questions/{max(visited) + 1}")
        if qnumber < max(visited):
            for q in range(qnumber, max(visited) + 1):
                #visited.remove(q)
                #return redirect(f"/quesions/{max(visited) + 1}") # if a user goes to the random question without answer one in the order
                flash("please visit in an orderly manner")
                return redirect(f"/quesions/{max(visited)}")
        visited.add(qnumber)

    return render_template("questions.html", question_number = qnumber, any_question = question) 

# fucntion that keeps user input and appends to response list
@app.route("/answer", methods=["POST"])
def get_input():
    # ans = request.form.get('Ans')
    ans = request.form['form-data']
    responses.append(ans)

    if max(visited) + 1 == len(satisfaction_survey.questions):
        # return render_template("thanks.html")
        return redirect("/thanks")
    else:
        return redirect(f"/questions/{max(visited) + 1}")

@app.route("/thanks")
def thanks_client():
    return render_template("thanks.html")