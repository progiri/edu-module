import json

from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import ToDo
from .forms import ToDoForm
from .serializers import ToDoSerializer

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
            todo = form.save()
            return JsonResponse({"code": 1, "todo": {"title": todo.title, "status": todo.status, "id": todo.id}})

        return JsonResponse({"code": -1, "todo": "Form is not valid"})

    if request.method == "PATCH":
        data = json.loads(request.body.decode())
        
        todo = get_object_or_404(ToDo, pk=data["id"])
        todo.status = data["status"]
        todo.save() 

        return JsonResponse({"code": 1, "todo": {"title": todo.title, "status": todo.status, "id": todo.id}})
    
        

    if request.method == "DELETE":
        data = json.loads(request.body.decode())
        todo = get_object_or_404(ToDo, pk=data["id"])
        todo.delete()
        return JsonResponse({"todo": "deleted"})

class Todos(views.APIView):
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        print(serializer.data)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetail(views.APIView):
    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
 