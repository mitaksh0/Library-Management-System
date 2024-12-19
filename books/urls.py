from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.manage_books, name="books_details"),
    path('books/<int:id>', views.manage_book_id, name="book_details"),
]