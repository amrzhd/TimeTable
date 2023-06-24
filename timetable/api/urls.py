from django.urls import path
from .views import TeacherAssignListCreateAPIView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'assign-teacher', TeacherAssignModelViewSet, basename='assign-teacher')

# urlpatterns = router.urls
urlpatterns = [
    path("assign-teacher/", TeacherAssignListCreateAPIView.as_view(), name="assign-teacher-create"), #post and list

]