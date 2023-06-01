from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Profile, Skill


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "phone_number", "date_of_birth", "account_type",
                    "is_staff", "is_active")
    list_filter = ("email", "phone_number", "date_of_birth", "account_type",
                   "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "phone_number", "date_of_birth",
                           "password", "account_type")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "phone_number", "date_of_birth", "password1",
                "password2", "account_type", "is_staff", "is_active"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Skill)
