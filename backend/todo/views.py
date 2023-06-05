from django.shortcuts import render
#import view sets from the REST framework

from rest_framework import viewsets
#import the TodoSerializer from the serializer file 
from .serializers import TodoSerializers

#import the Todo Model from the models file
from .models import Todo


# Create your views here.
class TodoView(viewsets.ModelViewSet):
    #create  serializer CLASS and
    #assign it to the eTodoSerializer class
    serializer_class = TodoSerializers

    #define a variable and poppulate it
    #with the Todo list objects

    queryset = Todo.objects.all()
