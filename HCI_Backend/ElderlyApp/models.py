from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_data')
    telephone = models.CharField(max_length=10)
    civilian_id = models.CharField(max_length=10)
    home_address = models.CharField(max_length=30)
    informations = models.TextField()
    date_born = models.DateField()

    class Meta:
        unique_together = ['user']

    def __str__(self):
        return 'Data_' + self.user.username
        
class UserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_settings')
    text_size = models.IntegerField(default=15, validators=[MinValueValidator(1)])
    title_size = models.IntegerField(default=20, validators=[MinValueValidator(1)])
    accept_button_colors = models.CharField(default="#008800", max_length=7) 
    decline_button_colors = models.CharField(default="#ff0000", max_length=7) 

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
    emergency_contact = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user','contact_name','emergency_contact']

    def __str__(self):
        return 'Contacts_' + self.user.username + "_" + self.contact_name
