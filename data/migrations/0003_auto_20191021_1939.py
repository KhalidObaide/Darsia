# Generated by Django 2.2.6 on 2019-10-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_why_darsia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='why_darsia',
            name='bio',
            field=models.TextField(max_length=999999),
        ),
    ]
