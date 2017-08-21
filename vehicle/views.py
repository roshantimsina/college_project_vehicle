from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from new_project.decorators import ajax_required
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic.detail import DetailView
from django.views import generic
from .models import Vehicle
from browse.models import Browse
from browse.models import BrowseImage
 

# class VehicleDetailView(DetailView):
#     model=Vehicle
#     template_name='vehicle/details.html'

#     def get_context_data(self, **kwargs):
#         context=super(VehicleDetailView,self).get_context_data(**kwargs)
#         return context

def vehicleDetail(request, pk):
    # vehicles = Vehicle.objects.filter(pk=pk)
    vehicles = Browse.objects.filter(pk=pk)
    img = BrowseImage.objects.filter(browse__pk=vehicles) 
    print(vehicles)
    return render(request, 'vecdetails.html', {
        'vehicles': vehicles,
        'img': img

        }) 


# @login_required
# @ajax_required
# def booking(request):
#     vehicle_id = request.POST['question']
#     vehicle = Vehicle.objects.get(pk=vehicle_id)
#     user = request.user
#     activity = Activity.objects.filter(activity_type=Activity.BOOK,
#                                        user=user, vehicle=vehicle_id)
#     if activity:
#         activity.delete()
#         user.profile.unotify_booked(vehicle)
#     else:
#         activity = Activity(activity_type=Activity.BOOK, user=user,
#                             vehicle=vehicle_id)
#         activity.save()
#         user.profile.notify_booked(vehicle)

#     return HttpResponse(vehicle.calculate_bookings())
