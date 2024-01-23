import os
import json
from scipy.stats import ttest_rel
import numpy as np
from typing import List
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

# correct answers:
wind = {
    "q1_wind": "C",
    "q2_wind": "C",
    "q3_wind": "D",
    "q4_wind": "B",
    "q5_wind": "B",
    "q6_wind": "C"
}

hydro = {
    "q1_hydro": "C",
    "q2_hydro": "C",
    "q3_hydro": "A",
    "q4_hydro": "D",
    "q5_hydro": "D",
    "q6_hydro": "B"
}

solar = {
    "q1_solar": "B",
    "q2_solar": "C",
    "q3_solar": "C",
    "q4_solar": "B",
    "q5_solar": "B",
    "q6_solar": "B"
}

der = {
    "q1_der": "B",
    "q2_der": "C",
    "q3_der": "C",
    "q4_der": "C",
    "q5_der": "B",
    "q6_der": "D"
}

def read_file_to_json(answers, path):
    file = open(path)
    data = json.load(file)
    answers.append(data)
    file.close()

"""
Returns percentage of correct answers.
"""
def verify_answers(answers, keys):
    total = len(keys)
    score = 0
    for question in keys:
        if answers[question] == keys[question]:
            score += 1
    return score / total * 100

def verify_answers_list(answers_list, keys):
    results = []
    for answers in answers_list:
        result = verify_answers(answers, keys)
        results.append(result)
    return results


def Filter(string: list, substr: list) -> list:
    """Filter strings based on the presence of substrings.

    :param  strings: List of strings to filter.
    :type strings: List
    :param substr: List of substrings to check for.
    :type substr: List
    :return: List of filtered strings.
    :rtype: List
    """
    return [str for str in string if any(sub in str for sub in substr)]

