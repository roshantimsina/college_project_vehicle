from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.




TYPE=(
	('Bus','Bus'),
	('Taxi','Taxi'),
	('Micro','Micro'),
	('Tempo','Tempo'),
	)


class Browse(models.Model):
	user = models.ForeignKey(User)
	vehicle_type = models.CharField(max_length=50,choices=TYPE)
	vehicle_name=models.CharField(max_length=50,null=True)
	source = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	fare = models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.vehicle_type



class BrowseImage(models.Model):
    
    browse = models.ForeignKey(Browse)
    browse_image=models.ImageField(upload_to='browse')
