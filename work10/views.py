from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm


@login_required
def todo_list(request):
    # ログイン中ユーザーのTODOだけ取得
    todos = Todo.objects.filter(user=request.user).order_by("due_date")

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user   # ← 超重要！！
            todo.save()
            return redirect("work10:todo_list")
    else:
        form = TodoForm()

    return render(request, "work10/todo_list.html", {
        "todos": todos,
        "form": form,
    })
