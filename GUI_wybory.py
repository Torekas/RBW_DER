import heapq
import math
import tkinter as tk
from collections import Counter
from itertools import chain
from tkinter import filedialog, messagebox, ttk

import pandas as pd


def metoda_dhondta(df, okrąg_wyborczy):
    partie = ["PiS", "KO", "Trzecia Droga", "Lewica", "Konfederacja"]
    filtered_row = df[df["Nr okręgu"] == okrąg_wyborczy]
    liczba_glosow = pd.DataFrame(filtered_row.iloc[0, 3:])
    liczba_mandatow = pd.DataFrame(filtered_row)["Liczba mandatów"].tolist()

    party_votes = liczba_glosow.iloc[:, 0].tolist()
    result_lists = []

    for vote_count in party_votes:
        temp_list = [vote_count / i for i in range(1, 21)]
        result_lists.append(temp_list)

    flat_list = list(chain.from_iterable(result_lists))

    top_values = heapq.nlargest(liczba_mandatow[0], flat_list)

    lists_containing_top_values = []

    for value in top_values:
        for i, sublist in enumerate(result_lists):
            if value in sublist:
                lists_containing_top_values.append((i, value))
                break

    party_mapping = {i: partie[i] for i in range(len(partie))}

    party_names_containing_top_values = [
        (party_mapping[i], value) for i, value in lists_containing_top_values
    ]

    party_names_containing_top_values = [
        (party_mapping[i], value) for i, value in lists_containing_top_values
    ]

    party_names = [party for party, _ in party_names_containing_top_values]
    party_counts = Counter(party_names)

    return party_counts


def metoda_sainte_lague(df, okrąg_wyborczy):
    partie = ["PiS", "KO", "Trzecia Droga", "Lewica", "Konfederacja"]
    filtered_row = df[df["Nr okręgu"] == okrąg_wyborczy]
    liczba_glosow = pd.DataFrame(filtered_row.iloc[0, 3:])
    liczba_mandatow = pd.DataFrame(filtered_row)["Liczba mandatów"].tolist()

    party_votes = liczba_glosow.iloc[:, 0].tolist()
    result_lists = []

    for vote_count in party_votes:
        temp_list = [vote_count / i for i in range(1, 21, 2)]
        result_lists.append(temp_list)

    flat_list = list(chain.from_iterable(result_lists))

    top_values = heapq.nlargest(liczba_mandatow[0], flat_list)

    lists_containing_top_values = []

    for value in top_values:
        for i, sublist in enumerate(result_lists):
            if value in sublist:
                lists_containing_top_values.append((i, value))
                break

    party_mapping = {i: partie[i] for i in range(len(partie))}

    party_names_containing_top_values = [
        (party_mapping[i], value) for i, value in lists_containing_top_values
    ]

    party_names_containing_top_values = [
        (party_mapping[i], value) for i, value in lists_containing_top_values
    ]

    party_names = [party for party, _ in party_names_containing_top_values]
    party_counts = Counter(party_names)

    return party_counts


def metoda_dunska(df, okrąg_wyborczy):
    partie = ["PiS", "KO", "Trzecia Droga", "Lewica", "Konfederacja"]
    filtered_row = df[df["Nr okręgu"] == okrąg_wyborczy]
    liczba_glosow = pd.DataFrame(filtered_row.iloc[0, 3:])
    liczba_mandatow = pd.DataFrame(filtered_row)["Liczba mandatów"].tolist()

    party_votes = liczba_glosow.iloc[:, 0].tolist()
    result_lists = []

    for vote_count in party_votes:
        temp_list = [vote_count / i for i in range(1, 21, 3)]
        result_lists.append(temp_list)

    flat_list = list(chain.from_iterable(result_lists))

    top_values = heapq.nlargest(liczba_mandatow[0], flat_list)

    lists_containing_top_values = []

    for value in top_values:
        for i, sublist in enumerate(result_lists):
            if value in sublist:
                lists_containing_top_values.append((i, value))
                break

    party_mapping = {i: partie[i] for i in range(len(partie))}

    party_names_containing_top_values = [
        (party_mapping[i], value) for i, value in lists_containing_top_values
    ]

    party_names_containing_top_values = [
        (party_mapping[i], value) for i, value in lists_containing_top_values
    ]

    party_names = [party for party, _ in party_names_containing_top_values]
    party_counts = Counter(party_names)

    return party_counts


