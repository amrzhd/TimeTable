from django.urls import path
from .views import (
    CreateSectionsAPIView,
    TeacherSetFreeSectionAPIView,
    SectionListAPIView,
    FreeSectionListAPIView,
    TeacherListSectionListAPIView,
    TeacherListFreeSectionListAPIView,
    SetClassUpdateAPIView,
    AddFreeSectionsToSectionsCreateAPIView,
    ConsultantSetFreeSectionAPIView,
    TeacherFreeSectionListAPIView,
    )

urlpatterns = [
    
    #Teacher Set Free section
    path("teacher-set-free-section/", TeacherSetFreeSectionAPIView.as_view(), name="teacher-set-free-section"),
    path("consultant-set-free-section/", ConsultantSetFreeSectionAPIView.as_view(), name="consultant-set-free-section"),
    
    #Section Lists:
    path("section-list/<str:teacher_id>/", SectionListAPIView.as_view(), name="section-list"),
    path("free-section-list/<str:teacher_id>/", FreeSectionListAPIView.as_view(), name="free-section-list"),
    path("teacher-free-section-list/", TeacherFreeSectionListAPIView.as_view(), name="teacher-free-section-list"),
    #Teacher lists based on a section
    path("teacher-list-section/<str:day>/<str:iranian_time>/", TeacherListSectionListAPIView.as_view(), name="teacher-list-section"),
    path("teacher-list-free-section/<str:day>/<str:iranian_time>/", 
         TeacherListFreeSectionListAPIView.as_view(), name="teacher-list-free-section"),
    
    #Class:
    path("set-class/", SetClassUpdateAPIView.as_view(), name="set-class"),
    
    #Adding Free Sections to Section:
    path("add-free-section-to-section/", AddFreeSectionsToSectionsCreateAPIView.as_view(), name = "add-free-section-to-section"),
    
    #Section Creators:
    path("section-creator/", CreateSectionsAPIView.as_view(), name="section-creator"),
]