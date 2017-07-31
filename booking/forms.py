from django import forms
from .models import Booking


# TYPE=(
# 	('Bus','Bus'),
# 	('Taxi','Taxi'),
# 	('Micro','Micro'),
# 	('Tempo','Tempo'),
# 	)

class BookingForm(forms.ModelForm):

	vehicle_name = forms.CharField (
		widget = forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'vechile-name'}),
		max_length=50)

	source = forms.CharField(
		widget = forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'source'}),
		max_length=50)

	destination = forms.CharField(
		widget = forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'destination'}),
		max_length=50)

	# booked_on = forms.CharField(
	# 	widget = forms.TextInput (attrs={'class': 'form-control'}),
	# 	max_length=50)

	booking_for = forms.CharField(
		widget = forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'booking_for'}),
		max_length=50)

	occupancy = forms.CharField(
		widget = forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'occupancy'}),
		max_length=50)

	class Meta:
		model = Booking
		fields =['user','vehicle','vehicle_name','source','destination','booking_for','occupancy','booked']
