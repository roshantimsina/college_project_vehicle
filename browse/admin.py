from django.contrib import admin

# Register your models here.
from .models import Browse,BrowseImage
admin.site.register(Browse),
admin.site.register(BrowseImage)