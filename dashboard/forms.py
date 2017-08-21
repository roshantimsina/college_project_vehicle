from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length = 30)
	last_name = forms.CharField(max_length = 30)
	bio = forms.CharField(max_length=30)
	contact = forms.CharField(max_length = 15)
	location = forms.CharField(max_length=30)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'bio', 'contact', 'location' )

