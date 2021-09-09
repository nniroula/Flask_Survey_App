from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "OH NO KEY"
debug = DebugToolbarExtension(app)

# @app.route("/hello")
# def test_flask_working():
#     return "Flask is working"

# step 2
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


# @app.route("/questions/0", methods = ["POST"])
@app.route("/questions/0")
def first_question():
    return render_template("question_0.html", first_question = questions[0])

# fucntion that keeps user input and appends to response list
@app.route("/answer", methods = ["POST"])
def get_input():
    # ans = request.form.get('Ans')

    ans = request.form['Ans']
    responses.append(ans)
   
   
    return responses
print(responses)

@app.route("/answer", methods = ["POST"])
def answer():
    # raise
    request.form['value in the name attribute in the form']
    ans = request.form['Ans']
    ans = request.form.get('Ans')
    responses.append(ans)

    print(responses)
    # get_input()
    return redirect("question_1.html", second_question = questions[1])  # or redirect ot html file for question 2

print(responses)
"""

@app.route("/questions/1")
def second_question():
    return render_template("question_1.html", second_question = questions[1])

@app.route("/questions/2")
def third_question():
    return render_template("question_2.html", third_question = questions[2])

@app.route("/questions/3")
def fourth_question():
    return render_template("question_3.html", fourth_question = questions[3])

"""






# step 3
# @app.route("/questions/<int:qnum>")
# def handle_questions(question_number):
#     #request.form["value in name attribute"]
#     template = "Not a valid question number."
#     if question_number == 0:
#         template = render_template("question_0.html", first_question = questions[0])
#     elif question_number == 1:
#         template = render_template("question_1.html", second_question = questions[1])
#     elif question_number == 2:
#         template = render_template("question_2.html", third_question = questions[2])
#     elif question_number == 3:
#          template = render_template("question_3.html", fourth_question = questions[3])
#     else:
#         return template
#     return template
