# Generated by Django 2.2.6 on 2019-10-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_simple_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timed_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999999)),
                ('username', models.CharField(max_length=9999999)),
                ('email', models.CharField(max_length=999999)),
                ('password', models.CharField(max_length=999999)),
                ('time_created', models.CharField(max_length=999999)),
            ],
        ),
    ]
