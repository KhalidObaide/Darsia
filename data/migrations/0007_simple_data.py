# Generated by Django 2.2.6 on 2019-10-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simple_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9999999)),
                ('data', models.CharField(max_length=9999999)),
            ],
        ),
    ]