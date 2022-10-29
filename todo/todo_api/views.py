from django.shortcuts import render
from rest_framework import viewsets
from todo_api.models import Todo
from todo_api.serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
  serializer_class = TodoSerializer
  queryset = Todo.objects.all()