from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from users.models import Profile, Skill
from .forms import CompanyEditForm, VacancyCreateForm
from .models import Vacancy, Company


class HomeView(TemplateView):
    template_name = "projects/home.html"

    def get(self, request):
        return render(request, self.template_name)


def DevelopmentView(request):
    return render(request, 'in_development.html')


class CompanyProfileView(TemplateView):
    template_name = "projects/profile_page.html"

    def get(self, request, id):
        company = Company.objects.get(id=id)
        context = {
            'company': company
        }
        return render(request, self.template_name, context)


class CompanyEditView(TemplateView):
    template_name = "projects/edit_company.html"

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.account_type == 'CO':
                return render(request, self.template_name)
            else:
                return redirect('projects-home')
        else:
            return redirect('users-signup')

    @method_decorator(login_required)
    def post(self, request):
        form = CompanyEditForm(request.POST, instance=request.user.company)
        if request.method == 'POST':
            print(form.errors)
            if form.is_valid():
                print(form.errors)
                create_company = form.save()
                create_company.save()
                print(create_company)
                return redirect('projects-home')
            else:
                company_form = CompanyEditForm()
                return render(request, self.template_name, {'company_form': company_form})


class CompaniesView(TemplateView):
    template_name = "projects/companies_page.html"

    def get(self, request):
        companies = Company.objects.exclude(company_name__isnull=True).exclude(company_name__exact='').all()
        context = {
            'companies': companies
        }
        return render(request, self.template_name, context)


class TalentProfileView(TemplateView):
    template_name = "projects/talent_profile.html"

    def get(self, request, id):
        profile = Profile.objects.get(id=id)
        context = {
            'profile': profile
        }
        return render(request, self.template_name, context)


class TalentsView(TemplateView):
    template_name = "projects/talents_page.html"

    def get(self, request):
        profiles = Profile.objects.exclude(first_name__isnull=True).exclude(first_name__exact='').all()
        context = {
            'profiles': profiles
        }
        return render(request, self.template_name, context)


def talent_by_skill(request, id):
    skill = get_object_or_404(Skill, id=id)
    profiles = Profile.objects.filter(skills__in=[skill]).all()
    print(profiles)
    context = {
        "profiles": profiles
    }

    return render(request, "projects/talents_page.html", context)


class VacancyProfileView(TemplateView):
    template_name = "projects/vacancy_profile.html"

    def get(self, request, id):
        vacancy = Vacancy.objects.get(id=id)
        company = Company.objects.get(id=vacancy.owner.id)
        context = {
            'vacancy': vacancy,
            'company': company,
        }
        return render(request, self.template_name, context)


class DeleteVacancyView(View):
    @method_decorator(login_required)
    def post(self, request):
        vacancy = Vacancy.objects.get(id=request.POST['vacancy_id'])
        if request.user.company == vacancy.owner:
            vacancy.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class VacancyCreateView(TemplateView):
    template_name = "projects/create_vacancy.html"

    @method_decorator(login_required)
    def get(self, request):
        if request.user.company:
            skills = Skill.objects.order_by('name').all()
            context = {
                'skills': skills,
            }
            return render(request, self.template_name, context)
        else:
            return redirect('projects-home')

    @method_decorator(login_required)
    def post(self, request):
        if request.method == 'POST':
            print(request.POST)
            form = VacancyCreateForm(request.POST)
            print(form.errors)
            if form.is_valid():
                print(form.errors)
                create_vacancy = form.save()
                create_vacancy.owner = request.user.company
                create_vacancy.save()
                form._save_m2m()
                print(create_vacancy)
                return redirect('projects-home')
            else:
                vacancy_form = VacancyCreateForm()
                skills = Skill.objects.all()
                context = {
                    'skills': skills,
                    'vacancy_form': vacancy_form,
                }
                return render(request, self.template_name, context)


class VacanciesView(TemplateView):
    template_name = "projects/vacancies_page.html"

    def get(self, request):
        vacancies = Vacancy.objects.exclude(title__isnull=True).exclude(title__exact='').all()
        context = {
            'vacancies': vacancies
        }
        return render(request, self.template_name, context)


class VacanciesList(TemplateView):
    template_name = "projects/vacancies_list.html"

    def get(self, request):
        vacancies = Vacancy.objects.filter(owner=request.user.company).all()
        context = {
            'vacancies': vacancies
        }
        return render(request, self.template_name, context)


class VacancyView(TemplateView):
    template_name = "projects/edit_vacancy.html"

    def get(self, request, id):
        vacancy = Vacancy.objects.get(id=id)
        skills = Skill.objects.order_by('name').all()
        context = {
            'vacancy': vacancy,
            'skills': skills,
        }
        if request.user.company == vacancy.owner:
            return render(request, self.template_name, context)
        else:
            return redirect('projects-home')

    @method_decorator(login_required)
    def post(self, request, id):
        if request.method == 'POST':
            form = VacancyCreateForm(request.POST, instance=Vacancy.objects.get(id=id))
            if form.is_valid():
                print(form.errors)
                edit_vacancy = form.save()
                edit_vacancy.save()
                form._save_m2m()
                return redirect('projects-home')
            else:
                vacancy_form = VacancyCreateForm()
                skills = Skill.objects.order_by('name').all()
                context = {
                    'skills': skills,
                    'vacancy_form': vacancy_form,
                }
                return render(request, self.template_name, context)


def vacancy_by_skill(request, id):
    skill = get_object_or_404(Skill, id=id)
    print(skill)
    vacancies = Vacancy.objects.filter(skills__in=[skill]).all()
    print(vacancies)
    context = {
        "vacancies": vacancies
    }

    return render(request, "projects/vacancies_page.html", context)
