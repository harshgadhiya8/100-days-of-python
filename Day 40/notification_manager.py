from twilio.rest import Client
import smtplib

TWILIO_SID = "copy from notes"
TWILIO_AUTH_TOKEN = "copy from notes"
TWILIO_VIRTUAL_NUMBER = "copy from notes"
TWILIO_VERIFIED_NUMBER = "copy from notes"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
    def send_emails(self, emails, message):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login("copy email from notes", "copy smtp email app password from notes")
            for email in emails:
                connection.sendmail(
                    from_addr='copy email from notes',
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )