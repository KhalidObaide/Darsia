# Generated by Django 2.2.6 on 2019-10-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_timed_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='timed_user',
            name='url',
            field=models.CharField(default=0, max_length=9999999),
            preserve_default=False,
        ),
    ]