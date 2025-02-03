from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/',
         views.product_detail,
         name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:product_id>/update/',
         views.product_update,
         name='product_update'),
    path('product/<int:product_id>/delete/',
         views.product_delete,
         name='product_delete'),
]
