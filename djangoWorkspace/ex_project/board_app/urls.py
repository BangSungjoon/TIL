from django.urls import path
from . import views

urlpatterns = [
    path('board_list/', views.board_list, name='board_list'),    
    path('board_form/', views.board_form, name='board_form'),     
]