from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit  import UpdateView
from .models import TodoApp

class TodoAppCreateView(CreateView):
    model = TodoApp
    fields = [
        "title"
        "description"
    ]
    template_name = "home.html"
    success_url =  "list.html"

class TodoAppListView(ListView):
    model = TodoApp
    template_name = "list.html"

class TodoAppDetailView(DetailView):
    model = TodoApp
    template_name = "detail.html"

class TodoAppUpdateView(UpdateView):
    model = TodoApp

    fields = [
        "title",
        "description"
    ]
    template_name = "update.html"
    success_url = "/"

