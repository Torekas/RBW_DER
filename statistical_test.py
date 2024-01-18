import os
import json
from scipy.stats import ttest_rel
import numpy as np

# correct answers:
# TODO: fill with correct answers
wind = {
    "q1_wind": "C",
    "q2_wind": "C",
    "q3_wind": "A",
    "q4_wind": "D",
    "q5_wind": "B",
    "q6_wind": "C"
}

# TODO: fill with correct answers
hydro = {
    "q1_hydro": "A",
    "q2_hydro": "C",
    "q3_hydro": "B",
    "q4_hydro": "A",
    "q5_hydro": "B",
    "q6_hydro": "A"
}

# TODO: fill with correct answers
solar = {
    "q1_solar": "A",
    "q2_solar": "A",
    "q3_solar": "A",
    "q4_solar": "A",
    "q5_solar": "A",
    "q6_solar": "B"
}

# TODO: fill with correct answers
der = {
    "q1_der": "A",
    "q2_der": "A",
    "q3_der": "A",
    "q4_der": "B",
    "q5_der": "A",
    "q6_der": "A"
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
    return score / total

def verify_answers_list(answers_list, keys):
    results = []
    for answers in answers_list:
        result = verify_answers(answers, keys)
        results.append(result)
    return results

def main():
    # List of dirs with answers before using educational platform
    primary_answers_dirs = ['path1.1']

    # List of dirs with answers after using educational platform
    final_answers_dirs = ['path1.2']
    # !!! Order of the elements from primary_answers_dirs must match final_answers_dirs !!!
    # !!! Number of elements from primary_answers_dirs must match final_answers_dirs !!!

    # lists of loaded JSONs
    primary_answers_wind = []
    final_answers_wind = []

    primary_answers_der = []
    final_answers_der = []

    primary_answers_solar = []
    final_answers_solar = []

    primary_answers_hydro = []
    final_answers_hydro = []

    # load JSONs
    for primary_dir in primary_answers_dirs:
        read_file_to_json(primary_answers_wind, os.path.join("answers", primary_dir, "answers_wind.json"))
        read_file_to_json(primary_answers_der, os.path.join("answers", primary_dir, "answers_der.json"))
        read_file_to_json(primary_answers_solar, os.path.join("answers", primary_dir, "answers_solar.json"))
        read_file_to_json(primary_answers_hydro, os.path.join("answers", primary_dir, "answers_hydro.json"))
    for final_dir in final_answers_dirs:
        read_file_to_json(final_answers_wind, os.path.join("answers", final_dir, "answers_wind.json"))
        read_file_to_json(final_answers_der, os.path.join("answers", final_dir, "answers_der.json"))
        read_file_to_json(final_answers_solar, os.path.join("answers", final_dir, "answers_solar.json"))
        read_file_to_json(final_answers_hydro, os.path.join("answers", final_dir, "answers_hydro.json"))

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
    t_statistic_wind, p_value_wind = ttest_rel(np.array(primary_results_wind), np.array(final_results_wind))
    t_statistic_der, p_value_der = ttest_rel(np.array(primary_results_der), np.array(final_results_der))
    t_statistic_solar, p_value_solar = ttest_rel(np.array(primary_results_solar), np.array(final_results_solar))
    t_statistic_hydro, p_value_hydro = ttest_rel(np.array(primary_results_hydro), np.array(final_results_hydro))
    t_statistic_total, p_value_total = ttest_rel(np.array(primary_results_total), np.array(final_results_total))

    # print test results
    print(f'{"category:":<10} | {"t_statistic":<15} | {"p_value":<10}')
    print(f'{"wind:":<10} | {t_statistic_wind:<15.4f} | {p_value_wind:<10.4f}')
    print(f'{"der:":<10} | {t_statistic_der:<15.4f} | {p_value_der:<10.4f}')
    print(f'{"solar:":<10} | {t_statistic_solar:<15.4f} | {p_value_solar:<10.4f}')
    print(f'{"hydro:":<10} | {t_statistic_hydro:<15.4f} | {p_value_hydro:<10.4f}')
    print(f'{"total:":<10} | {t_statistic_total:<15.4f} | {p_value_total:<10.4f}')

if __name__=="__main__":
    main()