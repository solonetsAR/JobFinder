# Generated by Django 4.2 on 2023-05-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_is_talent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='last name'),
        ),
    ]
