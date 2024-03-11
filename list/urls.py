from django.urls import path
from list.views import (
    TaskListView,
    TagListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
    TasksCreateView,
    TasksDeleteView,
    TasksUpdateView,
    change_task_status
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagsCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagsUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagsDeleteView.as_view(), name="tag-delete"),
    path("tasks/create", TasksCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/delete", TasksDeleteView.as_view(), name="task-delete"),
    path("change_task_status/<int:pk>/", change_task_status, name="task-update-status"),
    path("tasks/<int:pk>/update/", TasksUpdateView.as_view(), name="task-update"),
]
