from django.urls import path
from .views import (
    TeacherRegisterAPIView,
    SupervisorRegisterAPIView,
    ConsultantRegisterAPIView,
    GiveTeacherIdUpdateAPIView,
    )
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    #Register API:
    path("register-teacher/", TeacherRegisterAPIView.as_view(), name="register-teacher"),
    path("register-supervisor/", SupervisorRegisterAPIView.as_view(), name="register-supervisor"),
    path("register-consultant/", ConsultantRegisterAPIView.as_view(), name="register-consultant"),
    
    #ID Assign api:
    path("give-teacher-id/", GiveTeacherIdUpdateAPIView.as_view(), name="teacher-id-assign"),
    path("token/login/", ObtainAuthToken.as_view(), name="token_obtain"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
]
