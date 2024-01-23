from datetime import datetime
import json
import os
from flask import Flask, render_template, request, redirect, url_for

def get_formatted_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime("%d-%m-%Y_%H-%M-%S")
    return formatted_datetime

app = Flask(__name__)

@app.route('/')
def home():
    images = ['example_image.png', 'example_image2.png', 'wallpaper.gif']
    return render_template('starting.html')

@app.route('/index')
def index():
    # Add any dynamic content you want to pass to the template
    return render_template('index.html')


@app.route('/submit_quiz_wind', methods=['POST'])
def submit_quiz_wind():
    # Extract answers from the form
    answers = {
        'q1_wind': request.form.get('q1'),
        'q2_wind': request.form.get('q2'),
        'q3_wind': request.form.get('q3'),
        'q4_wind': request.form.get('q4'),
        'q5_wind': request.form.get('q5'),
        'q6_wind': request.form.get('q6')
    }

    answers_json = json.dumps(answers, indent=4)

    file_path = os.path.join(answers_dir, 'answers_wind.json')

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('home'))

@app.route('/submit_quiz_der', methods=['POST'])
def submit_quiz_der():
    # Extract answers from the form
    answers = {
        'q1_der': request.form.get('q1'),
        'q2_der': request.form.get('q2'),
        'q3_der': request.form.get('q3'),
        'q4_der': request.form.get('q4'),
        'q5_der': request.form.get('q5'),
        'q6_der': request.form.get('q6')
    }

    answers_json = json.dumps(answers, indent=4)

    # Define the file path
    file_path = os.path.join(answers_dir, 'answers_der.json')

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('index'))

@app.route('/submit_quiz_solar', methods=['POST'])
def submit_quiz_solar():
    # Extract answers from the form
    answers = {
        'q1_solar': request.form.get('q1'),
        'q2_solar': request.form.get('q2'),
        'q3_solar': request.form.get('q3'),
        'q4_solar': request.form.get('q4'),
        'q5_solar': request.form.get('q5'),
        'q6_solar': request.form.get('q6')
    }

    answers_json = json.dumps(answers, indent=4)

    # Define the file path
    file_path = os.path.join(answers_dir, 'answers_solar.json')

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('index'))

@app.route('/submit_quiz_hydro', methods=['POST'])
def submit_quiz_hydro():
    # Extract answers from the form
    answers = {
        'q1_hydro': request.form.get('q1'),
        'q2_hydro': request.form.get('q2'),
        'q3_hydro': request.form.get('q3'),
        'q4_hydro': request.form.get('q4'),
        'q5_hydro': request.form.get('q5'),
        'q6_hydro': request.form.get('q6')
    }
    answers_json = json.dumps(answers, indent=4)

    # Define the file path

    file_path = os.path.join(answers_dir, 'answers.der')

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('index'))
@app.route('/submit_quiz_wind_prim', methods=['POST'])
def submit_quiz_wind_prim():
    # Extract answers from the form
    answers = {
        'q1_wind': request.form.get('q1'),
        'q2_wind': request.form.get('q2'),
        'q3_wind': request.form.get('q3'),
        'q4_wind': request.form.get('q4'),
        'q5_wind': request.form.get('q5'),
        'q6_wind': request.form.get('q6')
    }

    answers_json = json.dumps(answers, indent=4)

    file_path = os.path.join(answers_dir, 'answers_wind_prim.json')

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('home'))

@app.route('/submit_quiz_der_prim', methods=['POST'])
def submit_quiz_der_prim():
    # Extract answers from the form
    answers = {
        'q1_der': request.form.get('q1'),
        'q2_der': request.form.get('q2'),
        'q3_der': request.form.get('q3'),
        'q4_der': request.form.get('q4'),
        'q5_der': request.form.get('q5'),
        'q6_der': request.form.get('q6')
    }

    answers_json = json.dumps(answers, indent=4)

    # Define the file path
    file_path = os.path.join(answers_dir, 'answers_der_prim.json')

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('home'))

@app.route('/submit_quiz_solar_prim', methods=['POST'])
def submit_quiz_solar_prim():
    # Extract answers from the form
    answers = {
        'q1_solar': request.form.get('q1'),
        'q2_solar': request.form.get('q2'),
        'q3_solar': request.form.get('q3'),
        'q4_solar': request.form.get('q4'),
        'q5_solar': request.form.get('q5'),
        'q6_solar': request.form.get('q6')
    }

    answers_json = json.dumps(answers, indent=4)

    # Define the file path
    file_path = os.path.join(answers_dir, 'answers_solar_prim.json')

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('home'))

@app.route('/submit_quiz_hydro_prim', methods=['POST'])
def submit_quiz_hydro_prim():
    # Extract answers from the form
    answers = {
        'q1_hydro': request.form.get('q1'),
        'q2_hydro': request.form.get('q2'),
        'q3_hydro': request.form.get('q3'),
        'q4_hydro': request.form.get('q4'),
        'q5_hydro': request.form.get('q5'),
        'q6_hydro': request.form.get('q6')
    }
    answers_json = json.dumps(answers, indent=4)

    # Define the file path

    file_path = os.path.join(answers_dir, 'answers_hydro_prim.json')

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('home'))


@app.route('/redirect')
def redirect_to_another_site():
    return redirect("https://dzalapino.github.io/DER_Simulation_Build/?fbclid=IwAR1T2MrVAHWCkbZdT6o03T9N_XzuZnayGECUpJJaFh5z5n37Ob2ZK-AxbW8")

if __name__ == '__main__':
    global answers_dir
    dt = get_formatted_datetime()
    answers_dir = os.path.join('answers', dt)
    os.makedirs(answers_dir)
    app.run(host='0.0.0.0', port='8080', debug=True)
