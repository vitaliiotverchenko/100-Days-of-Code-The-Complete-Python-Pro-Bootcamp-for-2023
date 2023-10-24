##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = 'vixenbqlab@gmail.com'
PASSWORD = 'yoambfqzsmtjlmxp'
LETTER_TEMPLATES_DIR = "Day_32_Mail_sending_project/letter_templates/"


def send_birthday_letter(email, letter_content):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f'Subject: Happy Birthday!\n\n{letter_content}')


def main():
    # make datetime object
    now = dt.datetime.now()
    try:
        birthdays_df = pd.read_csv('Day_32_Mail_sending_project/birthdays.csv')
        birthdays_dict = birthdays_df.to_dict(orient='records')
    except FileNotFoundError:
        print('File birthdays.csv not found!')

    for person in birthdays_dict:
        if person['month'] == now.month and person['day'] == now.day:
            print(f"Today is {person['name']}'s birthday! Sending a letter!")
            random_letter = random.randint(1, 3)
            try:
                with open(f"{LETTER_TEMPLATES_DIR}letter_{random_letter}.txt", mode='r') as file:
                    letter = file.read()
                    letter = letter.replace('[NAME]', person['name'])
                    send_birthday_letter(person['email'], letter)
            except FileNotFoundError:
                print('File not found')


if __name__ == "__main__":
    main()
