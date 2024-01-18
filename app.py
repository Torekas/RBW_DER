from flask import Flask, render_template, request, redirect, url_for
import json
import os
app = Flask(__name__)

@app.route('/')
def home():
    images = ['example_image.png', 'example_image2.png', 'wallpaper.gif']
    return render_template('index.html', images=images)

@app.route('/turtle')
def turtle_page():
    # Add any dynamic content you want to pass to the template
    return render_template('turtle_page.html')


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


    file_path = r'C:\Users\janmi\PycharmProjects\Studies\rbw_der\answers\answers_wind.json'

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
    file_path = file_path = r'C:\Users\janmi\PycharmProjects\Studies\rbw_der\answers\answers_der.json'

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('home'))

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
    file_path = r'C:\Users\janmi\PycharmProjects\Studies\rbw_der\answers\answers_solar.json'

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('home'))

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
    file_path = r'C:\Users\janmi\PycharmProjects\Studies\rbw_der\answers\answers_hydro.json'

    # Write answers to a JSON file
    with open(file_path, 'w') as file:
        file.write(answers_json)

    return redirect(url_for('home'))

@app.route('/redirect')
def redirect_to_another_site():
    return redirect("https://dzalapino.github.io/DER_Simulation_Build/?fbclid=IwAR1T2MrVAHWCkbZdT6o03T9N_XzuZnayGECUpJJaFh5z5n37Ob2ZK-AxbW8")

if __name__ == '__main__':
    app.run(debug=True)
