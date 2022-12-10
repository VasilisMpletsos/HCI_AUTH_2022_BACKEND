from rest_framework import serializers
from django.contrib.auth.models import User
from ElderlyApp.models import UserSettings

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserSettingsSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = UserSettings
        fields = ['user', 'text_size', 'title_size', 'accept_button_colors', 'decline_button_colors']



