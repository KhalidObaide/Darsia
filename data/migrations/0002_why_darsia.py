# Generated by Django 2.2.6 on 2019-10-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Why_darsia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=99999)),
                ('bio', models.CharField(max_length=99999)),
                ('img', models.CharField(max_length=99999)),
                ('time_added', models.CharField(max_length=99999)),
                ('status', models.CharField(max_length=99999)),
            ],
        ),
    ]
