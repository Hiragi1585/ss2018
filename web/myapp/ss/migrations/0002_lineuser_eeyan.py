# Generated by Django 2.0.2 on 2018-03-09 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineuser',
            name='eeyan',
            field=models.IntegerField(default=0),
        ),
    ]