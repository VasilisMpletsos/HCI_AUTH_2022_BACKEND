# Generated by Django 3.1.2 on 2022-12-10 13:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ElderlyApp', '0002_auto_20221210_1541'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserContacts',
            new_name='UserContact',
        ),
        migrations.RenameModel(
            old_name='UserSettings',
            new_name='UserSetting',
        ),
    ]