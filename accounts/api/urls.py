from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    UserCheckAPIView,
    TeacherRegisterAPIView,
    SupervisorRegisterAPIView,
    ConsultantRegisterAPIView,
    GiveUserIdUpdateAPIView,
    
    )


urlpatterns = [
    #Register API:
    path("user-check/", UserCheckAPIView.as_view(), name = "user-check"),
    path("register-teacher/", TeacherRegisterAPIView.as_view(), name="register-teacher"),
    path("register-supervisor/", SupervisorRegisterAPIView.as_view(), name="register-supervisor"),
    path("register-consultant/", ConsultantRegisterAPIView.as_view(), name="register-consultant"),
    
    #Token API:
    path("token/login/", ObtainAuthToken.as_view(), name="token_obtain"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    
    #ID Assign API::
    path("give-user-id/", GiveUserIdUpdateAPIView.as_view(), name="give-user-id"),
]
