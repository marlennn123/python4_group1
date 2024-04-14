from django.urls import path
from .views import *

urlpatterns = [
    path('', car_list, name='car_list'),
    path('<int:pk>/', car_detail, name='car_detail'),
    path('create/', car_create, name='car_create'),
    path('<int:pk>/update/', car_update, name='car_update'),
    path('<int:pk>/delete/', car_delete, name='car_delete'),
]