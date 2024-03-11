from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from list.forms import TagForm, TaskForm
from list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'


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


class TasksCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('list:task-list')


class TasksDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('list:task-list')


class TasksUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm


def change_task_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return HttpResponseRedirect(reverse_lazy('list:task-list'))
