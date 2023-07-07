from django.urls import path
from .views import TeacherRegisterApiView, ManagerRegisterApiView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("register-manager/", ManagerRegisterApiView.as_view(), name="register-manager"),
    path("register-teacher/", TeacherRegisterApiView.as_view(), name="register-teacher"),
    path("token/login", ObtainAuthToken.as_view(), name="token_obtain"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
]
