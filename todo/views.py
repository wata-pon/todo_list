# Create your views here.
from django.views.generic import ListView, DetailView

from .models import TodoModel


class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'Detail.html'
    model = TodoModel
