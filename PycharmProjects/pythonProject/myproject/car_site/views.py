from rest_framework import viewsets
from .models import *
from .serializers import *


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers