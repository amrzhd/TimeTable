from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ("email","teacher_id")
    list_filter = ("email", "is_active", "is_staff", "is_teacher", "is_manager", "teacher_id")
    ordering = ("-created_date",)
    list_display = ("email", "is_active", "is_staff", "is_teacher","is_manager", "teacher_id")
    fieldsets = (
        ("Authentication", {"fields": ("email","teacher_id")}),
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
                    "is_manager",
                    "teacher_id",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
