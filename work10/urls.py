from django.urls import path
from . import views

app_name = "work10"

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
]

