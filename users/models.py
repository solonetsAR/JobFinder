from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django_countries.fields import CountryField

from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    ACCOUNT_TYPE_CHOICES = [
        ('TA', 'TALENT'),
        ('CO', 'COMPANY')
    ]
    email = models.EmailField(_('email address'), unique=True)

    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    account_type = models.CharField(max_length=512, choices=ACCOUNT_TYPE_CHOICES, default='TALENT')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=100, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    github = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    linkedin = models.CharField(max_length=150, blank=True, null=True)
    youtube = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_skills(self):
        return ", ".join([skills.name for skills in self.skills.all()])
