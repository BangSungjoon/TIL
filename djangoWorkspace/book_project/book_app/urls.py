from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/list/', views.book_list, name='book_list'),
    path('book/detail/<str:bookno>', views.book_detail, name='book_detail'),
    path('book/insert/', views.book_insert, name='book_insert'),
]