# Generated by Django 4.2.5 on 2023-09-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abrev', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('icon_url', models.URLField(blank=True, max_length=128)),
            ],
        ),
    ]
