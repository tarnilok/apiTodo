from django.urls import path
from .views import home, todoList, todoListCreate,todo_List, todoListUpdate, todoListDelete, todo_detail

urlpatterns = [
    path('', home),
    path('todoList/', todoList),
    path('todoListCreate/', todoListCreate),
    path('todo_List/', todo_List),
    path('todoListUpdate/<int:pk>', todoListUpdate),
    path('todoListDelete/<int:pk>', todoListDelete),
    path('todo_detail/<int:pk>', todo_detail),
]