from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from activities.models import Activity
from vehicle.models import Vehicle
from .forms import BookingForm
# class BookingForm(LoginRequiredMixin, CreateView):

# 	model=Booking
# 	template_name='booking_form.html'
# 	fields=['user','vehicle_type','source','destination','vehicle_name','occupancy']
# 	success_url = '/'

# 	def get_initial(self):
# 		return {
#             "user": self.request.user
#         }
@login_required
def booking(request):
	user = request.user
	form = BookingForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			
			vehicle = Vehicle.objects.get(pk=2)
			
			activity = Activity.objects.filter(activity_type=Activity.BOOK,
                                       user=user, vehicle=2)
			if activity:
				activity.delete()
				user.profile.unotify_booked(vehicle)
			else:
				activity = Activity(activity_type=Activity.BOOK, user=user,
                            vehicle=2)
				activity.save()
				user.profile.notify_booked(vehicle)

			return redirect('/')
		else:
			return HttpResponse('Error')
	return render(request, 'booking_form.html', {'form':form} )

class BookingFormView(LoginRequiredMixin, FormView):
	form_class = BookingForm
	success_url = '/'
	template_name = 'booking_form.html'
	

	# def form_valid(self, form):
	# 	form.save()
	# 	return super(BookingFormView, self).form_valid(self)


	def post(self, request, *args, **kwargs):
		user = request.user
		form = self.get_form()
		if form.is_valid():
			vehicle_id = request.POST['vehicle']
			form.save()
			vehicle = Vehicle.objects.get(pk=vehicle_id)
			
			activity = Activity.objects.filter(activity_type=Activity.BOOK,
                                       user=user, vehicle=vehicle_id)
			if activity:
				activity.delete()
				user.profile.unotify_booked(vehicle)
			else:
				activity = Activity(activity_type=Activity.BOOK, user=user,
                            vehicle=vehicle_id)
				activity.save()
				user.profile.notify_booked(vehicle)

			return self.form_valid(form)
		else:
			return self.form_invalid(form)


	def get_initial(self):
		initial = super(BookingFormView, self).get_initial()
		initial = initial.copy()
		initial['user'] = self.request.user.pk

		return initial




