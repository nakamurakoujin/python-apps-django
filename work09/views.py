from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("todo_list")


def todo_list(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.description = ""
            todo.is_completed = False
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm()

    todos = Todo.objects.all().order_by("-created_at")

    return render(request, "work09/todo_list.html", {
        "todos": todos,
        "form": form
    })


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.description = todo.description or ""
            todo.is_completed = "is_completed" in request.POST
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)

    return render(request, "work09/todo_edit.html", {
        "form": form,
        "todo": todo
    })
