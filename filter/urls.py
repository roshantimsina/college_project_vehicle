from django.conf.urls import url 
from .views import browsefilter

urlpatterns = [
	url(r'^browsefilter/$', browsefilter, name='brfilter'),
	
	]


	# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)