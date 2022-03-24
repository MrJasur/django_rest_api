from rest_framework import serializers
from books.models import Books

class Bookserializer(serializers.ModelSerializer):
    class Meta:   #meros olyabdi
        model = Books
        fields = ('title', 'subtitle', 'author', 'isbn')