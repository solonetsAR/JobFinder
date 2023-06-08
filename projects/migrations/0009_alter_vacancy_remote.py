# Generated by Django 4.2 on 2023-06-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_vacancy_remote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='remote',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='No', max_length=512),
        ),
    ]