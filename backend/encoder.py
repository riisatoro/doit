from django.conf import settings
from itsdangerous import URLSafeTimedSerializer


def get_serializer():
    return URLSafeTimedSerializer(settings.SECRET_KEY)


def encode_email_token(email):
    serializer = get_serializer()
    return serializer.dumps(
        email,
        salt=settings.SECRET_EMAIL_SALT,
    )


def decode_email_token(token):
    serializer = get_serializer()
    try:
        return serializer.loads(
            token,
            salt=settings.SECRET_EMAIL_SALT,
            max_age=settings.TOKEN_EXPIRES_SECONDS,
        )
    except Exception:
        raise ValueError('Confirmation link is invalid or expired')
