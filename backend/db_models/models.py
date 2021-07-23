from django.db.models import (
    Model,
    CharField,
    EmailField,
    DateTimeField,
    ForeignKey,
    SlugField,
    SET,
)
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import TextField
from autoslug import AutoSlugField


class UserType(Model):
    name = CharField(blank=False, null=False, unique=True, max_length=50)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


def get_or_create_user_type():
    user_type, created = UserType.objects.get_or_create(name='other')
    return user_type.id


class CustomUser(AbstractUser):
    username = CharField(blank=False, null=False, unique=True, max_length=50)
    email = EmailField(blank=False, null=False, unique=True)
    user_type = ForeignKey(
        to=UserType,
        blank=False,
        null=False,
        on_delete=SET(get_or_create_user_type),
        default=get_or_create_user_type()
    )
    slug = AutoSlugField(
        max_length=100, unique=True, blank=False, null=False,  populate_from='username',
    )

    avatar = CharField(blank=False, null=True, max_length=256)
    avatar_id = CharField(blank=False, null=True, max_length=256)
    about = TextField(blank=False, null=True, max_length=1000)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
