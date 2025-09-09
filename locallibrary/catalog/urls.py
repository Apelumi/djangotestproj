from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', views.index, name = "index"),
    path('books/', views.BookListView.as_view(), name = "books"),
    path('books/<int:pk>', views.book_detail_view, name = "book_detail")
]