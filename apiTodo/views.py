from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status

############ class based ##########
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet


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

@api_view(['DELETE', 'PUT', 'GET', 'POST'])
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
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
############### API View ###############

class TodoList(APIView):
    def get(self, request):   # ismi get olmalı
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request): # ismi post olmalı 
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ToDetail(APIView):
    def get_objectt(self, pk):
        return get_object_or_404(Todo, pk=pk)
    
    def get(self, request, pk):
        todo = self.get_objectt(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        todo = self.get_objectt(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            serializer._data["success"] = "Todo succesfully updated.." # underscore protected datayı değiştirmeyi sağlıyor.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = self.get_objectt(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request): # ismi post olmalı 
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
############### GenericAPI View ###############

class TodoListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class TodoRetrieveUpdateDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
############### Concrete View ###############

class TodoConcListCreate(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class TodoConcRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
############### Viewsets ###############
#Viewset GenericViewSet ModelViewSet

class TodoVsListRetrieve(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False, methods=['get'])
    def todo_count(self, request):
        todo_count = Todo.objects.filter(is_done=False).count()
        count = {
            'undo-todos' : todo_count
        }
        return Response(count)

    

    
        



