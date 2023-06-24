from django.contrib import admin
from .models import Section


class SectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["iranian_time", "day","teachers",]
    list_filter = ("iranian_time", "day", "teachers",)
    list_display = ("iranian_time", "day",)
    add_fieldsets = ("iranian_time", "day",)
    
    
# Register your models here.
#admin.site.register(TeachingTime)
admin.site.register(Section,SectionAdminConfig)