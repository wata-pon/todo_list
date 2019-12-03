# Create your views here.
from django.views.generic import ListView


class TodoList(ListView):
    template_name = 'list.html'
