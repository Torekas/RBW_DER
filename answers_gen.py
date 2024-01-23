import os
import json
import random
from datetime import datetime

# Correct answers for each quiz type
correct_answers = {
    "wind": {"q1_wind": "C", "q2_wind": "C", "q3_wind": "D", "q4_wind": "B", "q5_wind": "B", "q6_wind": "C"},
    "hydro": {"q1_hydro": "C", "q2_hydro": "C", "q3_hydro": "A", "q4_hydro": "D", "q5_hydro": "D", "q6_hydro": "B"},
    "solar": {"q1_solar": "B", "q2_solar": "C", "q3_solar": "C", "q4_solar": "B", "q5_solar": "B", "q6_solar": "B"},
    "der": {"q1_der": "B", "q2_der": "C", "q3_der": "C", "q4_der": "C", "q5_der": "B", "q6_der": "D"}
}

def generate_random_datetime():
    day = random.randint(18, 24)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime(2024, 1, day, hour, minute, second)

def generate_answers(quiz_type, is_primary):
    possible_answers = ["A", "B", "C", "D"]
    answers = {}
    for i in range(1, 7):
        key = f"q{i}_{quiz_type}"
        correct = correct_answers[quiz_type][key]

        if is_primary:
            # Higher chance to pick the correct answer for primary
            answers[key] = correct if random.random() < 0.6 else random.choice(possible_answers)
        else:
            # Even higher chance for final answers
            answers[key] = correct if random.random() < 0.7 else random.choice(possible_answers)

    return answers

def create_folders_and_files():
    base_path = r'C:\Users\janmi\PycharmProjects\Studies\rbw_der\answers'  # Change this to your desired path
    for _ in range(100):
        folder_name = generate_random_datetime().strftime("%d-%m-%Y_%H-%M-%S")
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for quiz_type in correct_answers.keys():
            # Generate and write regular answers
            answers = generate_answers(quiz_type, False)
            with open(os.path.join(folder_path, f'answers_{quiz_type}.json'), 'w') as file:
                json.dump(answers, file, indent=4)

            # Generate and write primary answers
            answers_prim = generate_answers(quiz_type, True)
            with open(os.path.join(folder_path, f'answers_{quiz_type}_prim.json'), 'w') as file:
                json.dump(answers_prim, file, indent=4)

create_folders_and_files()
