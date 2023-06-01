from django import forms
from django_countries.fields import CountryField

from .models import Company


class CompanyCreationForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Company
        fields = ("image", "company_name", "email_company", "description", "website", "country")
