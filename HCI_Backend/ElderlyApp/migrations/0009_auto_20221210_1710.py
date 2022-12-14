# Generated by Django 3.1.2 on 2022-12-10 15:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ElderlyApp', '0008_auto_20221210_1709'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercontact',
            unique_together={('user', 'contact_name', 'emergency_contact')},
        ),
    ]
