from django.urls import path, include
from ElderlyApp.views import AllUsersView, AllUserSettingsView ,UserView, UserSettingsView


urlpatterns = [
    path('user/', UserView.as_view(), name='user_view'),
    path('user_settings/', UserSettingsView.as_view(), name='user_settings_view'),
    path('all_users/', AllUsersView.as_view(), name='all_users_view'),
    path('all_user_settings/', AllUserSettingsView.as_view(), name='all_user_settings_view'),
]
