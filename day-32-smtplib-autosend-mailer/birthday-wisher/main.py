import datetime as dt
import smtplib
import random
from pandas import read_csv
import glob


LETTERS_LOCATION = "letter_templates"
SENDER_MAIL = "test@gmail.com"
PASSWORD = "TESTP@SSWORD"
TO_MAIL = "test2@gmail.com"


# Setup SMTP server: python -m smtpd -c DebuggingServer -n localhost:1025
def send_mail(rcpt_name, msg):
    with smtplib.SMTP('localhost', 1025) as connection:
        # connection.starttls()
        # connection.login(user=SENDER_MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_MAIL,
            to_addrs=TO_MAIL,
            msg=f"Subject:Happy Birthday {rcpt_name}\n\n{msg}"
        )


def generate_letter(rcpt):
    letters = glob.glob(f"{LETTERS_LOCATION}/*.txt")
    with open(random.choice(letters)) as random_letter:
        return random_letter.read().replace("[NAME]", rcpt)


df_birthdays = read_csv("birthdays.csv").to_dict('records')

today = dt.datetime.now()
for birthday in df_birthdays:
    if today.month == birthday['month'] and today.day == birthday['day']:
        rcpt = birthday['name']
        body = generate_letter(rcpt)
        send_mail(rcpt, body)
