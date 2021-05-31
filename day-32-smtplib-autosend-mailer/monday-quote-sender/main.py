import datetime as dt
import smtplib
import random


SENDER_MAIL = "test@gmail.com"
PASSWORD = "TESTP@SSWORD"
TO_MAIL = "test2@gmail.com"

# Setup SMTP server: python -m smtpd -c DebuggingServer -n localhost:1025

def send_mail(msg):
    with smtplib.SMTP('localhost', 1025) as connection:
        # connection.starttls()
        # connection.login(user=SENDER_MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_MAIL,
            to_addrs=TO_MAIL,
            msg=f"Subject:Monday Motivational Quote\n\n{msg}"
        )


quotes = []

try:
    with open("quotes.txt") as file:
        quotes = file.readlines()
except FileNotFoundError:
    print("Quotes file not found! Goodbye!")
    exit()

today = dt.datetime.now().weekday()

if today == 6:
    today_quote = random.choice(quotes)
    send_mail(today_quote)
