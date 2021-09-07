from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import ToDo
from .forms import ToDoForm

# Create your views here.


def index_page(request):
    return render(request, 'build/index.html')


def todos(request, pk=None):
    if request.method == "GET":
        todo = ToDo.objects.all().values()
        return JsonResponse({"todo": list(todo)})

    if request.method == "POST":
        form = ToDoForm(request.POST)
        print(request.POST)
        print(f"\n\nform: {form}\n\n")

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return JsonResponse({"code": 1, "todo": todo})
        return JsonResponse({"code": -1, "todo": "Form is not valid"})

    if request.method == "PATCH":
        todo = get_object_or_404(ToDo, pk=pk)
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return JsonResponse({"todo": todo})
        return JsonResponse({"todo": "Form is not valid"})

    if request.method == "DELETE":
        todo = get_object_or_404(ToDo, pk=pk)
        todo.delete()
        return JsonResponse({"todo": "deleted"})
