from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_view),
    path('show/', views.show_book_view),
    path('add/', views.add_book_view),
    path('update/<int:i>/', views.update_book_view),
    path('delete/<int:i>/', views.delete_book_view),
    path('author/<str:author_name>/', views.books_by_author_view, name='books-by-author'),
]
