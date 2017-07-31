from django.contrib import admin

# Register your models here.
from .models import LoginForm,SignupForm
admin.site.register(LoginForm)
admin.site.register(SignupForm)
