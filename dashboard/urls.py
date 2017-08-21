from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'^dash/$', views.dashboard, name='dash'),

]
