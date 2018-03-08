# Generated by Django 2.0.2 on 2018-03-08 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('zip_code', models.CharField(max_length=7)),
                ('address', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('discribe', models.TextField()),
                ('event_url', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=64)),
                ('user_password', models.CharField(max_length=32)),
                ('beacon_id', models.CharField(max_length=10)),
                ('user_url', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ss.User'),
        ),
    ]
