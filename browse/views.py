from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Browse,BrowseImage
from PIL import Image

class BrowseForm(LoginRequiredMixin, CreateView):

	model=Browse
	# template_name='booking_form.html'
	fields=['user','vehicle_type','source','destination','vehicle_name',]
	success_url = '/'

	def get_initial(self):
		return {
            "user": self.request.user
        }
