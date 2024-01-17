from flask import Flask, render_template, request, jsonify
from agent import get_code_problem, get_code_big_o, get_code_feedback, get_hint
from tts import text_to_speech, text_to_speech_problem

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/get_problem', methods=['POST'])
def get_problem():
    """ gets a technical problem from Agent (aka OpenAI), 
    tts its and returns the text and audio file 
    to ajax request """
  
    difficulty = request.form.get('difficulty')
    code_problem = get_code_problem(difficulty)
    text_to_speech_problem(code_problem)
    problem_data = {
      "code_problem": code_problem,
      "audio_file": "static/audio/problem.mp3"
    }
    return jsonify(problem_data)

@app.route('/get_hint', methods=['POST'])
def gets_hint():
    """ receives the technical problem and solution 
    and ask the Agent (aka OpenAI) to provide a hint, 
    the text is then tts and returns the text and audio file 
    to ajax request """
  
    problem = request.form.get('problem')
    user_code_problem = request.form.get('userSolution')

    feedback = get_hint(problem, user_code_problem)
    text_to_speech(feedback)

    data = {
      "feedback": feedback,
      "audio_file": "static/audio/feedback.mp3"
    }
    return jsonify(data)

@app.route('/get_feedback', methods=['POST'])
def gets_feedback():
    """ receives the technical problem and solution 
    and ask the Agent (aka OpenAI) to provide feedback, 
    the text is then tts and returns the text and audio file 
    to ajax request """
    problem = request.form.get('problem')
    user_code_problem = request.form.get('userSolution')

    feedback = get_code_feedback(problem, user_code_problem)

    text_to_speech(feedback)

    data = {
      "feedback": feedback,
      "audio_file": "static/audio/feedback.mp3"
    }
    return jsonify(data)

@app.route('/submit_big_o', methods=['POST'])
def submit_big_o():
    """ receives the user provided solution & Big O  
    and ask the Agent (aka OpenAI) to provide validate it, 
    the text is then tts and returns the text and audio file 
    to ajax request """
    user_code_problem = request.form.get('user_solution')
    big_o = request.form.get('bigOValue')
    print(user_code_problem)

    feedback = get_code_big_o(user_code_problem, big_o)

    text_to_speech(feedback)
  
    data = {
      "feedback": feedback,
      "audio_file": "static/audio/feedback.mp3"
    }
    return jsonify(data)


app.run(host='0.0.0.0', port=81)
