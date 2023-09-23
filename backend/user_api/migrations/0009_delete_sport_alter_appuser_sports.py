# Generated by Django 4.2.5 on 2023-09-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_api', '0001_initial'),
        ('user_api', '0008_appuser_sports_delete_usersports'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sport',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='sports',
            field=models.ManyToManyField(blank=True, related_name='sports', to='sport_api.sport'),
        ),
    ]
