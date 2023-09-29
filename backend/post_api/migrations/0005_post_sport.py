# Generated by Django 4.2.5 on 2023-09-29 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_api', '0002_remove_sport_abrev'),
        ('post_api', '0004_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport_api.sport'),
        ),
    ]