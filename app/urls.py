from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list_create),
    path('books/bulk/', views.bulk_create_books),
    path('books/nested/', views.create_book_with_nested_author),
    path('books/plain/', views.book_plain_list_create),
    path('authors/', views.author_list_create),
    

]
