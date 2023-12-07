from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse | None:
    # return HttpResponse(loader.get_template("index.html").render())
    return render(request, "index.html")
