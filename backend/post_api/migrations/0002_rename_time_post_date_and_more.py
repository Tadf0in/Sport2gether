# Generated by Django 4.2.5 on 2023-09-22 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='time',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='posted_time',
            new_name='posted_date',
        ),
    ]
