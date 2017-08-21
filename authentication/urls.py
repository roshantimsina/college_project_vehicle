from django.conf.urls import url
from django.contrib.auth import views as auth_views
from  .views import UserSignupForm



urlpatterns=[

url(r'^signup/$', UserSignupForm.as_view(), name='signup'),
url(r'^login/$', auth_views.login,{'template_name':'login.html'}, name='login'),
url(r'^logout/$', auth_views.logout,{'next_page':'/'}, name='logout'),
]