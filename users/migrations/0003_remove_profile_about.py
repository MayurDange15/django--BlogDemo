# Generated by Django 3.1.7 on 2021-05-22 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
    ]