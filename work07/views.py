import random
from django.shortcuts import render


def top(request):
    return render(request, "work07/top.html")


def omikuji(request):
    result = None

    if request.method == "POST":
        omikuji_list = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]
        result = random.choice(omikuji_list)

    return render(request, "work07/omikuji.html", {
        "result": result
    })


# Create your views here.
