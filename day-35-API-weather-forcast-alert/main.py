import requests
import os
from twilio.rest import Client


OWM_API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
owm_api_key = os.environ['OWM_API_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_phone_number = os.environ['MY_PHONE']
twilio_number = os.environ['TWILIO_NUMBER']


if not owm_api_key or not account_sid or not auth_token or not my_phone_number or not twilio_number:
    exit("APIs KEY MISSING")

OWM_PARAMETERS = {
    "lat": 52.520008,
    "lon": 13.404954,
    "exclude": "current,minutely,daily",
    "appid": owm_api_key,
}

response = requests.get(url=OWM_API_ENDPOINT, params=OWM_PARAMETERS)
response.raise_for_status()
weather_data = response.json()
twelve_hours_data = weather_data["hourly"][0:11]
will_rain = False
for hour_weather in twelve_hours_data:
    for weather in hour_weather["weather"]:
        if weather["id"] < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to=my_phone_number,
        from_=twilio_number,
        body="Wezo: Bring your umbrella!"
    )
