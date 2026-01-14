from django.http import render


def index(request):
    # htmlを返す
    return render(request, "work05/templeates/index.html")
