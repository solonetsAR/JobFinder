from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import authenticate
from .models import User, Profile, Skill
from django_countries.fields import CountryField


class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    account_type = forms.ChoiceField(widget=forms.RadioSelect, choices=User.ACCOUNT_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ("email", "account_type")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("account_type",)


class CustomUserLoginForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("invalid credential")


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'country', 'skills', 'description', 'github', 'twitter',
                  'linkedin', 'youtube']

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'country', 'skills', 'description', 'github', 'twitter',
                  'linkedin', 'youtube']
