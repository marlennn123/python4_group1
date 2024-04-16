from .views import *
from django.urls import path

urlpatterns = [
    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>', CategoryViewSets.as_view({'get': 'retrieve',
                                                        'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),
path('product/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('product/<int:pk>', ProductViewSets.as_view({'get': 'retrieve',
                                                        'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),
]