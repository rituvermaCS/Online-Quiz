# Generated by Django 3.0.2 on 2020-02-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
