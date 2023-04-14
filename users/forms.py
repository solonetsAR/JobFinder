from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User
from django.core.validators import RegexValidator


class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17)
    bio = forms.CharField(required=False)

    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_number", "bio")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_number", "bio")