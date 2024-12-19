from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET', 'POST'])
def manage_books(request):

    if request.method == 'GET':
        # DO GET STUFF
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # DO POST STUFF
        if isinstance(request.data, list):
            serializer = BookSerializer(data=request.data, many=True)
        else:
            serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, 201)
    
@api_view(['GET', 'PUT', 'DELETE'])
def manage_book_id(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        book.delete()
        return Response(
            {"message": "book successfully deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )
