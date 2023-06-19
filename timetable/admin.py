from django.contrib import admin
from .models import Section


class SectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["iranian_time", "day", "teacher",]
    list_filter = ("iranian_time", "day", "teacher",)
    list_display = ("iranian_time", "day", "teacher",)
    add_fieldsets = ("iranian_time", "day", "teacher",)
    
    
# Register your models here.
#admin.site.register(TeachingTime)
admin.site.register(Section,SectionAdminConfig)