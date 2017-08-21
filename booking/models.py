from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from vehicle.models import Vehicle



# Create your models here.



# TYPE=(
# 	('Bus','Bus'),
# 	('Taxi','Taxi'),
# 	('Micro','Micro'),
# 	('Tempo','Tempo'),
# 	)



class Booking(models.Model):
	user = models.ForeignKey(User, null=True)
	vehicle = models.ForeignKey(Vehicle, null = True)
	# vehicle_type = models.CharField(max_length=50,choices=TYPE)
	vehicle_name=models.CharField(max_length=50,null=True)
	source = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	booking_on = models.DateTimeField(auto_now_add=True)
	booked = models.BooleanField(default=False)
	booking_for = models.DateTimeField(null=True)
	occupancy = models.IntegerField(null=True)

	def __str__(self):
		return self.vehicle_name







		