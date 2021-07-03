
from django.conf import settings
import requests



def send_email(recepients: list):
    return requests.post(
        f'https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages',
        auth=("api", settings.MAILGUN_API_KEY),
        data={"from": settings.MAILGUN_FROM,
            "to": recepients,
            "subject": "Hello",
            "text": "Testing some Mailgun awesomness!"}
        )
