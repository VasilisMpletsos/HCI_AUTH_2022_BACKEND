from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    text_size = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    title_size = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    accept_button_colors = models.CharField(max_length=7) 
    decline_button_colors = models.CharField(max_length=7) 

    class Meta:
        unique_together = ['user']

    def __str__(self):
        return 'Settings' + self.user.username
