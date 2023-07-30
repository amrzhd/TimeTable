from django.contrib import admin
from .models import (
    Section,
    Class,
    SectionTeacher,
    FreeSectionTeacher
)


class SectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["iranian_time", "day", "chinese_time", "month","year", ]
    list_filter = ("iranian_time", "day", "chinese_time", "month","year", )
    list_display = ("iranian_time", "day", "chinese_time", "month", "year", )
    add_fieldsets = ("iranian_time", "day", "chinese_time", "month","year", )    

admin.site.register(Section, SectionAdminConfig)

class ClassAdminConfig(admin.ModelAdmin):
    model = Class
    search_fields = ["student_name", "session", "platform",]
    list_filter = ("student_name", "session", "platform",)
    list_display = ("student_name", "session", "platform",)
    add_fieldsets = ("student_name", "session","platform",)    

admin.site.register(Class, ClassAdminConfig)

class SectionTeacherAdminConfig(admin.ModelAdmin):
    model = SectionTeacher
    search_fields = ["teacher", "section", "section_class", ]
    list_filter = ("teacher", "section", "section_class", )
    list_display = ("teacher", "section", "section_class", )
    add_fieldsets = ("teacher", "section", "section_class", )

admin.site.register(SectionTeacher, SectionTeacherAdminConfig)


class FreeSectionTeacherAdminConfig(admin.ModelAdmin):
    model = FreeSectionTeacher
    search_fields = ["teacher", "free_section", "free_section_class", ]
    list_filter = ("teacher", "free_section", "free_section_class", )
    list_display = ("teacher", "free_section", "free_section_class", )
    add_fieldsets = ("teacher", "free_section", "free_section_class", )

admin.site.register(FreeSectionTeacher, FreeSectionTeacherAdminConfig)

