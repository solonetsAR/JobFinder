from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .forms import CompanyCreationForm


class HomeView(TemplateView):
    template_name = "projects/home.html"

    def get(self, request):

        return render(request, self.template_name)


class CompanyCreateView(TemplateView):
    template_name = "projects/create_company.html"

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.account_type == 'CO':
                return render(request, self.template_name)
            else:
                return redirect('projects-home')
        else:
            return redirect('projects-home')

    @method_decorator(login_required)
    def post(self, request):
        form = CompanyCreationForm(request.POST, request.FILES)
        file = request.FILES.getlist('image')
        file_count = len(file)
        if file_count <= 1:
            if request.method == 'POST':
                print(form.errors)
                if form.is_valid():
                    print(form.errors)
                    create_company = form.save(commit=False)
                    create_company.owner = request.user
                    create_company.save()
                    print(create_company)
                    return redirect('projects-home')
                else:
                    company_form = CompanyCreationForm()
                    return render(request, self.template_name, {'company_form': company_form})


class CompanyEditView(TemplateView):
    template_name = "projects/edit_company.html"

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.account_type == 'CO':
                return render(request, self.template_name)
            else:
                return redirect('projects-home')
        else:
            return redirect('projects-home')

    @method_decorator(login_required)
    def post(self, request):
        form = CompanyCreationForm(request.POST, request.FILES, instance=request.user.company)
        file = request.FILES.getlist('image')
        file_count = len(file)
        if file_count <= 1:
            if request.method == 'POST':
                print(form.errors)
                if form.is_valid():
                    print(form.errors)
                    create_company = form.save()
                    create_company.save()
                    print(create_company)
                    return redirect('projects-home')
                else:
                    company_form = CompanyCreationForm()
                    return render(request, self.template_name, {'company_form': company_form})