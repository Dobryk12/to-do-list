from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from list.forms import TagForm
from list.models import Task, Tag


def index(request) -> HttpResponse:
    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        'tasks': tasks,
        'tags': tags
    }

    return render(request,"list/index.html",context)


class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tag_list'


class TagsCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('list:tags-list')


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('list:tags-list')


class TagsUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('list:tags-list')

