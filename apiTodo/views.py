from django.http.response import HttpResponse
from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>')


@api_view(['GET'])
def todoList(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def todoListCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def todo_List(request):
    if request.method == 'GET':
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def todoListUpdate(request, pk):
    queryset = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=queryset, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def todoListDelete(request, pk):
    queryset = Todo.objects.get(id=pk)
    queryset.delete()
    return Response('Item Deleted')

@api_view(['DELETE', 'PUT', 'GET'])
def todo_detail(request, pk):
    queryset = Todo.objects.get(id=pk)
    if request.method == 'GET':
        serializer = TodoSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(instance=queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    
        



