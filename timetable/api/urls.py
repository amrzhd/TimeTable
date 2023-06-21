from django.urls import path
from .views import TeacherAssignModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'assign-teacher', TeacherAssignModelViewSet, basename='assign-teacher')

urlpatterns = router.urls
# urlpatterns = [
#     path("assign-teacher/", TeacherAssignModelViewSet.as_view({'put':'create'}), name="assign-teacher"),

# ]