from django import forms
from django_countries.fields import CountryField

from .models import Company, Vacancy


class CompanyEditForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ("company_name", "email_company", "description", "website", "country")


class VacancyCreateForm(forms.ModelForm):
    salary_upper = forms.IntegerField(required=False)

    class Meta:
        model = Vacancy
        fields = ("title", "description", "country", "skills", "salary_lower", "salary_upper", "work_experience",
                  "job_type", "remote")
