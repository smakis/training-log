import smtplib
from email.message import EmailMessage
import os
from os import listdir
from os.path import isfile, join
from training_functions import training_folder


def send_program_by_mail(iter_num: int, address: str, psw: str):

    folder, files = email_attachment(iter_num)
    try:
        email = EmailMessage()
        email['from'] = address
        email['to'] = address
        email['subject'] = 'Hei, ohjelmasi'

        # The body and the attachments for the mail
        contents = 'Liitteenä ohjelmasi'
        email.set_content(contents)
        if files:
            for file in files:
                path_to_file = os.path.join(folder, file)
                email.add_attachment(
                    open(path_to_file, "r").read(), filename=f'{file}')
        else:
            print('No files found!')

        with smtplib.SMTP(host='smtp.live.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(address, psw)
            smtp.send_message(email)
            print(f'all good msg sent successfully to {address}')
    except Exception as err:
        print(err)


# Returns files from folder which is specified by iteration number
def email_attachment(iter_num: int):

    folder_path = training_folder(iter_num)
    if not os.path.exists(folder_path):
        print(
            f'Folder with iteration number {iter_num} does not exist. Files cannot be retrieved!')
    else:
        training_files = [file for file in listdir(
            folder_path) if isfile(join(folder_path, file))]
        return folder_path, training_files
