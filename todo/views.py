from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import ToDo
from .forms import ToDoForm

import json

# Create your views here.


def index_page(request):
    return render(request, 'build/index.html')


def todos(request, pk=None):
    if request.method == "GET":
        todo = ToDo.objects.all().values()
        return JsonResponse({"todo": list(todo)})

    if request.method == "POST":
        data = json.loads(request.body.decode())

        form = ToDoForm(data)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return JsonResponse({"code": 1, "todo": {"title": todo.title, "status": todo.status, "id": todo.id}})

        return JsonResponse({"code": -1, "todo": "Form is not valid"})

    if request.method == "PATCH":
        data = json.loads(request.body.decode())

        todo = get_object_or_404(ToDo, pk=data["id"])
        # form = ToDoForm(data, instance=todo)

        # if form.is_valid():
        #     todo = form.save(commit=False)

        todo.status = data["status"]

        todo.save()
        return JsonResponse({"code": 1, "todo": {"title": todo.title, "status": todo.status, "id": todo.id}})
        # return JsonResponse({"todo": "Form is not valid"})

    if request.method == "DELETE":
        data = json.loads(request.body.decode())

        todo = get_object_or_404(ToDo, pk=data["id"])
        todo.delete()

        return JsonResponse({"todo": "deleted"})
