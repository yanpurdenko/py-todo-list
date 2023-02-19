from django.conf.urls.static import static
from django.urls import path

from todo import settings
from app.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    complete_task,
    undo_task,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/<int:pk>/complete/", complete_task, name="complete-task"),
    path("tags/<int:pk>/undo/", undo_task, name="undo-task"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


app_name = "app"
