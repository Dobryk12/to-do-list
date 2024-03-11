from django.contrib import admin
from django.urls import path, include
from list.views import index, TagListView, TagsCreateView, TagsUpdateView, TagsDeleteView, TasksCreateView, \
    TasksDeleteView, TasksUpdateViewFull, TasksUpdateViewFull, TasksUpdateViewStatus

urlpatterns =[
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagsCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagsUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagsDeleteView.as_view(), name="tag-delete"),
    path("tasks/create", TasksCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/delete", TasksDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/update/staus", TasksUpdateViewStatus.as_view(), name="task-update-status"),
    path("tasks/<int:pk>/update/", TasksUpdateViewFull.as_view(), name="task-update"),
]
