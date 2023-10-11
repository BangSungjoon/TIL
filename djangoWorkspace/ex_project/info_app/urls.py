from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('board_app/board_list/', views.board_list, name='board_list'),
]