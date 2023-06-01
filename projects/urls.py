from django.urls import path
from .views import HomeView, CompanyCreateView, CompanyEditView

urlpatterns = [
    path("", HomeView.as_view(), name="projects-home"),
    path("create-company/", CompanyCreateView.as_view(), name='create-company'),
    path("edit-company/", CompanyEditView.as_view(), name='edit-company'),

]