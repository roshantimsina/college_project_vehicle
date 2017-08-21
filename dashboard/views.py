from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from booking.models  import Booking
from vehicle.models import Vehicle

class DashboardView(TemplateView):
	template_name = "dashboard.html"




def dashboard(request):
	vehicle = Vehicle.objects.filter(user = request.user)
	booking_list = Booking.objects.filter(vehicle = vehicle)
	print booking_list
	return render(request, 'dashboard.html', {'booking_list':booking_list,})