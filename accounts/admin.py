from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ("email",)
    list_filter = ("email", "is_active", "is_staff", "is_teacher", "is_manager")
    ordering = ("-created_date",)
    list_display = ("email", "is_active", "is_staff", "is_teacher","is_manager")
    fieldsets = (
        ("Authentication", {"fields": ("email",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_teacher","is_manager")}),
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
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_teacher",
                    "is_manager"
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Profile)
