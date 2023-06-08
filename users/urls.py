from django.urls import path
from .views import SignUpView, LogOutView, LogInView, ProfileEditView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="users-signup"),
    path("logout/", LogOutView, name="users-logout"),
    path("login/", LogInView, name="users-login"),
    path("edit-profile/", ProfileEditView.as_view(), name='edit-profile')
]
