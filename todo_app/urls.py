from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]
