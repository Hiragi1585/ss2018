# Generated by Django 2.0.2 on 2018-03-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=512)),
                ('timestamp', models.CharField(max_length=512)),
                ('hw_id', models.CharField(max_length=512)),
            ],
        ),
    ]
