from types import DynamicClassAttribute
import requests
from datetime import datetime
import time
import smtplib
import sys


LATITUDE = 52.520008
LONGITUDE = 13.404954
MARGIN = 5
SENDER_MAIL = "test@gmail.com"
PASSWORD = "TESTP@SSWORD"
TO_MAIL = "test2@gmail.com"


def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    print(f"Berlin latitude: {LATITUDE} longitute: {LONGITUDE}")
    print(f"ISS current latitude: {iss_lat} longitude: {iss_long}")

    if (iss_lat <= LATITUDE + MARGIN) and iss_lat >= LATITUDE - MARGIN:
        if (iss_long <= LONGITUDE + MARGIN) and iss_long >= LONGITUDE - MARGIN:
            return True
    return False


def is_night():
    sun_parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=sun_parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now_hour = datetime.now().utcnow().hour
    if time_now_hour >= sunset or time_now_hour <= sunrise:
        return True
    return False


# Setup SMTP server: python -m smtpd -c DebuggingServer -n localhost:1025
def send_mail():
    with smtplib.SMTP('localhost', 1025) as connection:
        # connection.starttls()
        # connection.login(user=SENDER_MAIL, password=PASSWORD)
        msg = f"ISS passing over your head in the sky!\nUTC Time: {datetime.utcnow()}"
        print(msg)
        connection.sendmail(
            from_addr=SENDER_MAIL,
            to_addrs=TO_MAIL,
            msg=f"Subject:Look up to the sky!\n\n{msg}"
        )


def main():
    try:
        while True:
            if is_iss_above() and is_night():
                send_mail()
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        print('\n! Received keyboard interrupt, quitting!.\n')
        sys.exit()


if __name__ == "__main__":
    main()
