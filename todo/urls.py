from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'), # index page
    
    path('todos/', views.todos, name='todo')
]
