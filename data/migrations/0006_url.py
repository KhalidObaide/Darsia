# Generated by Django 2.2.6 on 2019-10-22 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20191022_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9999999)),
                ('url', models.CharField(max_length=9999999)),
            ],
        ),
    ]
