from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'), # index page

    # мында тек todo или todos 
    path('todos/', views.todos, name='todo')
]
