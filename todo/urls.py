from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'), # index page

    # мында тек todo или todos 
    path('todo/add/', views.todo_add, name='todo_add'), # create new todo
    path('todo/<int:pk>/edit/', views.todo_edit, name='todo_edit'), # edit todo
    path('todp/<int:pk>/delete/', views.todo_delete, name='todo_delete')
]
