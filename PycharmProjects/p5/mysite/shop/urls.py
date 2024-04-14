from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductViewSets.as_view({'get': 'list',
                                      'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductViewSets.as_view({'get': 'retrieve',
                                               'post': 'update',
                                               'delete': 'destroy'}), name='product_detail'),
    path('category/', CategoryViewSets.as_view({'get': 'list',
                                      'post': 'create'}), name='product_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve',
                                               'post': 'update',
                                               'delete': 'destroy'}), name='product_detail')
]