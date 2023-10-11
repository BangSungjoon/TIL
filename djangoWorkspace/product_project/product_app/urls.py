from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/list/', views.product_list, name='product_list'),
    # http://127.0.0.1:8000/product/list/ : 주소줄에 표시
    path('product/detail/<str:prd_no>', views.product_detail, name='product_detail'),
    # <str:prd_no> : 매개변수  
    path('product/insert/', views.product_insert, name='product_insert'),
    path('product/update/<str:prd_no>', views.product_update, name='product_update'),
    path('product/delete/<str:prd_no>', views.product_delete, name='product_delete'),
]