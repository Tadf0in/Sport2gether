# Generated by Django 4.2.5 on 2023-09-23 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='abrev',
        ),
    ]