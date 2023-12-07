from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Task


def tasks_list(request: HttpRequest) -> HttpResponse | None:
    # template = loader.get_template("tasks/list.html")
    # return HttpResponse(template.render({"tasks": Task.objects.all()}))
    return render(request, "tasks/list.html", {"tasks": Task.objects.all()})


def task_detail(request: HttpRequest, task_id: int) -> HttpResponse | None:
    # return HttpResponse(loader.get_template("tasks/detail.html").render({"task": Task.objects.get(id=task_id)}))
    return render(request, "tasks/detail.html", {"task": Task.objects.get(id=task_id)})
