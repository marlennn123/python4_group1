from django.contrib import admin

from .models import *


admin.site.register(Marca)
admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(CarPhoto)
admin.site.register(Model)