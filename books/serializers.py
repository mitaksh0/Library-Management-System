from rest_framework import serializers
from .models import Book
from authors.models import Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_author(self, value):
        if not Author.objects.filter(id=value).exists():
            raise serializers.ValidationError("author not found")
        return value