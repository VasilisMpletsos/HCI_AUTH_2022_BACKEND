from django.urls import path, include
from ElderlyApp.views import AllUsersView, AllUserSettingsView, AllUserContactsView, AllUserDataView
from ElderlyApp.views import UserView, UserUpdateView, UserSettingsView, UserSettingsUpdateView, UserContactsView, UserDetailContactsView, UserDataView, LogoutView


urlpatterns = [
    path('user/', UserView.as_view(), name='user_view'),
    path('user/<int:pk>', UserUpdateView.as_view(), name='user_update_view'),
    path('user_settings/', UserSettingsView.as_view(), name='user_settings_view'),
    path('user_settings/<int:pk>', UserSettingsUpdateView.as_view(), name='user_settings_update_view'),
    path('user_contacts/', UserContactsView.as_view(), name='user_contacts_view'),
    path('user_contacts/<int:pk>', UserDetailContactsView.as_view(), name='user_contacts_details_view'),
    path('user_data/', UserDataView.as_view(), name='user_data_view'),
    path('all_users/', AllUsersView.as_view(), name='all_users_view'),
    path('all_users_settings/', AllUserSettingsView.as_view(), name='all_users_settings_view'),
    path('all_users_contacts/', AllUserContactsView.as_view(), name='all_users_contacts_view'),
    path('all_users_data/', AllUserDataView.as_view(), name='all_users_data_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
]
