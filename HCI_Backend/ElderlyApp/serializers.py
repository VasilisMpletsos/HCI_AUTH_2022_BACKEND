from rest_framework import serializers
from django.contrib.auth.models import User
from ElderlyApp.models import UserSetting, UserContact, UserData

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSetting
        fields = ['text_size', 'title_size', 'accept_button_colors', 'decline_button_colors']

class UserContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserContact
        fields = ['contact_name', 'county_code', 'cellphone_number', 'home_number']

class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ['telephone', 'civilian_id', 'home_address', 'informations', 'date_born']




