from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.manage_authors, name="authors_details"),
    path('authors/<int:id>/', views.manage_author_id, name="author_details"),
    path('', views.index_page)
]