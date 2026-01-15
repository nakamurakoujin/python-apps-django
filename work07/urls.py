from django.urls import path
from . import views

app_name = "work07"

urlpatterns = [
    path("", views.top, name="top"),
    path("omikuji/", views.omikuji, name="omikuji"),
]
