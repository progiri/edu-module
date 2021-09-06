from django.shortcuts import get_object_or_404, render, redirect
from .models import ToDo
from .forms import ToDoForm

# Create your views here.
def index_page(request):
    return render(request, 'todo/index.html')

# todo 
'''
мында get, post, put, patch, delete запростарға бөлек жағдай(if), қайтару керек JsonResponse();
'''

def todo_add(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
    else:
        form = ToDoForm()
    return render(request, 'todo/todo_add.html', {"form": form})


def todo_edit(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos')
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {"form": form})


def todo_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect('todos')


