from training_functions import calculate_max_weight, create_training_iteration
from send_email import send_program_by_mail
from completed_trainings import save_to_csv


def Main():
    while True:
        try:
            iter_num = 0
            user_input = int(input(
                'Give number of selected task to perform: '
                + ' \n 1. Calculate max \n 2. Create training plan'
                + ' \n 3. Email program'
                + ' \n 4. Save training week\'s last set to CSV file'
                + ' \n 5. Quit\n Input: '))

            if user_input == 5:
                print("------------ EXITING --------------- \n\n")
                break

            elif user_input == 1:
                movement_input_list = input(
                    'Give movement, weight used and reps done separated by a comma (e.g squat,75,10). \n Input:  ').split(',')
                if len(movement_input_list) < 3:
                    print("Sorry, you didn't give all neccessary values. Try again!\n")
                else:
                    print('Performed movement', movement_input_list)
                    max_weight = calculate_max_weight(
                        float(movement_input_list[1]), int(movement_input_list[2]))
                    print('Your max weight is: ', max_weight)

            elif user_input == 2:
                iter_num = int(
                    input('Give number of training iteration (e.g 1 (First 1-4 wk set etc)). \n Input: '))
                try:
                    if max_weight:
                        create_training_iteration(iter_num,
                                                  max_weight, movement_input_list)
                except NameError as err:
                    print('Calculated max needed, but not found')
                    print(err)

            elif user_input == 3:
                email_input = input(
                    'Give iteration number, email address and password separated by comma: ').split(',')
                send_program_by_mail(
                    email_input[0], email_input[1], email_input[2])

            elif user_input == 4:
                day = input('Give date of training e.g 2020-30-02: ')
                iter_num = int(input('Give iter num: '))
                wk_nbr = int(input('Give training week number: '))
                excercise = input('Give trained excercise: ')
                weight = float(input('Give weight used: '))
                reps = int(input('Give reps performed: '))
                comment = input("Additional comments: ")
                save_to_csv(day, iter_num, wk_nbr,
                            excercise, weight, reps, comment)

        except ValueError as err:
            print('Input needs to be a whole number')


if __name__ == "__main__":
    Main()
