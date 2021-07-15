
from django.conf import settings
import requests


def send_email(recepients: list, token: str):
    return requests.post(
        f'https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages',
        auth=("api", settings.MAILGUN_API_KEY),
        data={"from": settings.MAILGUN_FROM,
            "to": recepients,
            "subject": "Confirm your email on DOIT stock!",
            "text": f"Please, confirm your email: http://localhost:8000/auth/confirm/{token}/"}
        )
