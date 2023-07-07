from django.urls import path
from .views import SectionsListAPIView, TeacherSectionsListAPIView, AddTeachersToSectionAPIView, SectionDetailView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'assign-teacher', TeacherAssignModelViewSet, basename='assign-teacher')

# urlpatterns = router.urls
urlpatterns = [
    path("sections/", SectionsListAPIView.as_view(), name="sections-list"),
    path("teacher-section-list/", TeacherSectionsListAPIView.as_view(), name="teacher-section-list"), #list
    path("sections/<int:pk>/add-teachers/", AddTeachersToSectionAPIView.as_view(), name="add-teachers-to-section"),
    path("section-detail/<int:pk>/", SectionDetailView.as_view(), name="section-detail"),
    #path("section-creator/", CreateSectionsAPIView.as_view(), name="section-creator"),
 
]