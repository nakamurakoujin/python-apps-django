from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "due_date"]
        labels = {
            "title": "タイトル",
            "due_date": "期限日",
        }
