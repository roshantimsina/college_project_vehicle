from django.contrib import admin

# Register your models here.
from .models import Vehicle,Route
admin.site.register(Vehicle)
admin.site.register(Route)

