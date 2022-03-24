from django.shortcuts import render
from .models import Todo
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import TodoSerializers

# Create your views here.
class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers