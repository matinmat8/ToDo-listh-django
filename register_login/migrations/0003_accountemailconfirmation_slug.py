# Generated by Django 3.2.9 on 2022-03-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_login', '0002_auto_20220312_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountemailconfirmation',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
