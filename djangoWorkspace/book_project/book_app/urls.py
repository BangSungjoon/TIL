from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/list/', views.book_list, name='book_list'),
    path('book/detail/<str:bookno>', views.book_detail, name='book_detail'),
    path('book/insert/', views.book_insert, name='book_insert'),
    path('book/update/<str:bookno>', views.book_update, name='book_update'),

    path('book/search_form/', views.book_search_form, name='book_search_form'),
    path('book/search/', views.book_search, name='book_search'),
]