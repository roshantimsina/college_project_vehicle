from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from browse.models import Browse


class Vehicle(models.Model):
	user = models.ForeignKey(User, null=True)
	# vechile_type=models.CharField(max_length=200,choices=TYPE)
	vehicle_type = models.ForeignKey(Browse,null=True)
	vechile_number=models.PositiveIntegerField(null=True,blank=True)
	contact_number=models.PositiveIntegerField(null=True,blank=True)
	
	def __str__(self):
		return "Vehicle{}".format(self.vehicle_type)


	def calculate_bookings(self):
		bookings = Activity.objects.filter(activity_type=Activity.BOOK,
			vehicle=self.pk).count()
		self.bookings = bookings
		self.save()
		return self.bookings

		

class Route(models.Model):
	vechile_type=models.ForeignKey(Vehicle)
	source=models.CharField(max_length=50)
	destination=models.CharField(max_length=50)
	fare=models.IntegerField(null=True,blank=True)


	def __str__(self):
		return fare










