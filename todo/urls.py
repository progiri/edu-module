from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo_list'), # index page
    path('todo/add/', views.todo_add, name='todo_add'), # create new todo
    path('todo/<int:pk>/edit/', views.todo_edit, name='todo_edit'), # edit todo
    path('todp/<int:pk>/delete/', views.todo_delete, name='todo_delete')
]
