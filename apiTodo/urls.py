from django.urls import path, include
from .views import home, todoList, todoListCreate,todo_List, todoListUpdate, todoListDelete, todo_detail, TodoList, ToDetail, TodoListCreate, TodoRetrieveUpdateDelete, TodoConcListCreate, TodoConcRetrieveUpdateDelete, TodoVsListRetrieve, TodoMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todovs-list', TodoVsListRetrieve)
router.register('todomvs-list', TodoMVS)

urlpatterns = [
    path('', home),
    path('todoList/', todoList),
    path('todoListCreate/', todoListCreate),
    path('todo_List/', todo_List),
    path('todoListUpdate/<int:pk>', todoListUpdate),
    path('todoListDelete/<int:pk>', todoListDelete),
    path('todo_detail/<int:pk>', todo_detail),
    #class_base 
    path('classtodolist/', TodoList.as_view()),
    path('classtododetail/<int:pk>', ToDetail.as_view()),
    path('classtodolistcreate/<int:pk>', TodoListCreate.as_view()),
    path('classtodoretrieve/<int:pk>', TodoRetrieveUpdateDelete.as_view()),
    path('TodoConcListCreate/', TodoConcListCreate.as_view()),
    path('TodoConcRetrieve/<int:pk>', TodoConcRetrieveUpdateDelete.as_view()),
    path('', include(router.urls)),
]