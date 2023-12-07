from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import User


def user_list(request: HttpRequest) -> HttpResponse | None:
    # template = loader.get_template("users/list.html")
    try:
        # return HttpResponse(template.render({"users": User.objects.all()}))
        return render(request, "users/list.html", {"users": User.objects.all()})
    except Exception as e:
        # return HttpResponse(template.render({"error_message": f"Error: {e}"}))
        return render(request, "users/list.html", {"error_message": f"Error: {e}"})


def user_detail(request: HttpRequest, user_id: int) -> HttpResponse | None:
    # return HttpResponse(loader.get_template("users/detail.html").render({"user": User.objects.get(id=user_id)}))
    return render(request, "users/detail.html", {"user": User.objects.get(id=user_id)})
