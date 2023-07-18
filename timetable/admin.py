from django.contrib import admin
from .models import Section, FreeSection, SectionTeacher, FreeSectionTeacher


class SectionAdminConfig(admin.ModelAdmin):
    model = Section

    # def display_chinese_time(self, obj):
    #     return obj.chinese_time

    search_fields = ["section_id", "iranian_time", "day", "chinese_time"]
    list_filter = ("section_id", "iranian_time", "day")
    list_display = ("section_id", "iranian_time",)

admin.site.register(Section, SectionAdminConfig)


class FreeSectionAdminConfig(admin.ModelAdmin):
    model = Section
    search_fields = ["section_id", "iranian_time", "day",]
    list_filter = ("section_id", "iranian_time", "day", )
    list_display = ("section_id", "iranian_time", "day",)
    add_fieldsets = ("iranian_time", "day",)    

admin.site.register(FreeSection, FreeSectionAdminConfig)

class SectionTeacherAdminConfig(admin.ModelAdmin):
    model = SectionTeacher
    search_fields = ["teacher", "section",]
    list_filter = ("teacher", "section",)
    list_display = ("teacher", "section", )
    add_fieldsets = ("teacher", "section", )

admin.site.register(SectionTeacher, SectionTeacherAdminConfig)


class FreeSectionTeacherAdminConfig(admin.ModelAdmin):
    model = FreeSectionTeacher
    search_fields = ["teacher", "free_section"]
    list_filter = ("teacher", "free_section")
    list_display = ("teacher", "free_section", )
    add_fieldsets = ("teacher", "free_section", )

admin.site.register(FreeSectionTeacher, FreeSectionTeacherAdminConfig)

