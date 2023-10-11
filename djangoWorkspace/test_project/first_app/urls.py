from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('img/', views.show_img, name='show_img'),
    # http://127.0.0.1:8000/img/
    path('data_form/', views.data_form, name='data_form'),
    path('data_form2/', views.data_form2, name='data_form2')
]