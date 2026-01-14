from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("reiwa/", views.reiwa, name="reiwa"),
]
