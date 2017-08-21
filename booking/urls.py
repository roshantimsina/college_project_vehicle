from django.conf.urls import url
from .views import BookingFormView

urlpatterns=[

url(r'^$',BookingFormView.as_view(),name='booking'),


]