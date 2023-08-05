from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ("email", "national_code", "personal_id",)
    list_filter = ("email", "national_code", "is_active", "is_staff", "is_teacher", "is_supervisor", "is_consultant", "personal_id",)
    ordering = ("-created_date",)
    list_display = ("email", "national_code", "is_active", "is_staff", "is_teacher", "is_supervisor", "is_consultant", "personal_id",)
    fieldsets = (
        ("Authentication", {"fields": ("email", "national_code", "personal_id")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_teacher", "is_supervisor", "is_consultant")}),
        (
            "Group Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "national_code",
                    "phone",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_teacher",
                    "is_supervisor",
                    "is_consultant",
                    "personal_id",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
