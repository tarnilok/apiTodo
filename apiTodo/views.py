from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>')
