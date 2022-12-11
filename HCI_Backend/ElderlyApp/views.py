from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.serializers import serialize 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, authentication, status
from ElderlyApp.serializers import UserSerializer, UserSettingsSerializer, UserContactsSerializer, UserDataSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ElderlyApp.permissions import IsSelf, HasObjectPermissions
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

class UserView(generics.RetrieveAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        data = User.objects.get(id=self.request.user.id);
        serializer = UserSerializer(data, many=False)
        return Response(serializer.data)

class UserUpdateView(generics.RetrieveUpdateAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSelf]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserSettingsView(generics.RetrieveAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        data = UserSetting.objects.get(user=self.request.user);
        serializer = UserSettingsSerializer(data, many=False)
        return Response(serializer.data)
    
class UserSettingsUpdateView(generics.RetrieveUpdateAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, HasObjectPermissions]
    serializer_class = UserSettingsSerializer
    queryset = UserSetting.objects.all()

class UserContactsView(generics.ListCreateAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserContactsSerializer

    def get_queryset(self):
        return UserContact.objects.filter(user=self.request.user);

    def post(self, request, format=None):
        count_contacts = UserContact.objects.filter(user=request.user).count();
        if count_contacts >= 6:
            return Response({"error": "Too Many Contacts"},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            serializer = self.get_serializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save(user = self.request.user)
                return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

class UserDetailContactsView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, HasObjectPermissions]
    serializer_class = UserContactsSerializer
    queryset = UserContact.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
       
        

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
        return Response(status=status.HTTP_202_ACCEPTED)

