from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_settings')
    text_size = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    title_size = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    accept_button_colors = models.CharField(max_length=7) 
    decline_button_colors = models.CharField(max_length=7) 

    class Meta:
        unique_together = ['user']

    def __str__(self):
        return 'Settings_' + self.user.username


class UserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_contacts')
    contact_name = models.CharField(max_length=50)
    county_code =  models.CharField(max_length=3) 
    cellphone_number = models.CharField(max_length=10)
    home_number = models.CharField(max_length=10)

    class Meta:
        unique_together = ['user','contact_name']

    def __str__(self):
        return 'Contacts_' + self.user.username