def main():
    base_dir = r'C:\Users\janmi\PycharmProjects\Studies\rbw_der\answers'

    # Lists for storing JSON data
    primary_answers_wind = []
    final_answers_wind = []
    primary_answers_der = []
    final_answers_der = []
    primary_answers_solar = []
    final_answers_solar = []
    primary_answers_hydro = []
    final_answers_hydro = []

    # Function to load data from a JSON file
    def load_json_data(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    # Loop through each folder and load the JSON data
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)

        # Check if the path is a directory
        if os.path.isdir(folder_path):
            # Load primary and final JSONs for each quiz type
            for quiz_type in ['wind', 'der', 'solar', 'hydro']:
                primary_file_path = os.path.join(folder_path, f'answers_{quiz_type}_prim.json')
                final_file_path = os.path.join(folder_path, f'answers_{quiz_type}.json')

                if os.path.exists(primary_file_path) and os.path.exists(final_file_path):
                    # Load primary answers
                    primary_data = load_json_data(primary_file_path)
                    eval(f'primary_answers_{quiz_type}').append(primary_data)

                    # Load final answers
                    final_data = load_json_data(final_file_path)
                    eval(f'final_answers_{quiz_type}').append(final_data)

        # print(folder_path)

    # primary_results
    primary_results_wind = verify_answers_list(primary_answers_wind, wind)
    final_results_wind = verify_answers_list(final_answers_wind, wind)

    primary_results_der = verify_answers_list(primary_answers_der, der)
    final_results_der = verify_answers_list(final_answers_der, der)

    primary_results_solar = verify_answers_list(primary_answers_solar, solar)
    final_results_solar = verify_answers_list(final_answers_solar, solar)

    primary_results_hydro = verify_answers_list(primary_answers_hydro, hydro)
    final_results_hydro = verify_answers_list(final_answers_hydro, hydro)

    primary_results_all = primary_results_wind + primary_results_der + primary_results_solar + primary_results_hydro
    final_results_all = final_results_wind + final_results_der + final_results_solar + final_results_hydro

    # perform t-tests
    t_test_results = {
        'wind': ttest_rel(np.array(primary_results_wind), np.array(final_results_wind)),
        'der': ttest_rel(np.array(primary_results_der), np.array(final_results_der)),
        'solar': ttest_rel(np.array(primary_results_solar), np.array(final_results_solar)),
        'hydro': ttest_rel(np.array(primary_results_hydro), np.array(final_results_hydro)),
        'total': ttest_rel(np.array(primary_results_all), np.array(final_results_all))
    }

    # Tkinter Application Setup
    window = tk.Tk()
    window.title("Quiz Results Analysis")
    window.geometry("780x600")  # Adjusting window size

    # Custom Font for Hypotheses
    customFont = Font(family="Helvetica", size=12, weight="bold")

    # Custom Font for Titles and Hypotheses
    titleFont = Font(family="Helvetica", size=14, weight="bold")
    hypothesisFont = Font(family="Helvetica", size=12)

    def create_hypothesis_labels():
        # Two-Tailed Hypotheses Title
        two_tailed_title = tk.Label(window, text="Two-Tailed Test Hypotheses", font=titleFont)
        two_tailed_title.grid(row=2, column=0, columnspan=2, sticky='ew', padx=0, pady=5)

        # Two-Tailed Hypotheses Labels
        h0_label_two_tailed = tk.Label(window, text="H0: µ1 = µ2 (Means are equal)", font=hypothesisFont)
        h0_label_two_tailed.grid(row=3, column=0, columnspan=2, sticky='ew', padx=0, pady=0)

        ha_label_two_tailed = tk.Label(window, text="HA: µ1 ≠ µ2 (Means are not equal)", font=hypothesisFont)
        ha_label_two_tailed.grid(row=4, column=0, columnspan=2, sticky='ew', padx=0, pady=0)

        # One-Tailed Hypotheses Title
        one_tailed_title = tk.Label(window, text="One-Tailed Test Hypotheses", font=titleFont)
        one_tailed_title.grid(row=6, column=0, columnspan=2, sticky='ew', padx=0, pady=5)

        # One-Tailed Hypotheses Labels
        h0_label_one_tailed = tk.Label(window, text="H0: µ1 = µ2 (Primary mean is equal to Final mean)",
                                       font=hypothesisFont)
        h0_label_one_tailed.grid(row=7, column=0, columnspan=2, sticky='ew', padx=0, pady=0)

        ha_label_one_tailed = tk.Label(window, text="HA: µ1 < µ2 (Primary mean is less than Final mean)",
                                       font=hypothesisFont)
        ha_label_one_tailed.grid(row=8, column=0, columnspan=2, sticky='ew', padx=0, pady=0)

    def update_results():
        # Clear existing data in the table
        for i in tree.get_children():
            tree.delete(i)

        # Add rows to the table from the t_test_results dictionary
        for category, (t_statistic, p_value) in t_test_results.items():
            # Two-tailed test decision
            decision_two_tailed = "Reject H0" if p_value < .05 else "Fail to Reject H0"

            # One-tailed test decision (testing if µ1 < µ2)
            one_tailed_p_value = p_value / 2
            decision_one_tailed = "Reject H0" if one_tailed_p_value < .025 and t_statistic < 0 else "Fail to Reject H0"

            tree.insert('', tk.END, values=(
            category, f'{t_statistic:.4f}', f'{p_value:.6f}', decision_two_tailed, f'{one_tailed_p_value:.6f}',
            decision_one_tailed))

    # Update columns for the Table to include one-tailed test
    columns = (
    'category', 't_statistic', 'p_value_two_tailed', 'decision_two_tailed', 'p_value_one_tailed', 'decision_one_tailed')

    # Creating a Treeview Widget
    tree = ttk.Treeview(window, columns=columns, show='headings')
    tree.heading('category', text='Category')
    tree.heading('t_statistic', text='T-Statistic')
    tree.heading('p_value_two_tailed', text='P-Value (Two-tailed)')
    tree.heading('decision_two_tailed', text='Decision (Two-tailed)')
    tree.heading('p_value_one_tailed', text='P-Value (One-tailed)')
    tree.heading('decision_one_tailed', text='Decision (One-tailed)')
    tree.column('category', width=80)
    tree.column('t_statistic', width=80)
    tree.column('p_value_two_tailed', width=150)
    tree.column('decision_two_tailed', width=150)
    tree.column('p_value_one_tailed', width=150)
    tree.column('decision_one_tailed', width=150)
    tree.grid(row=5, column=0, padx=10, pady=50)
    create_hypothesis_labels()

    # Button to trigger results update
    update_button = tk.Button(window, text="Show Results", command=update_results)
    update_button.grid(row=9, column=0, pady=8)

    window.mainloop()

if __name__=="__main__":
    main()