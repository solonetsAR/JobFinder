from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from projects.models import Company
from .models import Skill, User, Profile
from users.forms import CustomUserCreationForm, EditProfileForm, CustomUserChangeForm


def LogInView(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('projects-home')
        else:
            error = "Incorrect email or password"
            return render(request, 'registration/signup.html', {'error': error})


def LogOutView(request):
    logout(request)
    return redirect('projects-home')


class SignUpView(TemplateView):
    template_name = "registration/signup.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('projects-home')
        else:
            return render(request, self.template_name)

    def post(self, request):
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            new_user = authenticate(
                email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password2']
            )
            print(new_user)
            login(request, new_user)
            if new_user.account_type == 'TA':
                Profile.objects.create(user=new_user)
            elif new_user.account_type == 'CO':
                Company.objects.create(owner=new_user)
            return redirect(reverse('projects-home'))
        return render(request, self.template_name, {'user_form': user_form})


class ProfileEditView(TemplateView):
    template_name = "registration/edit_profile.html"

    def get(self, request):
        if request.user.is_authenticated:
            skills = Skill.objects.all()
            params = {
                'skills': skills,
            }
            if request.user.account_type == 'TA':
                return render(request, self.template_name, params)
            elif request.user.account_type == 'CO':
                return redirect('edit-company')
            else:
                return redirect('projects-home')

        else:
            return redirect('projects-home')

    @method_decorator(login_required)
    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user.profile)
        if request.method == 'POST':
            if form.is_valid():
                edit_profile = form.save()
                edit_profile.save()
                return redirect('projects-home')
            else:
                profile_form = EditProfileForm()
                skills = Skill.objects.all()
                context = {
                    'profile_form': profile_form,
                    'skills': skills,
                }
                return render(request, self.template_name, context)
