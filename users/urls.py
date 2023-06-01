from django.urls import path
from .views import SignUpView, LogOutView, LogInView, ProfileCreateView, ProfileEditView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="users-signup"),
    path("logout/", LogOutView, name="users-logout"),
    path("login/", LogInView, name="users-login"),
    path("create-profile/", ProfileCreateView.as_view(), name='create-profile'),
    path("edit-profile/", ProfileEditView.as_view(), name='edit-profile')
]
