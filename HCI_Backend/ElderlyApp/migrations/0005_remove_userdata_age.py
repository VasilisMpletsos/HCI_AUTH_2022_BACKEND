# Generated by Django 3.1.2 on 2022-12-10 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ElderlyApp', '0004_auto_20221210_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='age',
        ),
    ]
