from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index_page, name='index_page'), # index page
    
    path('todos/', views.todos, name='todo'),
    path('api/v1/todos/', views.Todos.as_view(), name='api_todo'),
    path('api/v1/todos/<int:pk>/', views.ToDoDetail.as_view(), name='api_todo_detail')
]

router = routers.SimpleRouter()
router.register('api/v2/todos', views.ToDoViewSet)

urlpatterns += router.urls
