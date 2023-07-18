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
    )

# router = DefaultRouter()
# router.register(r'assign-teacher', TeacherAssignModelViewSet, basename='assign-teacher')

# urlpatterns = router.urls
urlpatterns = [
    path("teacher-free-section-adjust/", TeacherFreeSectionAdjustAPIView.as_view(
        {'post':'create','delete':'destroy'}), 
         name="teacher-free-section-register"),
    path("teacher-section-adjust/", TeacherSectionAdjustAPIView.as_view(
        {'post':'create'}),
         name="teacher-section-register"),
    
    #Section Lists:
    path("section-list/<str:teacher_email>/", SectionListAPIView.as_view(), name="section-list"),
    path("free-section-list/<str:teacher_email>/", FreeSectionListAPIView.as_view(), name="free-section-list"),
    
    #Teacher lists based on a section
    path("teacher-list-section/<str:day>/<str:iranian_time>/", TeacherListSectionListAPIView.as_view(), name="teacher-list-section"),
    path("teacher-list-free-section/<str:day>/<str:iranian_time>/", TeacherListFreeSectionListAPIView.as_view(), name="teacher-list-free-section"),
    
    #Section Creators:
    path("section-creator/", CreateSectionsAPIView.as_view(), name="section-creator"),
    path("free-section-creator/", CreateFreeSectionsAPIView.as_view(), name="free-section-creator"),
]