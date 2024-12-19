from django.urls import path
from . import views

urlpatterns = [
    path('borrow/', views.borrow_book),
    path('borrow/<int:id>/return/', views.return_borrow),
]