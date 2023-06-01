# Generated by Django 4.2 on 2023-04-26 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_skill_remove_user_bio_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='profile_images/default.jpg', null=True, upload_to='profile_images')),
                ('company_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('website', models.CharField(blank=True, max_length=150, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('salary_lower', models.IntegerField(max_length=100000)),
                ('salary_upper', models.IntegerField(blank=True, max_length=100000, null=True)),
                ('work_experience', models.CharField(choices=[('NO', 'No Experience Required'), ('EN', 'Entry Level'), ('MD', 'Mid Level'), ('SN', 'Senior Level')], max_length=512)),
                ('job_type', models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-Time'), ('CT', 'Contract'), ('TR', 'Temporary'), ('IN', 'Internship')], max_length=512)),
                ('remote', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.company')),
                ('skills', models.ManyToManyField(blank=True, to='users.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('created', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projects.company')),
                ('likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]