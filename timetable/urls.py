from django.urls import path, include

app_name = "timetable"

urlpatterns = [

    path("api/", include("timetable.api.urls"))
]
