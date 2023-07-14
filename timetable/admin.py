from django.contrib import admin
from .models import Section, FreeSection, SectionTeacher


class SectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["section_id", "iranian_time", "day"]
    list_filter = ("section_id", "iranian_time", "day", )
    list_display = ("section_id", "iranian_time", "day",)
    add_fieldsets = ("iranian_time", "day",)

class FreeSectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["section_id", "iranian_time", "day"]
    list_filter = ("section_id", "iranian_time", "day", )
    list_display = ("section_id", "iranian_time", "day",)
    add_fieldsets = ("iranian_time", "day",)    
    
class SectionTeacherAdminConfig(admin.ModelAdmin):
    model = SectionTeacher
    search_fields = ["user", "section", "free_section"]
    list_filter = ("user", )
    list_display = ("user", "section", "free_section")
    add_fieldsets = ("user", "section", "free_section")   

admin.site.register(Section,SectionAdminConfig)
admin.site.register(FreeSection,FreeSectionAdminConfig)
admin.site.register(SectionTeacher,SectionTeacherAdminConfig)
