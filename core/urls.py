"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from decouple import config



urlpatterns = [
    #admin panel
    path("admin/", admin.site.urls),
    # accounts app
    path("accounts/", include("accounts.urls")),
    # timetable app
    path("timetable/", include("timetable.urls")),
    # api authentication 
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # api doc app
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/",SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui"),
    path("api/schema/redoc/",SpectacularRedocView.as_view(url_name="schema"),name="redoc"),
    #silk
    path(f"{config('SILK_URL', default='silk')}/", include('silk.urls', namespace='silk')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
