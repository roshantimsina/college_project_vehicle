from __future__ import unicode_literals

from django.db import models
from location.fields import GeopositionField


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    position = GeopositionField(blank=True)

    class Meta:
        verbose_name_plural = 'points of interest'

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^geoposition\.fields\.GeopositionField"])
except ImportError:
    pass
