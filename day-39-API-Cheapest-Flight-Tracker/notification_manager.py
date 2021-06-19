from twilio.rest import Client
import os


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.my_phone_number = os.environ['MY_PHONE']
        self.twilio_number = os.environ['TWILIO_NUMBER']        

    def send_sms(self, sms_body):
        client = Client(self.account_sid, self.auth_token)
        client.api.account.messages.create(
            to=self.my_phone_number,
            from_=self.twilio_number,
            body=sms_body
        )