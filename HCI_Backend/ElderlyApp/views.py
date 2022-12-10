from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication
from ElderlyApp.serializers import UserSerializer, UserSettingsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ElderlyApp.permissions import IsSelf
from ElderlyApp.models import UserSettings

# Create your views here.
class AllUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AllUserSettingsView(generics.ListAPIView):
    serializer_class = UserSettingsSerializer
    queryset = UserSettings.objects.all()

class UserView(generics.ListAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username);

class UserSettingsView(generics.ListAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserSettingsSerializer

    def get_queryset(self):
        return UserSettings.objects.filter(user=self.request.user);
