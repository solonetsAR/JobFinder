from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from users.models import Skill, User
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    email_company = models.EmailField(_('email address'), blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    country = CountryField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner)

    def get_company_profile(self):
        return reverse("company-profile", args=[self.id])

    class Meta:
        ordering = ['created']


class Vacancy(models.Model):
    WORK_EXPERIENCE_CHOICES = [
        ('NO', 'No Experience Required'),
        ('EN', 'Entry Level'),
        ('MD', 'Mid Level'),
        ('SN', 'Senior Level')
    ]

    JOB_TYPE_CHOICES = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('CT', 'Contract'),
        ('TR', 'Temporary'),
        ('IN', 'Internship')
    ]

    REMOTE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    owner = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    country = CountryField()
    date_posted = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill)
    salary_lower = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100000)])
    salary_upper = models.IntegerField(validators=[MinValueValidator(salary_lower),
                                       MaxValueValidator(100000)], blank=True, null=True)
    work_experience = models.CharField(max_length=512, choices=WORK_EXPERIENCE_CHOICES)
    job_type = models.CharField(max_length=512, choices=JOB_TYPE_CHOICES)
    remote = models.CharField(max_length=512, choices=REMOTE_CHOICES, default='No')

    def __str__(self):
        return str(self.title)

    def get_vacancy_url(self):
        return reverse("edit-vacancy", args=[self.id])

    def get_vacancy_profile(self):
        return reverse("vacancy-profile", args=[self.id])

    def get_skills(self):
        return ", ".join([skills for skills in self.skills.all()])

    class Meta:
        ordering = ['date_posted']


class Comment(models.Model):
    content = models.TextField(max_length=500)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='comments')
    created = models.DateField(auto_now_add=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='comments')

    def comments_count(self):
        return len(Comment.objects.all())
