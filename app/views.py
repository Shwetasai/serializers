from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book,Author
from .serializers import (BookModelSerializer,BookBulkSerializer,BookNestedAuthorSerializer,BookPlainSerializer,AuthorSerializer)

@api_view(['GET', 'POST'])
def book_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def author_list_create(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET', 'POST'])
def book_plain_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookPlainSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookPlainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def bulk_create_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookBulkSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookBulkSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def create_book_with_nested_author(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookNestedAuthorSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookNestedAuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


