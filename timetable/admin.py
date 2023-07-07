from django.contrib import admin
from .models import Section


class SectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["section_id", "iranian_time", "day","teachers",]
    list_filter = ("section_id", "iranian_time", "day", "teachers",)
    list_display = ("section_id", "iranian_time", "day",)
    add_fieldsets = ("iranian_time", "day",)
    
    
# Register your models here.
#admin.site.register(TeachingTime)
admin.site.register(Section,SectionAdminConfig)