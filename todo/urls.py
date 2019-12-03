from django.urls import path

from todo.views import todolist

urlpatterns = [
    path('todo', todolist),
]
