from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import vehicleDetail




urlpatterns = [

	url(r'^vehicle-detail/(?P<pk>[\d]+)$', vehicleDetail, name='vehicle_detail')
	

]