from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm


def top(request):
    memos = Memo.objects.all().order_by("-id")
    return render(request, "work08/top.html", {"memos": memos})


def new(request):
    memo = Memo.objects.create(title="no title")
    return redirect("work08:edit", pk=memo.pk)


def edit(request, pk):
    memo = get_object_or_404(Memo, pk=pk)

    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect("work08:top")
    else:
        form = MemoForm(instance=memo)

    return render(request, "work08/edit.html", {
        "form": form,
        "memo": memo
          })


def delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    memo.delete()
    return redirect("work08:top")
