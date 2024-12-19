from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AuthorSerializer
from .models import Author
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def manage_authors(request):
    
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, 201)
    
@api_view(['GET', 'PUT', 'DELETE'])
def manage_author_id(request, id):    
    author = get_object_or_404(Author, id=id)
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        author.delete()
        return Response(
            {"message": "author successfully deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )

@api_view(['GET'])
def index_page(request):
    return Response({
        "message": "Welcome to Library Management System! Please go to /docs for usage."
    })