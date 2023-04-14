from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "first_name", "last_name", "phone_number", "bio", "date_of_birth", "is_staff", "is_active")
    list_filter = ("email", "first_name", "last_name", "phone_number", "bio", "date_of_birth", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "first_name", "last_name", "phone_number", "bio", "date_of_birth",
                           "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "first_name", "last_name", "phone_number", "bio", "date_of_birth", "password1",
                "password2", "is_staff", "is_active"
            )}
         ),
    )
    search_fields = ("last_name", "email")
    ordering = ("last_name", "email")


admin.site.register(User, CustomUserAdmin)
