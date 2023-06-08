# Generated by Django 4.2 on 2023-06-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_rename_project_vacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='remote',
            field=models.CharField(choices=[('RT', 'Remote'), ('FT', 'Full-Time')], default='Full-Time', max_length=512),
        ),
    ]