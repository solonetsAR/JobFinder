# Generated by Django 4.2 on 2023-06-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_vacancy_remote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]