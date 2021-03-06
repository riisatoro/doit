import ipaddress
from django.forms import (
    FileField,
    ModelForm,
    CharField,
    PasswordInput,
    CheckboxSelectMultiple,
)
from django.forms.fields import MultipleChoiceField
from django.forms.models import ModelChoiceField
from app_utils.models import (
    CustomUser, MediaStorage,
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

    def save(self, commit=True, avatar=None):
        user = super(RegistrationForm, self).save(commit=False)
        user.is_active = False
        user.avatar = avatar
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'confirm_password',]
