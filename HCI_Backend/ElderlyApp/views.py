from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.serializers import serialize 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, authentication, status
from ElderlyApp.serializers import UserSerializer, UserSettingsSerializer, UserContactsSerializer, UserDataSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ElderlyApp.permissions import IsSelf
from ElderlyApp.models import UserSetting, UserContact, UserData

# Create your views here.
class AllUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AllUserSettingsView(generics.ListAPIView):
    serializer_class = UserSettingsSerializer
    queryset = UserSetting.objects.all()

class AllUserContactsView(generics.ListAPIView):
    serializer_class = UserContactsSerializer
    queryset = UserContact.objects.all()

class AllUserDataView(generics.ListAPIView):
    serializer_class = UserDataSerializer
    queryset = UserData.objects.all()

class UserView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        data = User.objects.get(id = request.user.id);
        serializer = UserSerializer(data, many=False)
        return Response(serializer.data)

class UserSettingsView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        data = UserSetting.objects.get(user = request.user);
        serializer = UserSettingsSerializer(data, many=False)
        return Response(serializer.data)

class UserContactsView(generics.ListAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserContactsSerializer

    def get_queryset(self):
        return UserContact.objects.filter(user=self.request.user);

class UserDataView(generics.ListAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        data = UserData.objects.get(user = self.request.user);
        serializer = UserDataSerializer(data, many=False)
        return Response(serializer.data)

class LogoutView(APIView):
    def get(self, request, format=None):
        logout(request);
        return Response(status=status.HTTP_201_CREATED)

