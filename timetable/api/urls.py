from django.urls import path
from .views import (
    CreateSectionsAPIView,
    CreateFreeSectionsAPIView,
    TeacherFreeSectionAdjustAPIView,
    TeacherSectionAdjustAPIView,
    SectionListAPIView,
    FreeSectionListAPIView,
    TeacherListSectionListAPIView,
    TeacherListFreeSectionListAPIView,
    SetClassUpdateAPIView,
    AddFreeSectionsToSectionsCreateAPIView,
    )

urlpatterns = [
    path("teacher-free-section-adjust/", TeacherFreeSectionAdjustAPIView.as_view(
        {'post':'create','delete':'destroy'}), 
         name="teacher-free-section-adjust"),
    path("teacher-section-adjust/", TeacherSectionAdjustAPIView.as_view(
        {'post':'create'}),
         name="teacher-section-adjust"),
    
    #Section Lists:
    path("section-list/<str:teacher_email>/", SectionListAPIView.as_view(), name="section-list"),
    path("free-section-list/<str:teacher_email>/", FreeSectionListAPIView.as_view(), name="free-section-list"),
    
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
    path("free-section-creator/", CreateFreeSectionsAPIView.as_view(), name="free-section-creator"),
]