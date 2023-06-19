from django.urls import path
from .views import TeacherAssignModelViewSet
from rest_framework.routers import DefaultRouter

# app_name = 'api1'
# router = DefaultRouter()
# router.register("teacher-assign", TeacherAssignModelViewSet, basename="teacher-assign")
# urlpatterns = router.urls
urlpatterns = [
    path("assign-teacher/", TeacherAssignModelViewSet.as_view({'get':'list'}), name="assign-teacher"),

]