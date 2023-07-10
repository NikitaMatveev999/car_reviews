from django.contrib import admin
from .models import Car, Manufacturer, Comment, Country

admin.site.register(Car)
admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(Comment)
