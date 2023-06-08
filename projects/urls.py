from django.urls import path
from .views import HomeView, CompanyEditView, CompaniesView, TalentsView, VacancyCreateView, VacanciesView, \
    VacanciesList, VacancyView, DevelopmentView, DeleteVacancyView, CompanyProfileView, TalentProfileView,\
    VacancyProfileView, vacancy_by_skill, talent_by_skill

urlpatterns = [
    path("", HomeView.as_view(), name="projects-home"),
    path("company-<int:id>/", CompanyProfileView.as_view(), name='company-profile'),
    path("edit-company/", CompanyEditView.as_view(), name='edit-company'),
    path("companies/", CompaniesView.as_view(), name='companies-page'),
    path("talents/", TalentsView.as_view(), name='talents-page'),
    path("talents-<int:id>/", talent_by_skill, name='talents-skills'),
    path("talent-<int:id>/", TalentProfileView.as_view(), name='talent-profile'),
    path("create-vacancy/", VacancyCreateView.as_view(), name='vacancy-create'),
    path("vacancies-list/vacancy-delete/", DeleteVacancyView.as_view(), name="vacancy-delete"),
    path("vacancies/", VacanciesView.as_view(), name='vacancies-page'),
    path("vacancies-<int:id>/", vacancy_by_skill, name='vacancies-skills'),
    path("vacancies-list/", VacanciesList.as_view(), name='vacancies-list'),
    path("vacancy-<int:id>/", VacancyProfileView.as_view(), name='vacancy-profile'),
    path("edit-vacancy-<int:id>/", VacancyView.as_view(), name='edit-vacancy'),
    path("development/", DevelopmentView, name='development')
]
