from django.urls import path
from .views import *

urlpatterns = [
    path('', StoreViewSet.as_view({'get': 'list'}), name='store_list'),
    path('<int:pk>/', StoreViewSet.as_view({'get': 'list'}), name='store_list'),
]
