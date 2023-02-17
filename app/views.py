from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.models import Tag, Task


def index(request):
    """View function for the home page of the site."""

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_visits": num_visits + 1,

    }

    return render(request, "app/index.html", context=context)

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:index")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("app:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "app/tag_list.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:index")
