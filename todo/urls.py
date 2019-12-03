from django.urls import path

from todo.views import TodoList

urlpatterns = [
    path('list/', TodoList.as_view()),
]
