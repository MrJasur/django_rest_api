from django.shortcuts import render
from rest_framework import generics #new
from books.models import Books
from .serializers import Bookserializer #new

# Create your views here.
class BookApiView(generics.ListAPIView):
    queryset = Books.objects.all() #barchasini bir joyga yigib beradi
    serializer_class = Bookserializer