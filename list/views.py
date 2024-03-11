from django.http import HttpResponse
from django.shortcuts import render

from list.models import Task, Tag


def index(request, HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        'tasks': tasks,
        'tags': tags
    }

    return render(request,"list/index.html",context)


