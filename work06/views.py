from django.shortcuts import render
from .forms import ReiwaForm


def top(request):
    return render(request, "top.html")


def reiwa(request):
    result = None

    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["reiwa_year"]
            result = reiwa_year + 2018
    else:
        form = ReiwaForm()

    return render(
        request,
        "reiwa.html",
        {
            "form": form,
            "result": result,
        },
    )
