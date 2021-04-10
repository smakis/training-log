import os
import csv
from training_functions import training_folder
from datetime import date


def save_to_csv(day: str, iter_num: int, wk_nbr: int, excercise: str, weight: float, reps: int, comment: str):
    day = date.fromisoformat(day)

    training_log = f'training_iteration_{iter_num}_wk3_{excercise}_realized_reps.csv'
    folder_path = training_folder(iter_num)
    file_path = os.path.join(folder_path, training_log)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    try:
        with open(file_path, mode='a+', newline='') as file:
            fieldnames = ['Date', 'Training cycle wk',
                          'Exercise', 'Weight', 'Reps', 'Comment']
            log_writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Check if csv empty
            if file.tell() == 0:
                log_writer.writeheader()

            log_writer.writerow({'Date': day, 'Training cycle wk': wk_nbr, 'Exercise': excercise,
                                 'Weight': weight, 'Reps': reps, 'Comment': comment})
    except FileNotFoundError as err:
        print(err)