def huntington_hill(df, okrąg_wyborczy):
    partie = ["PiS", "KO", "Trzecia Droga", "Lewica", "Konfederacja"]
    filtered_row = df[df["Nr okręgu"] == okrąg_wyborczy]
    liczba_glosow = pd.DataFrame(filtered_row.iloc[0, 3:])
    liczba_mandatow = [
        mandaty - 5
        for mandaty in pd.DataFrame(filtered_row)["Liczba mandatów"].tolist()
    ]

    party_votes = liczba_glosow.iloc[:, 0].tolist()
    result_lists = []

    for vote_count in party_votes:
        temp_list = [vote_count / (math.sqrt((i) * (i + 1))) for i in range(1, 21)]
        result_lists.append(temp_list)

    flat_list = list(chain.from_iterable(result_lists))

    top_values = heapq.nlargest(liczba_mandatow[0], flat_list)

    lists_containing_top_values = []

    for value in top_values:
        for i, sublist in enumerate(result_lists):
            if value in sublist:
                lists_containing_top_values.append((i, value))
                break

    party_mapping = {i: partie[i] for i in range(len(partie))}

    party_names_containing_top_values = [
        (party_mapping[i], value) for i, value in lists_containing_top_values
    ]

    party_names = [party for party, _ in party_names_containing_top_values]
    party_counts = Counter(party_names)

    for party in partie:
        party_counts[party] += 1

    return party_counts


def load_data_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("XLSX files", "*.xlsx")]
    )

    if file_path:
        try:
            if file_path.endswith(".csv"):
                loaded_df = pd.read_csv(file_path)  # Load the CSV file
            elif file_path.endswith(".xlsx"):
                loaded_df = pd.read_excel(file_path)  # Load the XLSX file
            else:
                messagebox.showerror("Error", "Zly format pliku")
                return

            return loaded_df

        except Exception as e:
            messagebox.showerror("Error", f"Bląd wczytywania pliku: {str(e)}")

    return None


def process_data(method, data):
    if data is not None:
        try:
            nr_okręgu = data["Nr okręgu"].tolist()

            result_data = []

            for element in nr_okręgu:
                party_counts = method(data, element)
                result_data.append(party_counts)

            party_names = data.columns[3:].tolist()

            dict_list = []

            for party_counts in result_data:
                party_counts_dict = {}
                for party in party_names:
                    if party in party_counts:
                        party_counts_dict[party] = party_counts[party]
                    else:
                        party_counts_dict[party] = 0
                dict_list.append(party_counts_dict)

            output = pd.DataFrame(dict_list)

            output.insert(0, "nr_okręgu", nr_okręgu)

            output = output.astype(float)
            output = output.fillna(0)

            sums = output.iloc[:, 1:].sum()

            result_window = tk.Toplevel(root)
            result_window.title("Result")

            result_text = tk.Text(result_window)
            result_text.pack()

            result_text.insert(tk.END, f"Suma mandatów partii:\n{sums}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


root = tk.Tk()
root.title("Analiza wyborów")
root.geometry("400x120")

load_data_frame = tk.Frame(root)
load_data_frame.pack(side=tk.TOP, padx=10, pady=10)

load_data_button = tk.Button(
    load_data_frame, text="Wczytaj plik z danymi", command=lambda: load_data()
)
load_data_button.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, padx=10, pady=10)

method_dhondta_button = tk.Button(
    button_frame,
    text="Metoda Dhondta",
    command=lambda: process_data(metoda_dhondta, data),
)
method_1_button = tk.Button(
    button_frame,
    text="Metoda Sainte Lague",
    command=lambda: process_data(metoda_sainte_lague, data),
)
method_2_button = tk.Button(
    button_frame,
    text="Metoda dunska",
    command=lambda: process_data(metoda_dunska, data),
)
method_huntington_hill_button = tk.Button(
    button_frame,
    text="Metoda Huntingtona-Hilla",
    command=lambda: process_data(huntington_hill, data),
)

method_dhondta_button.pack(side=tk.LEFT, padx=5)
method_1_button.pack(side=tk.LEFT, padx=5)
method_2_button.pack(side=tk.LEFT, padx=5)
method_huntington_hill_button.pack(side=tk.LEFT, padx=5)

data = None


def load_data():
    global data
    data = load_data_file()


root.mainloop()
