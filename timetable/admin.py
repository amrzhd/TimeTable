from django.contrib import admin
from .models import Section, FreeSection, SectionTeacher, FreeSectionTeacher


class SectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["section_id", "iranian_time", "day", "chinese_time"]
    list_filter = ("section_id", "iranian_time", "day", "chinese_time")
    list_display = ("section_id", "iranian_time", "day", "chinese_time")
    add_fieldsets = ("iranian_time", "day", "chinese_time")    

admin.site.register(Section, SectionAdminConfig)


class FreeSectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["section_id", "iranian_time", "day", "chinese_time"]
    list_filter = ("section_id", "iranian_time", "day", "chinese_time")
    list_display = ("section_id", "iranian_time", "day", "chinese_time")
    add_fieldsets = ("iranian_time", "day", "chinese_time")    

admin.site.register(FreeSection, FreeSectionAdminConfig)

class SectionTeacherAdminConfig(admin.ModelAdmin):
    model = SectionTeacher
    search_fields = ["teacher", "section","student",]
    list_filter = ("teacher", "section", "student",)
    list_display = ("teacher", "section", "student",)
    add_fieldsets = ("teacher", "section", "student",)

admin.site.register(SectionTeacher, SectionTeacherAdminConfig)


class FreeSectionTeacherAdminConfig(admin.ModelAdmin):
    model = FreeSectionTeacher
    search_fields = ["teacher", "free_section", "student",]
    list_filter = ("teacher", "free_section", "student",)
    list_display = ("teacher", "free_section", "student",)
    add_fieldsets = ("teacher", "free_section", "student",)

admin.site.register(FreeSectionTeacher, FreeSectionTeacherAdminConfig)

