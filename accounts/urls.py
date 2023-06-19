from django.urls import path, include

app_name = "accounts"

urlpatterns = [
    # template base authentication
    # path('', include('django.contrib.auth.urls')),
    # api based authentication
    path("api/", include("accounts.api.urls")),
]
