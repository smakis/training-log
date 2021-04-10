import os


def calculate_ninety(max_weight: float):
    get_ninety = round(max_weight / 100 * 90, 2)
    return get_ninety


def calculate_max_weight(weight: float, reps: int):
    max_unrounded = weight * (36 / (37 - reps))
    max_weight = round(max_unrounded, 1)
    return max_weight


def calc_percentage(num: float, percentage: int):
    return round(num / 100 * percentage, 0)


def training_folder(iter_num: int):
    folder_name = f'iter_{iter_num}'
    root = os.getcwd()
    folder_path = os.path.join(root, folder_name)
    return folder_path


def create_training_iteration(iter_num: int, max_weight: float, training_list: list):
    training_file = f'training_iteration_{iter_num}_{training_list[0]}.txt'
    folder_path = training_folder(iter_num)
    file_path = os.path.join(folder_path, training_file)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    if os.path.exists(file_path):
        print('Sorry, file with iteration number already exists. Check your iter number!')
    else:
        ninety = calculate_ninety(max_weight)

        # wk1 65,75,85 3x5
        wk1_65 = calc_percentage(ninety, 65)
        wk1_75 = calc_percentage(ninety, 75)
        wk1_85 = calc_percentage(ninety, 85)

        # wk2 70,80,90 3x3
        wk2_70 = calc_percentage(ninety, 70)
        wk2_80 = calc_percentage(ninety, 80)
        wk2_90 = calc_percentage(ninety, 90)

        # wk3 75,85,95 5x3x1
        wk3_75 = calc_percentage(ninety, 75)
        wk3_85 = calc_percentage(ninety, 85)
        wk3_95 = calc_percentage(ninety, 95)

        # wk4 40, 50, 60 5x5
        wk4_40 = calc_percentage(ninety, 40)
        wk4_50 = calc_percentage(ninety, 50)
        wk4_60 = calc_percentage(ninety, 60)

        try:
            with open(file_path, mode='w') as file:
                file.write(
                    f"{training_list[0]}, real max: {max_weight} kg, 90%: {ninety} kg \n\n Week1: 65 % 1x5 {wk1_65} kg, \n Week1: 75 % 1x5 {wk1_75} kg, \n Week1: 85 % 1x5+ {wk1_85} kg, \n \n Week2: 70 % 1x3 {wk2_70} kg, \n Week2: 80 % 1x3 {wk2_80} kg, \n Week2: 90 % 1x3+ {wk2_90} kg, \n \n \n Week3: 75 % 1x5 {wk3_75} kg, \n Week3: 85 % 1x3 {wk3_85} kg, \n Week3: 95 % 1x1+ {wk3_95} kg, \n \n \n Week4 (deload): \n 40 % 1x5 {wk4_40} kg, \n Week4: 50 % 1x5 {wk4_50} kg, \n Week4: 60 % 1x5 {wk4_60} kg, \n")
        except FileNotFoundError as err:
            print(err)
