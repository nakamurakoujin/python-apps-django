from django.urls import path
from . import views

app_name = "work08"

urlpatterns = [
    path("", views.top, name="top"),
    path("new/", views.new, name="new"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
