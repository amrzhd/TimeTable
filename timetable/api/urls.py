from django.urls import path
from .views import (
    CreateSectionsAPIView,
    CreateFreeSectionsAPIView,
    TeacherSectionRegisterAPIView
    )

# router = DefaultRouter()
# router.register(r'assign-teacher', TeacherAssignModelViewSet, basename='assign-teacher')

# urlpatterns = router.urls
urlpatterns = [
    path("teacher-section-register/", TeacherSectionRegisterAPIView.as_view({'post':'create'}), name="teacher-section-register"), #list
    path("section-creator/", CreateSectionsAPIView.as_view(), name="section-creator"),
    path("free-section-creator/", CreateFreeSectionsAPIView.as_view(), name="section-creator"),
]