from django.db.models import fields
from django.forms import (
    ModelForm,
    CharField,
    PasswordInput,
)
from db_models.models import (
    CustomUser,
)


class RegistrationForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'confirm_password', 'user_type']
